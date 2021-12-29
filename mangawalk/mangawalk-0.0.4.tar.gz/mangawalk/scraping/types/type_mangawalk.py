from dataclasses import dataclass
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
    def csv_header(cls):
        return f"id,url,title,author,site,created_at,comiklist_capture_path"

    def to_csv_format(self):
        return f"{self.id},{self.url},{self.title},{self.author},{self.site},{self.created_at},{self.comiklist_capture_path}"

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
        # lambdaのファイル上限に引っかかるため、pandasが使えない
        # df.to_csv(output_file, sep=',', encoding='utf-8', index=False, quotechar='"', quoting=csv.QUOTE_ALL)
        csv_str = "\n".join(list(map(lambda x: x.to_csv_format(), r)))
        print(PVResultWithCapture.csv_header())
        print(csv_str)
        with open(output_file, 'w') as f:
            f.write(PVResultWithCapture.csv_header() + '\n')
            f.write(csv_str)
        return output_file