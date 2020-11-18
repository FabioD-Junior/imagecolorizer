import urllib.request
import zipfile
import os.path


def _download_model():
    checkpoints_file = 'checkpoints.zip'
    if not os.path.isfile(checkpoints_file):
        print(f"Downloading {checkpoints_file}")
        urllib.request.urlretrieve('https://github.com/guilhermesilveira/imagecolorizer/releases/download/0.1.2/checkpoints.zip', checkpoints_file)

    checkpoints_dir = "checkpoints"
    if not os.path.isdir(checkpoints_dir):
        print(f"Unziping {checkpoints_file}")
        with zipfile.ZipFile(checkpoints_file, 'r') as zip_ref:
            zip_ref.extractall('.')

class ImageColorizer:
    def __init__(self):
        _download_model()
