"""Module which defines functions to manage voice models."""

from __future__ import annotations

from typing import TYPE_CHECKING

import re
import shutil
import urllib.request
import zipfile
from pathlib import Path

from ultimate_rvc.common import (
    CUSTOM_EMBEDDER_MODELS_DIR,
    CUSTOM_PRETRAINED_MODELS_DIR,
    TRAINING_MODELS_DIR,
    VOICE_MODELS_DIR,
    lazy_import,
)
from ultimate_rvc.core.common import (
    copy_files_to_new_dir,
    display_progress,
    get_file_size,
    json_dump,
    json_load,
    validate_url,
)
from ultimate_rvc.core.exceptions import (
    Entity,
    Location,
    ModelExistsError,
    ModelNotFoundError,
    NotFoundError,
    NotProvidedError,
    PretrainedModelExistsError,
    PretrainedModelNotAvailableError,
    UIMessage,
    UploadLimitError,
    UploadTypeError,
)
from ultimate_rvc.core.manage.typing_extra import (
    PretrainedModelMetaDataTable,
    VoiceModelMetaData,
    VoiceModelMetaDataList,
    VoiceModelMetaDataPredicate,
    VoiceModelMetaDataTable,
    VoiceModelTagName,
)

if TYPE_CHECKING:
    from typing import NoReturn

    from _collections_abc import Sequence
    from concurrent import futures as concurrent_futures

    import requests

    import gradio as gr
    import tqdm

    from ultimate_rvc.typing_extra import PretrainedSampleRate, StrPath
else:
    requests = lazy_import("requests")
    tqdm = lazy_import("tqdm")
    concurrent_futures = lazy_import("concurrent.futures")

PUBLIC_MODELS_JSON = json_load(Path(__file__).parent / "public_models.json")
PUBLIC_MODELS_TABLE = VoiceModelMetaDataTable.model_validate(PUBLIC_MODELS_JSON)


def get_voice_model_names() -> list[str]:
    """
    Get the names of all saved voice models.

    Returns
    -------
    list[str]
        A list of names of all saved voice models.

    """
    if VOICE_MODELS_DIR.is_dir():
        model_paths = VOICE_MODELS_DIR.iterdir()
        return sorted(
            [model_path.name for model_path in model_paths],
        )
    return []


def get_custom_embedder_model_names() -> list[str]:
    """
    Get the names of all saved custom embedder models.

    Returns
    -------
    list[str]
        A list of the names of all saved custom embedder models.

    """
    if CUSTOM_EMBEDDER_MODELS_DIR.is_dir():
        return sorted(
            [model.name for model in CUSTOM_EMBEDDER_MODELS_DIR.iterdir()],
        )
    return []


def get_custom_pretrained_model_names() -> list[str]:
    """
    Get the names of all saved custom pretrained models.

    Returns
    -------
    list[str]
        A list of the names of all saved custom pretrained models.

    """
    if CUSTOM_PRETRAINED_MODELS_DIR.is_dir():
        return sorted(
            [
                model.name
                for model in CUSTOM_PRETRAINED_MODELS_DIR.iterdir()
                if model.name != "pretrains.json"
            ],
        )
    return []


def get_training_model_names() -> list[str]:
    """
    Get the names of all saved training models.

    Returns
    -------
    list[str]
        A list of the names of all saved training models.

    """
    if TRAINING_MODELS_DIR.is_dir():
        return sorted(
            [model.name for model in TRAINING_MODELS_DIR.iterdir()],
        )
    return []


def load_public_models_table(
    predicates: Sequence[VoiceModelMetaDataPredicate],
) -> VoiceModelMetaDataList:
    """
    Load table containing metadata of public voice models, optionally
    filtered by a set of predicates.

    Parameters
    ----------
    predicates : Sequence[VoiceModelMetaDataPredicate]
        Predicates to filter the metadata table by.

    Returns
    -------
    VoiceModelMetaDataList
        List containing metadata for each public voice model that
        satisfies the given predicates.

    """
    return [
        [
            model.name,
            model.description,
            model.tags,
            model.credit,
            model.added,
            model.url,
        ]
        for model in PUBLIC_MODELS_TABLE.models
        if all(predicate(model) for predicate in predicates)
    ]


