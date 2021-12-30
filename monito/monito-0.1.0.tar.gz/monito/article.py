"""The article class for monito

LICENSE
   MIT (https://mit-license.org/)

COPYRIGHT
   © 2021 Steffen Brinkmann <s-b@mailbox.org>
"""

import json
import logging
import os
from dataclasses import asdict, dataclass, field

try:
    from tools import sanitize_filename
except ModuleNotFoundError:
    from .tools import sanitize_filename


@dataclass
class Article:
    """
    The article class
    """

    version: str = ""
    url: str = ""
    published: str = ""  # datetime = field(default_factory=datetime)
    outlet: str = ""
    title: str = ""
    subtitle: str = ""
    category: list[str] = field(default_factory=list)
    text: str = ""
    keywords: list[str] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)
    bag_of_words: list[str] = field(default_factory=list)
    places: list[str] = field(default_factory=list)
    people: list[str] = field(default_factory=list)
    orgs: list[str] = field(default_factory=list)
    legibility: dict = field(default_factory=dict)
    stats: dict = field(default_factory=dict)

    def dumps_json(self) -> str:
        """
        Return the article as a json string.
        """
        return json.dumps(asdict(self), indent=4, ensure_ascii=False)

    def dump_json(
        self,
        save_file: bool = True,
        outdir: str = ".",
        filename: str = None,
        heal_filename=True,
    ) -> str:
        """
        Save the article as a json file.
        If save_file is True, save to a file.
        If filename is None, the filename will be generated.
        Return the filename
        """

        if save_file:
            if not filename:
                filename = (
                    f"{self.published}__"
                    f"{self.outlet.replace(' ', '_')}__"
                    f"{self.category[-1].replace(' ', '_')}__"
                    f"{self.title.replace(' ', '_')}"
                )
            if heal_filename:
                filename = sanitize_filename(filename)
            filename += ".json"
            outpath = os.path.join(outdir, filename)

            if os.path.isfile(outpath):
                logging.warning(f"overwriting {outpath}")

            logging.info(f"saving file {outpath}")
            with open(outpath, "w", errors="replace1") as f:
                json.dump(asdict(self), f, indent=4, ensure_ascii=False)

        return filename


@dataclass
class Articles:
    """A list of articles"""

    articles: list[Article]


if __name__ == "__main__":
    logging.info("testing")

    art = Article()
    print(art)
    print(asdict(art))

    art = Article(title="The Title", outlet="The Outlet", published="2021-12-12")
    print(art)
    print(asdict(art))

    print(art.to_json())
