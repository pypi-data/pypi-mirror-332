from typing import List, Optional

import typer
from typing_extensions import Annotated

from inference_cli.lib.env import ROBOFLOW_API_KEY
from inference_cli.lib.roboflow_cloud.common import ensure_api_key_is_set
from inference_cli.lib.roboflow_cloud.data_staging import api_operations

data_staging_app = typer.Typer(
    help="Commands for interacting with Roboflow Data Staging. THIS IS ALPHA PREVIEW OF THE FEATURE."
)


@data_staging_app.command(help="List staging batches in your workspace.")
def list_batches(
    api_key: Annotated[
        Optional[str],
        typer.Option(
            "--api-key",
            "-a",
            help="Roboflow API key for your workspace. If not given - env variable `ROBOFLOW_API_KEY` will be used",
        ),
    ] = None,
    pages: Annotated[
        int,
        typer.Option("--pages", "-p", help="Number of pages to pull"),
    ] = 1,
    page_size: Annotated[
        Optional[int],
        typer.Option("--page-size", help="Size of pagination page"),
    ] = None,
    debug_mode: Annotated[
        bool,
        typer.Option(
            "--debug-mode/--no-debug-mode",
            help="Flag enabling errors stack traces to be displayed (helpful for debugging)",
        ),
    ] = False,
) -> None:
    if api_key is None:
        api_key = ROBOFLOW_API_KEY
    try:
        ensure_api_key_is_set(api_key=api_key)
        api_operations.display_batches(
            api_key=api_key, pages=pages, page_size=page_size
        )
    except KeyboardInterrupt:
        print("Command interrupted.")
        raise typer.Exit(code=2)
    except Exception as error:
        if debug_mode:
            raise error
        typer.echo(f"Command failed. Cause: {error}")
        raise typer.Exit(code=1)


@data_staging_app.command(help="List content of individual batch.")
def list_batch_content(
    batch_id: Annotated[
        str,
        typer.Option(
            "--batch-id",
            "-b",
            help="Identifier of new batch (must be lower-cased letters with '-' and '_' allowed",
        ),
    ],
    part_names: Annotated[
        Optional[List[str]],
        typer.Option(
            "--part-name",
            "-pn",
            help="Name of the part to be listed (if not given - all parts are presented). Invalid if batch is "
            "not multipart",
        ),
    ] = None,
    limit: Annotated[
        Optional[int],
        typer.Option(
            "--limit",
            "-l",
            help="Number of entries to display / dump into th output files. If not given - whole "
            "content will be presented.",
        ),
    ] = None,
    output_file: Annotated[
        Optional[str],
        typer.Option(
            "--output-file",
            "-o",
            help="Path to the output file - if not provided, command will dump result to the console. "
            "File type is JSONL.",
        ),
    ] = None,
    api_key: Annotated[
        Optional[str],
        typer.Option(
            "--api-key",
            "-a",
            help="Roboflow API key for your workspace. If not given - env variable `ROBOFLOW_API_KEY` will be used",
        ),
    ] = None,
    debug_mode: Annotated[
        bool,
        typer.Option(
            "--debug-mode/--no-debug-mode",
            help="Flag enabling errors stack traces to be displayed (helpful for debugging)",
        ),
    ] = False,
) -> None:
    if api_key is None:
        api_key = ROBOFLOW_API_KEY
    if part_names:
        part_names = set(part_names)
    else:
        # this is needed - just Typer things - part_names is empty list instead of node, and we need default
        part_names = None
    try:
        ensure_api_key_is_set(api_key=api_key)
        api_operations.get_batch_content(
            batch_id=batch_id,
            api_key=api_key,
            part_names=part_names,
            limit=limit,
            output_file=output_file,
        )
    except KeyboardInterrupt:
        print("Command interrupted.")
        raise typer.Exit(code=2)
    except Exception as error:
        if debug_mode:
            raise error
        typer.echo(f"Command failed. Cause: {error}")
        raise typer.Exit(code=1)


@data_staging_app.command(help="Create new batch with your images.")
def create_batch_of_images(
    batch_id: Annotated[
        str,
        typer.Option(
            "--batch-id",
            "-b",
            help="Identifier of new batch (must be lower-cased letters with '-' and '_' allowed",
        ),
    ],
    images_dir: Annotated[
        str,
        typer.Option(
            "--images-dir",
            "-i",
            help="Path to your images directory to upload",
        ),
    ],
    batch_name: Annotated[
        Optional[str],
        typer.Option(
            "--batch-name",
            "-bn",
            help="Display name of your batch",
        ),
    ] = None,
    api_key: Annotated[
        Optional[str],
        typer.Option(
            "--api-key",
            "-a",
            help="Roboflow API key for your workspace. If not given - env variable `ROBOFLOW_API_KEY` will be used",
        ),
    ] = None,
    debug_mode: Annotated[
        bool,
        typer.Option(
            "--debug-mode/--no-debug-mode",
            help="Flag enabling errors stack traces to be displayed (helpful for debugging)",
        ),
    ] = False,
) -> None:
    if api_key is None:
        api_key = ROBOFLOW_API_KEY
    try:
        ensure_api_key_is_set(api_key=api_key)
        api_operations.create_images_batch_from_directory(
            directory=images_dir,
            batch_id=batch_id,
            api_key=api_key,
            batch_name=batch_name,
        )
    except KeyboardInterrupt:
        print("Command interrupted.")
        raise typer.Exit(code=2)
    except Exception as error:
        if debug_mode:
            raise error
        typer.echo(f"Command failed. Cause: {error}")
        raise typer.Exit(code=1)