def get_public_model_tags() -> list[VoiceModelTagName]:
    """
    Get the names of all valid public voice model tags.

    Returns
    -------
    list[str]
        A list of names of all valid public voice model tags.

    """
    return [tag.name for tag in PUBLIC_MODELS_TABLE.tags]


def filter_public_models_table(
    tags: Sequence[str],
    query: str,
) -> VoiceModelMetaDataList:
    """
    Filter table containing metadata of public voice models by tags and
    a search query.


    The search query is matched against the name, description, tags,
    credit,and added date of each entry in the metadata table. Case
    insensitive search is performed. If the search query is empty, the
    metadata table is filtered only bythe given tags.

    Parameters
    ----------
    tags : Sequence[str]
        Tags to filter the metadata table by.
    query : str
        Search query to filter the metadata table by.

    Returns
    -------
    VoiceModelMetaDataList
        List containing metadata for each public voice model that
        match the given tags and search query.

    """

    def _tags_predicate(model: VoiceModelMetaData) -> bool:
        return all(tag in model.tags for tag in tags)

    def _query_predicate(model: VoiceModelMetaData) -> bool:
        return (
            query.lower()
            in (
                f"{model.name} {model.description} {' '.join(model.tags)} "
                f"{model.credit} {model.added}"
            ).lower()
            if query
            else True
        )

    filter_fns = [_tags_predicate, _query_predicate]

    return load_public_models_table(filter_fns)


def get_pretrained_metadata() -> PretrainedModelMetaDataTable:
    """
    Get metadata for pretrained models available for download.

    Returns
    -------
    PretrainedModelMetaDataTable
        Table with metadata for pretrained models available for
        download.

    """
    CUSTOM_PRETRAINED_MODELS_DIR.mkdir(parents=True, exist_ok=True)
    pretrained_metadata_path = CUSTOM_PRETRAINED_MODELS_DIR / "pretrains.json"
    if pretrained_metadata_path.is_file():
        pretrained_metadata_dict = json_load(pretrained_metadata_path)
        pretrained_metadata = PretrainedModelMetaDataTable.model_validate(
            pretrained_metadata_dict,
        )
    else:
        try:
            json_url = "https://huggingface.co/JackismyShephard/ultimate-rvc/raw/main/pretrains.json"
            response = requests.get(json_url)
            response.raise_for_status()
            pretrained_metadata_dict = response.json()
            pretrained_metadata = PretrainedModelMetaDataTable.model_validate(
                pretrained_metadata_dict,
            )
            json_dump(pretrained_metadata_dict, pretrained_metadata_path)
        except requests.exceptions.RequestException:
            pretrained_metadata_dict = {
                "Titan": {
                    "32k": {
                        "D": (
                            "blaise-tk/TITAN/resolve/main/models/medium/"
                            "32k/pretrained/D-f032k-TITAN-Medium.pth"
                        ),
                        "G": (
                            "blaise-tk/TITAN/resolve/main/models/medium/"
                            "32k/pretrained/G-f032k-TITAN-Medium.pth"
                        ),
                    },
                },
            }
            pretrained_metadata = PretrainedModelMetaDataTable.model_validate(
                pretrained_metadata_dict,
            )
    return pretrained_metadata


def get_available_pretrained_model_names() -> list[str]:
    """
    Get the names of all pretrained models available for download.

    Returns
    -------
    list[str]
        The names of all pretrained models available for download.

    """
    return get_pretrained_metadata().keys()


