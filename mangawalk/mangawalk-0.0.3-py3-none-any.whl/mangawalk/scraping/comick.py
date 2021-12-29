from catswalk.scraping.webdriver import CWWebDriver
from catswalk.scraping.request import CWRequest
from catswalk.scraping.types.type_webdriver import  EXECUTION_ENV, DEVICE, DEVICE_MODE
from mangawalk.scraping.types.type_comick import *
from mangawalk.scraping.types.type_mangawalk import *
import logging
from mangawalk.utils.dateutils import created_at
import os

logger = logging.getLogger()

class ComicKException(Exception):
    pass


class ComicK:
    def __init__(self, binary_location: str = None, executable_path: str = None, execution_env: EXECUTION_ENV = EXECUTION_ENV.LOCAL,  device: DEVICE = DEVICE.DESKTOP_GENERAL, proxy: str = None):
        """[summary]

        Args:
            binary_location (str): [description]
            executable_path (str): [description]
            execution_env (str, optional): [local, local_headless, aws]. Defaults to "local".
            proxy (str, optional): [description]. Defaults to None.
        """
        self.cw_driver = CWWebDriver(binary_location=binary_location, executable_path=executable_path, execution_env=execution_env, proxy=proxy, device=device)
        self.device_mode = device.value.mode

    def __enter__(self):
        """

        :return:
        """
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.close()

    def close(self):
        """[Close WebDriverSession, if chromewebdriver dosen't kill, plsease execute "killall chromedriver"]
        
        """
        self.cw_driver.close()

    def init(self):
        self.transition_home()

    def transition_home(self):
        self.cw_driver.transition(url=ComicKURL.HOME.value)

    @classmethod
    def get_rank(cls, comicK_rank_gen: ComicKRankGen = ComicKRankGen.TOTAL, comicK_rank_duration: ComicKRankDuration = ComicKRankDuration.DAILY, comicK_rank_sex: ComicKRankSex = ComicKRankSex.COMMON):
        """[Get ranling]

        Args:
            comicK_rank_gen (ComicKRankGen, optional): [description]. Defaults to ComicKRankGen.GENERAL.
            comicK_rank_duration (ComicKRankDuration, optional): [description]. Defaults to ComicKRankDuration.DAILY.
            comicK_rank_sex (ComicKRankSex, optional): [description]. Defaults to ComicKRankSex.COMMON.
        """

        with CWRequest() as request:
            base_url = ComicKURL.RANK.value

            if comicK_rank_gen != ComicKRankGen.TOTAL:
                base_url = f"{base_url}/{comicK_rank_gen.value}"

            if comicK_rank_duration != ComicKRankDuration.DAILY:
                base_url = f"{base_url}/{comicK_rank_duration.value}"

            if comicK_rank_sex != ComicKRankSex.COMMON:
                base_url = f"{base_url}/{comicK_rank_sex.value}"

            bs = request.get(base_url, "html").content
            ranks = list(map(lambda x: x['href'], bs.findAll("a", {"class": "book-list--item"})))
            # pv_detail_title = list(map(lambda x: x.text, content.findAll("dt", {"class": "book-info--detail-title"})))
            return ranks

    def get_pv(self, url: str) -> PVResult:
        """[get pv info
        EX. https://comic.k-manga.jp/title/128536/pv
        ]

        Args:
            id (str): [description]
            output_path (str): [description]

        Raises:
            ComicKException: [description]

        Returns:
            PVResult: [description]
        """
        id = url.split("/")[-2]
        logger.info(f"get_pv: {url}")
       
        # モバイル対応のため、contentはrequestで取得する
        with CWRequest() as request:
            content = request.get(url, "html").content
            title = content.find("h1", {"class": "book-info--title"}).find("span", {"itemprop": "name"}).text 
            pv_detail_title = list(map(lambda x: x.text, content.findAll("dt", {"class": "book-info--detail-title"})))
            pv_detail_item = list(map(lambda x: x.text, content.findAll("dd", {"class": "book-info--detail-item"})))

            if len(pv_detail_title) != len(pv_detail_item):
                raise ComicKException(f"pv_detail_title and pv_detail_item dosen't match {len(pv_detail_title)}, {len(pv_detail_title)}")
            pv_detail = dict(zip(pv_detail_title, pv_detail_item))


        #  content=content.find("div", {"id": "contents"}),
            
        result = PVResult(id=id,
                                url=url,
                                title=title,
                                author=pv_detail["著者・作者"]
                                )
        return result

    def get_pv_by_id(self, id: str) -> PVResult:
        """[get pv info
        EX. https://comic.k-manga.jp/title/128536/pv
        ]

        Args:
            id (str): [description]
            output_path (str): [description]

        Raises:
            ComicKException: [description]

        Returns:
            ComicKPVResult: [description]
        """
        url = ComicKURL.PV.value.format((id))
        result = self.get_pv(url=url)
        return result

    def get_pvs(self, url_list: List[str]) -> List[PVResult]:
        """[get pv info
        EX. [https://comic.k-manga.jp/title/128536/pv]
        ]
        """
        results = list(map(lambda url: self.get_pv(url=url), url_list))
        return results

    def save_comiclist_img(self, output_path: str, url:str, filename:str = "comiclist_img") -> str:
        """[summary]

        Args:
            output_path (str): [description]
        """
        #xpath = '//*[@id="contents"]/div[2]/section[2]'
        #book-chapter book-chapter__pv active
        self.cw_driver.get(url=url)
        if self.device_mode == DEVICE_MODE.MOBILE:
            # expand list
            # gaevent-detail-notlogin-bookchapter btn

            self.cw_driver.click_by_class_name("gaevent-detail-notlogin-bookchapter")
            print("clicked")

            self.cw_driver.move_to_element_by_class_name("x-book-chapter--target")
            print("moved")

            save_path = self.cw_driver.print_screen_by_class_name(class_name = "x-book-chapter--target", output_path=output_path, filename=filename)
            print("captured")

        else:
            save_path = self.cw_driver.print_screen_by_class_name(class_name = "book-chapter", output_path=output_path, filename=filename)
        return save_path


    def output_pvs(self, url_lst: List[str], output_path:str) -> str:
        """[summary]

        Args:
            ids (List[str]): [description]
            output_path ([type]): [description]

        Returns:
            List[ComicKPVResult]: [description]
        """
        os.makedirs(output_path, exist_ok=True)
        comick_output_path = f"{output_path}/comick"
        comick_output_result_path = f"{comick_output_path}/result"
        os.makedirs(comick_output_result_path, exist_ok=True)
        comick_output_img_path = f"{comick_output_path}/img"
        os.makedirs(comick_output_img_path, exist_ok=True)

        # capture
        def __mk_output_pvs(r: PVResult) -> PVResultWithCapture:
            comiklist_capture_path = self.save_comiclist_img(output_path=comick_output_img_path, url=r.url, filename=f"{r.title}_comicklist")
            return PVResultWithCapture.convert_from_pv(r=r, comiklist_capture_path=comiklist_capture_path, site=SITE_NAME)

        pvs_list = self.get_pvs(url_list=url_lst)
        pvs_with_capture_list = list(map(lambda r: __mk_output_pvs(r), pvs_list))

        path = PVResultWithCapture.write_as_csv(pvs_with_capture_list, comick_output_result_path, f"mangawalk_pv_{created_at()}")

        return path