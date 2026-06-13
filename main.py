"""
Project entrypoint
"""

import sys

import typer
from typing import Annotated

sys.path.insert(0, "./src")  # this is bad - must be removed
from bumbufile.core import FileProcessingError, FileProcessing
from bumbufile.console import progress

app = typer.Typer()

@app.command(
    name="resize-image",
    help="Resize an image to defined height and width",
)
def resize_image(
    width: Annotated[  # when i was doing typer.Option, I couldn't use both long and short form -w/--width for some reason
        int,
        typer.Option(
            "--width",
            "-w",
            help="Image width",
        )
    ],
    height: Annotated[
        int,
        typer.Option(
            "--height",
            "-h",
            help="Image height",
        )
    ],
    image_path: str = typer.Argument(
        help = "Path on the filesystem to the image to be resized"
    ),
    resized_image_path: Annotated[
        str | None,
        typer.Option(
            "--resized-image-path",
            "-r",
            help = 'Path to which the resized image will be saved - if not provided, defaults to original name of the image with prefix "resized-"',
        )
    ] = None,
):
    try:
        with progress() as prgs:
            prgs.add_task(description="Resizing image", total=None)
            FileProcessing.resize_image(
                image_path=image_path,
                width=width,
                height=height,
                new_image_path=resized_image_path,
            )
    except FileProcessingError as exc:
        raise exc
        print(f"Error occurred: {exc}")  # use rich of course

@app.command(
    name="--web",
    help="Launch web interface to perform all the file operations in the browser",
)
def web():
    pass

if __name__ == "__main__":
    app()
