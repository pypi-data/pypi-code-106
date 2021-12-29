import re
import typing


__all__ = ["Properties"]


class Properties:
    """
    properties 파일을 파싱합니다.
    """
    def __init__(self):
        self.__loaded: bool = False
        self.__load_args: typing.Tuple[str, dict] = ("", {})
        self.__data: dict = {}

    def __setitem__(self, key, value) -> None:
        """
        속성을 설정합니다.

        :param key: 키 값
        :param value: 속성의 값
        :exception RuntimeError: 알 수 없는 이유로 실패할 때 발생합니다.
        """
        if not self.set_property(key, value):
            raise RuntimeError("Property setting failed.")

    def __getitem__(self, key) -> str:
        """
        속성을 가져옵니다.

        :param key: 키 값
        :exception KeyError: 속성이 존재하지 않을 때 발생합니다.
        :return: 속성의 값
        """
        return self.get_property(key)

    def __len__(self) -> int:
        """
        속성의 갯수를 가져옵니다.

        :return: 속성의 갯수
        """
        return len(self.__data)

    def __iter__(self) -> typing.Iterator:
        """
        이터레이터를 생성합니다.

        :return: 이터레이터
        """
        return iter(self.__data.keys())

    def load(self, file_name: str, **opt) -> bool:
        """
        properties 파일을 로드합니다.

        :param file_name: properties 파일 이름
        :param opt: 기타 스트림 옵션
        :return: 성공 여부
        """
        if self.__loaded:
            self.save(self.__load_args[0], **self.__load_args[1])
        self.__loaded = False
        try:
            with open(file=file_name, mode="r", **opt) as f:
                raw = re.sub("#.+\n", "", f.read())
                raw = re.split("(?<!\\\\)=|\n", raw)
                raw = [i.replace("\\=", "=") for i in raw]
                self.__data = dict(zip(raw[::2], raw[1::2]))
        except (IOError, TypeError):
            self.__loaded = False
            self.__load_args = ("", {})
            self.__data = {}
            return False
        self.__loaded = True
        self.__load_args = (file_name, opt)
        return True

    def save(self, file_name: str = None, **opt) -> bool:
        """
        properties 파일을 저장합니다.

        :param file_name: properties 파일 이름
        :param opt: 기타 스트림 옵션
        :return: 성공 여부
        """
        try:
            sl = "\\"
            raw = "\n".join(
                [f"{i[0].replace('=', sl + '=')}={i[1].replace('=', sl + '=')}"
                 for i in self.__data.items()])
            fn = self.__load_args[0] if file_name is None else file_name
            with open(file=fn, mode="w", **opt) as f:
                f.write(raw)
        except IOError:
            return False
        return True

    def set_property(self, key: str, value: str) -> bool:
        """
        속성을 설정합니다.

        :param key: 키 값
        :param value: 속성의 값
        :return: 성공 여부
        """
        if self.__loaded:
            self.__data[key] = value
            return True
        return False

    def get_property(self, key: str, default: str = None) -> str:
        """
        속성을 가져옵니다.

        :param key: 키 값
        :param default: 키가 존재하지 않을 경우 대체 값
        :exception KeyError: 속성이 존재하지 않을 때 발생합니다.
        :return: 속성의 값
        """
        if self.__loaded:
            if key in self.__data.keys():
                return self.__data[key]
            elif default is not None:
                return default
            raise KeyError("Property does not exist.")
        raise Exception("Cannot get property before load properties file.")

    def list(self) -> typing.List[str]:
        """
        속성들의 키 값 리스트를 가져옵니다.

        :return: 키 값 리스트
        """
        return list(self.__data.keys())
