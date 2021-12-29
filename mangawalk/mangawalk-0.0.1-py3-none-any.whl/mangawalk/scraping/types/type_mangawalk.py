from dataclasses import dataclass
from typing import List, Mapping
from bs4 import BeautifulSoup
from requests import Response as R
import logging
from enum import Enum
import pandas as pd
import csv
from mangawalk.utils.dateutils import created_at


@dataclass
class PVResult:
    """[summary]
    """
    id: str
    url: str
    title: str
    author: str

@dataclass
class PVResultWithCapture:
    id: str
    url: str
    title: str
    author: str
    site: str
    created_at = created_at()
    comiklist_capture_path: str

    @classmethod
    def convert_from_pv(cls, r:PVResult, site:str, comiklist_capture_path:str):
        """[summary]

        Args:
            r (PVResult): [description]
            site (str): [description]
            comiklist_capture_path (str): [description]

        Returns:
            [type]: [description]
        """
        return PVResultWithCapture(
            id = r.id, 
            url = r.url,
            title = r.title,
            author = r.author,
            site = site,
            comiklist_capture_path=comiklist_capture_path
            )
    
    @classmethod
    def to_pandas(cls, r):
        """[summary]

        Args:
            r ([type]): [description]

        Returns:
            [type]: [description]
        """
        return pd.DataFrame(r)

    @classmethod
    def write_as_csv(cls, r, path:str, filename: str) -> str:
        """[summary]

        Args:
            r ([type]): [description]
            path (str): [description]
            filename (str): [description]

        Returns:
            str: [description]
        """
        output_file = f'{path}/{filename}.csv'
        df = PVResultWithCapture.to_pandas(r)
        df.to_csv(output_file, sep=',', encoding='utf-8', index=False, quotechar='"', quoting=csv.QUOTE_ALL)
        print(df)
        return output_file