@data_staging_app.command(help="Create new batch with your videos.")
def create_batch_of_videos(
    batch_id: Annotated[
        str,
        typer.Option(
            "--batch-id",
            "-b",
            help="Identifier of new batch (must be lower-cased letters with '-' and '_' allowed",
        ),
    ],
    videos_dir: Annotated[
        str,
        typer.Option(
            "--videos-dir",
            "-v",
            help="Path to your videos directory to upload",
        ),
    ],
    api_key: Annotated[
        Optional[str],
        typer.Option(
            "--api-key",
            "-a",
            help="Roboflow API key for your workspace. If not given - env variable `ROBOFLOW_API_KEY` will be used",
        ),
    ] = None,
    batch_name: Annotated[
        Optional[str],
        typer.Option(
            "--batch-name",
            "-bn",
            help="Display name of your batch",
        ),
    ] = None,
    debug_mode: Annotated[
        bool,
        typer.Option(
            "--debug-mode/--no-debug-mode",
            help="Flag enabling errors stack traces to be displayed (helpful for debugging)",
        ),
    ] = False,
) -> None:
    if api_key is None:
        api_key = ROBOFLOW_API_KEY
    try:
        ensure_api_key_is_set(api_key=api_key)
        api_operations.create_videos_batch_from_directory(
            directory=videos_dir,
            batch_id=batch_id,
            api_key=api_key,
            batch_name=batch_name,
        )
    except KeyboardInterrupt:
        print("Command interrupted.")
        return
    except Exception as error:
        if debug_mode:
            raise error
        typer.echo(f"Command failed. Cause: {error}")
        raise typer.Exit(code=1)


@data_staging_app.command(help="Show batch details")
def show_batch_details(
    batch_id: Annotated[
        str,
        typer.Option(
            "--batch-id",
            "-b",
            help="Identifier of new batch (must be lower-cased letters with '-' and '_' allowed",
        ),
    ],
    api_key: Annotated[
        Optional[str],
        typer.Option(
            "--api-key",
            "-a",
            help="Roboflow API key for your workspace. If not given - env variable `ROBOFLOW_API_KEY` will be used",
        ),
    ] = None,
    debug_mode: Annotated[
        bool,
        typer.Option(
            "--debug-mode/--no-debug-mode",
            help="Flag enabling errors stack traces to be displayed (helpful for debugging)",
        ),
    ] = False,
) -> None:
    if api_key is None:
        api_key = ROBOFLOW_API_KEY
    try:
        ensure_api_key_is_set(api_key=api_key)
        api_operations.display_batch_details(batch_id=batch_id, api_key=api_key)
    except KeyboardInterrupt:
        print("Command interrupted.")
        raise typer.Exit(code=1)
    except Exception as error:
        if debug_mode:
            raise error
        typer.echo(f"Command failed. Cause: {error}")
        raise typer.Exit(code=1)


@data_staging_app.command(help="Export batch")
def export_batch(
    batch_id: Annotated[
        str,
        typer.Option(
            "--batch-id",
            "-b",
            help="Identifier of new batch (must be lower-cased letters with '-' and '_' allowed",
        ),
    ],
    target_dir: Annotated[
        str,
        typer.Option(
            "--target-dir",
            "-t",
            help="Path to export directory",
        ),
    ],
    part_names: Annotated[
        Optional[List[str]],
        typer.Option(
            "--part-name",
            "-pn",
            help="Name of the part to be exported (if not given - all parts are presented). Invalid if batch is "
            "not multipart",
        ),
    ] = None,
    api_key: Annotated[
        Optional[str],
        typer.Option(
            "--api-key",
            "-a",
            help="Roboflow API key for your workspace. If not given - env variable `ROBOFLOW_API_KEY` will be used",
        ),
    ] = None,
    override_existing: Annotated[
        bool,
        typer.Option(
            "--override-existing/--no-override-existing",
            help="Flag to enforce export even if partial content is already exported",
        ),
    ] = False,
    debug_mode: Annotated[
        bool,
        typer.Option(
            "--debug-mode/--no-debug-mode",
            help="Flag enabling errors stack traces to be displayed (helpful for debugging)",
        ),
    ] = False,
) -> None:
    if api_key is None:
        api_key = ROBOFLOW_API_KEY
    if part_names:
        part_names = set(part_names)
    else:
        # this is needed - just Typer things - part_names is empty list instead of node, and we need default
        part_names = None
    try:
        ensure_api_key_is_set(api_key=api_key)
        api_operations.export_data(
            batch_id=batch_id,
            api_key=api_key,
            target_directory=target_dir,
            part_names=part_names,
            override_existing=override_existing,
        )
    except KeyboardInterrupt:
        print("Command interrupted.")
        raise typer.Exit(code=2)
    except Exception as error:
        if debug_mode:
            raise error
        typer.echo(f"Command failed. Cause: {error}")
        raise typer.Exit(code=1)
