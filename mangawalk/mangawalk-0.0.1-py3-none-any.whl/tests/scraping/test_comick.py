import unittest
from mangawalk.scraping.comick import ComicK
from mangawalk.scraping.types.type_comick import *
import time
from catswalk.scraping.types.type_webdriver import *
from catswalk.utils.functional import calc_time
import os

class TestComicK(unittest.TestCase):
    binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    executable_path = "/Users/rv/ws/tools/chromedriver"
    proxy = None
    headless = True
    url_list = ["https://comic.k-manga.jp/title/95912/pv", "https://comic.k-manga.jp/title/94017/pv", "https://comic.k-manga.jp/title/109519/pv"]


    @calc_time()
    def test_get_pv(self):
        """[python -m unittest tests.scraping.test_comick.TestComicK.test_get_pv]
        """
        request = ComicK(binary_location=self.binary_location, executable_path=self.executable_path, execution_env=EXECUTION_ENV.LOCAL_HEADLESS)
        request.init()
        result = request.get_pv("https://comic.k-manga.jp/title/95912/pv").to_csv()
        print(result)
        time.sleep(10)
    
    @calc_time()
    def test_get_pvs(self):
        """[python -m unittest tests.scraping.test_comick.TestComicK.test_get_pvs]
        """
        request = ComicK(binary_location=self.binary_location, executable_path=self.executable_path, execution_env=EXECUTION_ENV.LOCAL_HEADLESS, device = DEVICE.MOBILE_GALAXY_S5)
        request.init()
        results = ComicKPVResult.write_as_csv(request.get_pvs(self.url_list), "/tmp", "mangak_pvs")
        print(results)
        time.sleep(10)

    @calc_time()
    def test_save_comiclist_img(self):
        """[python -m unittest tests.scraping.test_comick.TestComicK.test_save_comiclist_img]
        """
        request = ComicK(binary_location=self.binary_location, executable_path=self.executable_path, execution_env=EXECUTION_ENV.LOCAL_HEADLESS,  device = DEVICE.MOBILE_GALAXY_S5)
        request.init()
        results = request.save_comiclist_img("/Users/rv/Desktop", "https://comic.k-manga.jp/title/95912/pv")
        print(results)
        time.sleep(10)

    @calc_time()
    def test_output_pvs(self):
        """[python -m unittest tests.scraping.test_comick.TestComicK.test_output_pvs]
        """
        request = ComicK(binary_location=self.binary_location, executable_path=self.executable_path, execution_env=EXECUTION_ENV.LOCAL_HEADLESS,  device = DEVICE.MOBILE_GALAXY_S5)
        request.init()
        base_path = os.getcwd() + "/output"
        results = request.output_pvs(self.url_list, base_path)
        print(request)
        print("end")
        time.sleep(10)

    @calc_time()
    def test_get_rank(self):
        """[python -m unittest tests.scraping.test_comick.TestComicK.test_get_rank]
        """
        rr = ComicK.get_rank()
        for r in rr:
            print(r)
        #time.sleep(10)


if __name__ == "__main__":
    unittest.main()