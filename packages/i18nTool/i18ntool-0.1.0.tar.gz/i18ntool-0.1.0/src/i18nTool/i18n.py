"""
MIT License
Copyright (c) 2025 weinibuliu
"""

from pathlib import Path
from typing import List, Literal, Optional, Union

from .flags import Flags
from .read import Read


class I18n:
    _lang = ""
    _default_text = "Undefined"
    _data = _tran_data = {}

    def __init__(
        self,
        langs: Union[List[str], str],
        lang: str = "",
        path: Union[Path, str, None] = "translation",
        file_type: Literal["json", "yaml", "yml"] = "yml",
        default_text: str = "Undefined",
    ) -> None:
        """
        :params langs: Support language(s)
        :param lang: Use luguage
        :param path: Path where translation in. If provide a Path class,use it; else, use relative paths to the working directory. (Default: 'translation')
        :param file_type: Translation file(s) type. (Default: 'yml')
        :param default_text: The default return text if fail to get translation. (Default: 'Undefined')
        """

        self.langs = langs
        self.default_text = default_text

        self.data = Read(langs, path, file_type).data
        self.tran_data = self.data.get(self.lang, {})

        self.lang = lang

    def get(self, key: str, use_default_text: bool = False) -> str:
        """
        get str from translation

        :param key: the key name in translation
        :param use_default_text: If True,when the key not in translation,return the defalut text, else return the key.
        """

        if not self.lang:
            raise ValueError("Please set a value for I18.lang.")

        _tran = self.tran_data.get(key, Flags.NoValue)
        if _tran == Flags.NoValue:
            return self.default_text if use_default_text else key
        else:
            return _tran

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, value: str) -> None:
        """The current used language"""
        if not value:
            return

        if value in self.langs:
            self._lang = value
            self.tran_data = self.data.get(value, {})
            if not self.tran_data:
                print(f"Warning: {value} translation is empty.")
        else:
            raise ValueError(
                f"{value} is not in support language list. (Supported: {self.langs})"
            )

    @property
    def data(self) -> dict:
        """The all translation data.It is like {"zh_CN": {"text1": "Some Text"}, "en_US": {"text1": "Some Text"}}"""
        return self._data

    @data.setter
    def data(self, value: dict[str, dict]) -> None:
        self._data = value

    @property
    def tran_data(self) -> dict:
        return self._tran_data

    @tran_data.setter
    def tran_data(self, value: dict[str, dict]) -> None:
        """The current translation data.It is like {"text1": "Some Texts"}"""
        self._tran_data = value

    @data.setter
    def data(self, value: dict[str, dict]) -> None:
        """The all translation data.It is like {"zh_CN": {"text1": "Some Text"}, "en_US": {"text1": "Some Text"}}"""
        self._data = value

    @property
    def default_text(self) -> str:
        """The default return text if fail to get translation"""
        return self._default_text

    @default_text.setter
    def default_text(self, value: str) -> None:
        self._default_text = value

    @property
    def default_lang_data(self) -> dict[str, str]:
        return self._default_lang_data

    @default_lang_data.setter
    def default_lang_data(self, value: dict) -> None:
        self._default_lang_data = value
