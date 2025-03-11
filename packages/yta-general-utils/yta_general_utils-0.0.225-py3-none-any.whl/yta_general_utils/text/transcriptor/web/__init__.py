"""
Module to handle the html file that allows us using
the web navigator speech recognition system.
"""
from yta_general_utils.programming.path import get_project_abspath
from yta_general_utils.file.checker import FileValidator
from yta_general_utils.downloader import Downloader


TRANSCRIBER_HTML_FILENAME = 'transcribe.html'

def download_web_file():
    """
    Download the html file from Google Drive if
    not available locally.
    """
    file_abspath = f'{get_project_abspath()}{TRANSCRIBER_HTML_FILENAME}'

    if not FileValidator.file_exists(file_abspath):
        Downloader.download_google_drive_resource(
            'https://drive.google.com/file/d/1KQs6D7Zmd2Oj7mT4JTV8S38e2ITu_gUs/view?usp=sharing',
            TRANSCRIBER_HTML_FILENAME
        )

download_web_file()