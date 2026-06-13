"""
Contains logic for file manipulation
"""
import os
from PIL import Image
from pathlib import Path


class FileProcessingError(Exception):
    """
    Core module Exception
    """

class FileProcessing:
    @staticmethod
    def validate_file(filename: str | Path) -> None:
        path = Path(filename)
        if not path.exists():
            raise FileProcessingError(f'File "{filename}" does not exist')
        if not path.is_file():
            raise FileProcessingError(f'"{filename}" is not a file')
        if not os.access(path, os.R_OK):
            raise FileProcessingError(f'File "{filename}" is not readable')
        if not os.access(path, os.W_OK):
            raise FileProcessingError(f'File "{filename}" is not writable')

    @staticmethod
    def get_new_filename(filename: str | Path) -> str:
        # assume file is already validated
        path = Path(filename)
        return str(path.parent.absolute() / f"processed-{path.name}")

    @staticmethod
    def resize_image(image_path: str | Path, width: int, height: int, new_image_path: str | None = None) -> None:
        path = Path(image_path)
        FileProcessing.validate_file(path)
        try:
            with Image.open(path) as fp:
                img = fp.resize((width, height))
            img.save(
                fp=new_image_path if new_image_path else FileProcessing.get_new_filename(path)
            )
        except OSError as exc:
            raise FileProcessingError("Error occurred during image resizing") from exc

    @staticmethod
    def display_image(image_path: str | Path) -> None:
        FileProcessing.validate_file(image_path)
        try:
            # TODO: try to write your own or use some existing gui library
           with Image.open(image_path) as img:
              img.show()
        except OSError as exc:
            raise FileProcessingError(f'Failed to display image "{image_path}"') from exc

    @staticmethod
    def get_file_metadata(filename: str | Path) -> dict:
        FileProcessing.validate_file(filename)
        try:
            with Image.open(filename) as img:
                return {
                    "format": img.format,
                    "width": img.size[0],
                    "height": img.size[1],
                    "mode": img.mode,
                }
        except OSError as exc:
            raise FileProcessingError("Error occurred during extraction of file metadata") from exc

if __name__ == "__main__":
    image_path = "data/shuttle.jpg"
    path = Path(image_path)
    print(path)
    print(Path(path))
    print(FileProcessing.get_file_metadata(image_path))