def get_available_pretrained_sample_rates(name: str) -> list[PretrainedSampleRate]:
    """
    Get the samples rates for which instances of the pretrained model
    with the provided name are available for download.

    Parameters
    ----------
    name : str
        The name of the pretrained model for which to get available
        sample rates.

    Returns
    -------
    list[PretrainedSampleRate]
        The sample rates for which there are instances of the pretrained
        model with the provided name available for download.

    """
    pretrained_metadata = get_pretrained_metadata()
    pretrained_sample_rates = pretrained_metadata[name]

    return pretrained_sample_rates.keys()


def _extract_voice_model(
    zip_file: StrPath,
    extraction_dir: StrPath,
    remove_incomplete: bool = True,
    remove_zip: bool = False,
) -> None:
    """
    Extract a zipped voice model to a directory.

    Parameters
    ----------
    zip_file : StrPath
        The path to a zip file containing the voice model to extract.
    extraction_dir : StrPath
        The path to the directory to extract the voice model to.

    remove_incomplete : bool, default=True
        Whether to remove the extraction directory if the extraction
        process fails.
    remove_zip : bool, default=False
        Whether to remove the zip file once the extraction process is
        complete.

    Raises
    ------
    NotFoundError
        If no model file is found in the extracted zip file.

    """
    extraction_path = Path(extraction_dir)
    zip_path = Path(zip_file)
    extraction_completed = False
    try:
        extraction_path.mkdir(parents=True)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extraction_path)
        file_path_map = {
            ext: Path(root, name)
            for root, _, files in extraction_path.walk()
            for name in files
            for ext in [".index", ".pth"]
            if Path(name).suffix == ext
            and Path(root, name).stat().st_size
            > 1024 * (100 if ext == ".index" else 1024 * 40)
        }
        if ".pth" not in file_path_map:
            raise NotFoundError(
                entity=Entity.MODEL_FILE,
                location=Location.EXTRACTED_ZIP_FILE,
                is_path=False,
            )

        # move model and index file to root of the extraction directory
        for file_path in file_path_map.values():
            file_path.rename(extraction_path / file_path.name)

        # remove any sub-directories within the extraction directory
        for path in extraction_path.iterdir():
            if path.is_dir():
                shutil.rmtree(path)
        extraction_completed = True
    finally:
        if not extraction_completed and remove_incomplete and extraction_path.is_dir():
            shutil.rmtree(extraction_path)
        if remove_zip and zip_path.exists():
            zip_path.unlink()


def download_voice_model(
    url: str,
    name: str,
    progress_bar: gr.Progress | None = None,
    percentages: tuple[float, float] = (0.0, 0.5),
) -> None:
    """
    Download a zipped voice model.

    Parameters
    ----------
    url : str
        An URL pointing to a location where the zipped voice model can
        be downloaded from.
    name : str
        The name to give to the downloaded voice model.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentages : tuple[float, float], default=(0.0, 0.5)
        Percentages to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no URL or name is provided.
    ModelExistsError
        If a voice model with the provided name already exists.

    """
    if not url:
        raise NotProvidedError(entity=Entity.URL)
    if not name:
        raise NotProvidedError(entity=Entity.MODEL_NAME)
    name = name.strip()
    extraction_path = VOICE_MODELS_DIR / name
    if extraction_path.exists():
        raise ModelExistsError(Entity.VOICE_MODEL, name)

    validate_url(url)
    zip_name = url.split("/")[-1].split("?")[0]

    # NOTE in case huggingface link is a direct link rather
    # than a resolve link then convert it to a resolve link
    url = re.sub(
        r"https://huggingface.co/([^/]+)/([^/]+)/blob/(.*)",
        r"https://huggingface.co/\1/\2/resolve/\3",
        url,
    )
    if "pixeldrain.com" in url:
        url = f"https://pixeldrain.com/api/file/{zip_name}"

    display_progress(
        "[~] Downloading voice model ...",
        percentages[0],
        progress_bar,
    )
    urllib.request.urlretrieve(url, zip_name)  # noqa: S310

    display_progress("[~] Extracting zip file...", percentages[1], progress_bar)
    _extract_voice_model(zip_name, extraction_path, remove_zip=True)


