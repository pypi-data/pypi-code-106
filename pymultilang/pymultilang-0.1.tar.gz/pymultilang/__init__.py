from enum import Enum


class LanguageNotProvided(Exception):

    def __init__(self, lang: Enum):
        super().__init__(f"This phrase does not support this language ({lang.name},{lang.value})")


class Languages(Enum):
    ru = "Русский"
    en = "English"


class __BasePhrase:
    _storage: dict

    def __init__(self):
        self._storage = dict()

    def __get_text_by_lang(self, lang: Enum):
        if lang.name in self._storage.keys():
            return self._storage[lang.name]
        raise LanguageNotProvided(lang)

    def ru(self):
        return self.__get_text_by_lang(Languages.ru)

    def en(self):
        return self.__get_text_by_lang(Languages.en)


class Phrase(__BasePhrase):
    _storage: dict

    def __init__(self, **kwargs):
        super().__init__()
        for item in kwargs.items():
            lang, phrase = item[0], item[1]
            if lang in Languages.__members__ and isinstance(phrase, str):
                self._storage[lang] = phrase

    def __repr__(self):
        return f"<Phrase: {self._storage}>"
