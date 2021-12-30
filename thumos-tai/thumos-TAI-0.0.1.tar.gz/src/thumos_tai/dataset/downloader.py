import os
import zipfile
import gdown


class StockDataDownloader:
    def __init__(self, exchange: str, output_dir: str):
        self.exchange = exchange
        self.output_dir = output_dir
        self.nasdaq_url = 'https://drive.google.com/uc?id=1Te_B2dIChh3WFXPGz4iCq94G8LI1xxgp'
        self.nyse_url = 'https://drive.google.com/uc?id=17KCevcvfp4eA6KhOXRQSY0Mc-Vd8URtO'
        self.temp_file_name = "tmp"

    def download(self):
        if self.exchange == 'nasdaq':
            url = self.nasdaq_url
        else:
            url = self.nyse_url
        temp_file_path = os.path.join(self.output_dir, self.temp_file_name)
        gdown.download(url, temp_file_path, quiet=True)
        with zipfile.ZipFile(temp_file_path, 'r') as zip_ref:
            zip_ref.extractall(path=self.output_dir)
        os.remove(temp_file_path)