def _download_pretrained_model_file(
    url: str,
    destination: StrPath,
    progress_bar: tqdm.tqdm[NoReturn] | None = None,
) -> None:
    """
    Download a pretrained model file.

    Parameters
    ----------
    url : str
        The URL of the pretrained model file to download.
    destination : strPath
        The destination to save the downloaded pretrained model file to.
    progress_bar : tqdm.tqdm, optional
        TQDM progress bar to update.

    """
    response = requests.get(url, stream=True)
    response.raise_for_status()
    block_size = 1024
    destination_path = Path(destination)
    with destination_path.open("wb") as file:
        for data in response.iter_content(block_size):
            file.write(data)
            if progress_bar:
                progress_bar.update(len(data))


def download_pretrained_model(
    name: str,
    sample_rate: PretrainedSampleRate,
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Download a pretrained model.

    Parameters
    ----------
    name : str
        The name of the pretrained model to download.
    sample_rate : PretrainedSampleRate
        The sample rate of the pretrained model to download.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    PretrainedModelExistsError
        If a pretrained model with the provided name and sample rate
        already exists.
    PretrainedModelNotAvailableError
        If a pretrained model with the provided name and sample rate is
        not available for download.

    """
    model_path = CUSTOM_PRETRAINED_MODELS_DIR / f"{name} {sample_rate}"
    if model_path.is_dir():
        raise PretrainedModelExistsError(name, sample_rate)

    pretrained_metadata = get_pretrained_metadata()

    available_model_names = pretrained_metadata.keys()
    if name not in available_model_names:
        raise PretrainedModelNotAvailableError(name)

    model_metadata = pretrained_metadata[name]
    available_sample_rates = model_metadata.keys()
    if sample_rate not in available_sample_rates:
        raise PretrainedModelNotAvailableError(name, sample_rate)
    paths = model_metadata[sample_rate]

    d_url = f"https://huggingface.co/{paths.D}"
    g_url = f"https://huggingface.co/{paths.G}"

    total_size = get_file_size(d_url) + get_file_size(g_url)

    display_progress("[~] Downloading pretrained model...", percentage, progress_bar)

    model_path.mkdir(parents=True)

    with (
        tqdm.tqdm(
            total=total_size,
            unit="iB",
            unit_scale=True,
            desc="Downloading files",
        ) as tqdm_bar,
        concurrent_futures.ThreadPoolExecutor() as executor,
    ):
        futures = [
            executor.submit(
                _download_pretrained_model_file,
                d_url,
                model_path / Path(paths.D).name,
                tqdm_bar,
            ),
            executor.submit(
                _download_pretrained_model_file,
                g_url,
                model_path / Path(paths.G).name,
                tqdm_bar,
            ),
        ]

        for future in futures:
            try:
                future.result()
            except requests.exceptions.RequestException as e:
                shutil.rmtree(model_path)
                raise PretrainedModelNotAvailableError(name, sample_rate) from e


def upload_voice_model(
    files: Sequence[StrPath],
    name: str,
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Upload a voice model from either a zip file or a .pth file and an
    optional index file.

    Parameters
    ----------
    files : Sequence[StrPath]
        Paths to the files to upload.
    name : str
        The name to give to the uploaded voice model.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no file paths or name are provided.
    ModelExistsError
        If a voice model with the provided name already
        exists.
    UploadTypeError
        If a single uploaded file is not a .pth file or a .zip file.
        If two uploaded files are not a .pth file and an .index file.
    UploadLimitError
        If more than two file paths are provided.

    """
    if not files:
        raise NotProvidedError(entity=Entity.FILES, ui_msg=UIMessage.NO_UPLOADED_FILES)
    if not name:
        raise NotProvidedError(entity=Entity.MODEL_NAME)
    name = name.strip()
    model_dir_path = VOICE_MODELS_DIR / name
    if model_dir_path.exists():
        raise ModelExistsError(Entity.VOICE_MODEL, name)
    sorted_file_paths = sorted([Path(f) for f in files], key=lambda f: f.suffix)
    match sorted_file_paths:
        case [file_path]:
            if file_path.suffix == ".pth":
                display_progress("[~] Copying .pth file ...", percentage, progress_bar)
                copy_files_to_new_dir([file_path], model_dir_path)
            # NOTE a .pth file is actually itself a zip file
            elif zipfile.is_zipfile(file_path):
                display_progress("[~] Extracting zip file...", percentage, progress_bar)
                _extract_voice_model(file_path, model_dir_path)
            else:
                raise UploadTypeError(
                    entity=Entity.FILES,
                    valid_types=[".pth", ".zip"],
                    type_class="formats",
                    multiple=False,
                )
        case [index_path, pth_path]:
            if index_path.suffix == ".index" and pth_path.suffix == ".pth":
                display_progress(
                    "[~] Copying .pth file and index file ...",
                    percentage,
                    progress_bar,
                )
                copy_files_to_new_dir([index_path, pth_path], model_dir_path)
            else:
                raise UploadTypeError(
                    entity=Entity.FILES,
                    valid_types=[".pth", ".index"],
                    type_class="formats",
                    multiple=True,
                )
        case _:
            raise UploadLimitError(entity=Entity.FILES, limit="two")


def _extract_custom_embedder_model(
    zip_file: StrPath,
    extraction_dir: StrPath,
    remove_incomplete: bool = True,
    remove_zip: bool = False,
) -> None:
    """
    Extract a zipped custom embedder model to a directory.

    Parameters
    ----------
    zip_file : StrPath
        The path to a zip file containing the custom embedder model to
        extract.
    extraction_dir : StrPath
        The path to the directory to extract the custom embedder model
        to.

    remove_incomplete : bool, default=True
        Whether to remove the extraction directory if the extraction
        process fails.
    remove_zip : bool, default=False
        Whether to remove the zip file once the extraction process is
        complete.

    Raises
    ------
    NotFoundError
        If no pytorch_model.bin file or config.json file is found in
        the extracted zip file.

    """
    extraction_path = Path(extraction_dir)
    zip_path = Path(zip_file)
    extraction_completed = False
    try:
        extraction_path.mkdir(parents=True)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extraction_path)
        file_path_map = {
            file: Path(root, file)
            for root, _, files in extraction_path.walk()
            for file in files
            if file in {"pytorch_model.bin", "config.json"}
        }
        if "config.json" not in file_path_map:
            raise NotFoundError(
                entity=Entity.CONFIG_JSON_FILE,
                location=Location.EXTRACTED_ZIP_FILE,
                is_path=False,
            )
        if "pytorch_model.bin" not in file_path_map:
            raise NotFoundError(
                entity=Entity.MODEL_BIN_FILE,
                location=Location.EXTRACTED_ZIP_FILE,
                is_path=False,
            )

        # move pytorch_model.bin file and config.json file to root of
        # the extraction directory
        for file_path in file_path_map.values():
            file_path.rename(extraction_path / file_path.name)

        # remove any sub-directories within the extraction directory
        for path in extraction_path.iterdir():
            if path.is_dir():
                shutil.rmtree(path)
        extraction_completed = True
    finally:
        if not extraction_completed and remove_incomplete and extraction_path.is_dir():
            shutil.rmtree(extraction_path)
        if remove_zip and zip_path.exists():
            zip_path.unlink()


def upload_custom_embedder_model(
    files: Sequence[StrPath],
    name: str,
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Upload a custom embedder model from either a zip file or a pair
    consisting of a pytorch_model.bin file and a config.json file.

    Parameters
    ----------
    files : Sequence[StrPath]
        Paths to the files to upload.
    name : str
        The name to give to the uploaded custom embedder model.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no name or file paths are provided.
    ModelExistsError
        If a custom embedder model with the provided name already
        exists.
    UploadTypeError
        If a single uploaded file is not a .zip file or two uploaded
        files are not named "pytorch_model.bin" and "config.json".
    UploadLimitError
        If more than two file paths are provided.

    """
    if not files:
        raise NotProvidedError(entity=Entity.FILES, ui_msg=UIMessage.NO_UPLOADED_FILES)
    if not name:
        raise NotProvidedError(entity=Entity.MODEL_NAME)
    name = name.strip()
    model_dir_path = CUSTOM_EMBEDDER_MODELS_DIR / name
    if model_dir_path.exists():
        raise ModelExistsError(Entity.CUSTOM_EMBEDDER_MODEL, name)
    sorted_file_paths = sorted([Path(f) for f in files], key=lambda f: f.suffix)
    match sorted_file_paths:
        case [file_path]:
            if zipfile.is_zipfile(file_path):
                display_progress("[~] Extracting zip file...", percentage, progress_bar)
                _extract_custom_embedder_model(file_path, model_dir_path)
            else:
                raise UploadTypeError(
                    entity=Entity.FILES,
                    valid_types=[".zip"],
                    type_class="formats",
                    multiple=False,
                )
        case [bin_path, json_path]:
            if bin_path.name == "pytorch_model.bin" and json_path.name == "config.json":
                display_progress(
                    "[~] Copying pytorch_model.bin file and config.json file ...",
                    percentage,
                    progress_bar,
                )
                copy_files_to_new_dir([bin_path, json_path], model_dir_path)
            else:
                raise UploadTypeError(
                    entity=Entity.FILES,
                    valid_types=["pytorch_model.bin", "config.json"],
                    type_class="names",
                    multiple=True,
                )
        case _:
            raise UploadLimitError(entity=Entity.FILES, limit="two")


def delete_voice_models(
    names: Sequence[str],
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete one or more voice models.

    Parameters
    ----------
    names : Sequence[str]
        Names of the voice models to delete.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no names are provided.
    ModelNotFoundError
        If a voice model with a provided name does not exist.

    """
    if not names:
        raise NotProvidedError(
            entity=Entity.MODEL_NAMES,
            ui_msg=UIMessage.NO_VOICE_MODELS,
        )
    model_dir_paths: list[Path] = []
    for name in names:
        model_dir_path = VOICE_MODELS_DIR / name
        if not model_dir_path.is_dir():
            raise ModelNotFoundError(Entity.VOICE_MODEL, name)
        model_dir_paths.append(model_dir_path)
    display_progress(
        "[~] Deleting voice models ...",
        percentage,
        progress_bar,
    )
    for model_dir_path in model_dir_paths:
        shutil.rmtree(model_dir_path)


def delete_custom_embedder_models(
    names: Sequence[str],
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete one or more custom embedder models.

    Parameters
    ----------
    names : Sequence[str]
        Names of the custom embedder models to delete.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no names are provided.
    ModelNotFoundError
        If a custom embedder model with a provided name does not exist.

    """
    if not names:
        raise NotProvidedError(
            entity=Entity.MODEL_NAMES,
            ui_msg=UIMessage.NO_CUSTOM_EMBEDDER_MODELS,
        )
    model_dir_paths: list[Path] = []
    for name in names:
        model_dir_path = CUSTOM_EMBEDDER_MODELS_DIR / name
        if not model_dir_path.is_dir():
            raise ModelNotFoundError(Entity.CUSTOM_EMBEDDER_MODEL, name)
        model_dir_paths.append(model_dir_path)
    display_progress(
        "[~] Deleting custom embedder models ...",
        percentage,
        progress_bar,
    )
    for model_dir_path in model_dir_paths:
        shutil.rmtree(model_dir_path)


def delete_custom_pretrained_models(
    names: Sequence[str],
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete one or more custom pretrained models.

    Parameters
    ----------
    names : Sequence[str]
        Names of the custom pretrained models to delete.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no names are provided.
    ModelNotFoundError
        If a custom pretrained model with a provided name does not
        exist.

    """
    if not names:
        raise NotProvidedError(
            entity=Entity.MODEL_NAMES,
            ui_msg=UIMessage.NO_CUSTOM_PRETRAINED_MODELS,
        )
    model_dir_paths: list[Path] = []
    for name in names:
        model_dir_path = CUSTOM_PRETRAINED_MODELS_DIR / name
        if not model_dir_path.is_dir():
            raise ModelNotFoundError(Entity.CUSTOM_PRETRAINED_MODEL, name)
        model_dir_paths.append(model_dir_path)
    display_progress(
        "[~] Deleting custom pretrained models ...",
        percentage,
        progress_bar,
    )
    for model_dir_path in model_dir_paths:
        shutil.rmtree(model_dir_path)


def delete_training_models(
    names: Sequence[str],
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete one or more training models.

    Parameters
    ----------
    names : Sequence[str]
        Names of the training models to delete.
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    Raises
    ------
    NotProvidedError
        If no names are provided.
    ModelNotFoundError
        If a training model with a provided name does not exist.

    """
    if not names:
        raise NotProvidedError(
            entity=Entity.MODEL_NAMES,
            ui_msg=UIMessage.NO_TRAINING_MODELS,
        )

    model_dir_paths: list[Path] = []
    for name in names:
        model_dir_path = TRAINING_MODELS_DIR / name
        if not model_dir_path.is_dir():
            raise ModelNotFoundError(Entity.TRAINING_MODEL, name)
        model_dir_paths.append(model_dir_path)

    display_progress(
        "[~] Deleting training models ...",
        percentage,
        progress_bar,
    )
    for model_dir_path in model_dir_paths:
        shutil.rmtree(model_dir_path)


def delete_all_voice_models(
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete all voice models.

    Parameters
    ----------
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    """
    display_progress("[~] Deleting all voice models ...", percentage, progress_bar)
    if VOICE_MODELS_DIR.is_dir():
        shutil.rmtree(VOICE_MODELS_DIR)


def delete_all_custom_embedder_models(
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete all custom embedder models.

    Parameters
    ----------
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    """
    display_progress(
        "[~] Deleting all custom embedder models ...",
        percentage,
        progress_bar,
    )
    if CUSTOM_EMBEDDER_MODELS_DIR.is_dir():
        shutil.rmtree(CUSTOM_EMBEDDER_MODELS_DIR)


def delete_all_custom_pretrained_models(
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete all custom pretrained models.

    Parameters
    ----------
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    """
    display_progress(
        "[~] Deleting all custom pretrained models ...",
        percentage,
        progress_bar,
    )
    if CUSTOM_PRETRAINED_MODELS_DIR.is_dir():
        shutil.rmtree(CUSTOM_PRETRAINED_MODELS_DIR)


def delete_all_training_models(
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete all training models.

    Parameters
    ----------
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    """
    display_progress("[~] Deleting all training models ...", percentage, progress_bar)
    if TRAINING_MODELS_DIR.is_dir():
        shutil.rmtree(TRAINING_MODELS_DIR)


def delete_all_models(
    progress_bar: gr.Progress | None = None,
    percentage: float = 0.5,
) -> None:
    """
    Delete all voice and training models.

    Parameters
    ----------
    progress_bar : gr.Progress, optional
        Gradio progress bar to update.
    percentage : float, default=0.5
        Percentage to display in the progress bar.

    """
    display_progress("[~] Deleting all models ...", percentage, progress_bar)
    delete_all_voice_models(progress_bar, percentage)
    delete_all_custom_embedder_models(progress_bar, percentage)
    delete_all_custom_pretrained_models(progress_bar, percentage)
    delete_all_training_models(progress_bar, percentage)
