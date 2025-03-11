"""
MIT License
Copyright (c) 2025 weinibuliu
"""

import json
import yaml
from pathlib import Path
from typing import Any, Dict, List, Literal, Union

FILE_TYPE = ["yaml", "yml", "json"]


class Read:
    def __init__(
        self,
        langs: Union[List[str], str],
        path: Union[Path, str, None],
        file_type: Literal["json", "yaml", "yml"],
    ) -> None:

        if not langs:
            raise ValueError(f"`langs` cannot be empty.(Current: {langs})")
        elif type(langs) == list:
            self._langs = langs
        elif type(langs) == str:
            self._langs = [langs]
        else:
            raise TypeError(f"langs")

        if path is None:
            self._path = Path.cwd()
        elif type(path) == str:
            self._path = Path.cwd() / path
        elif type(path) == Path:
            self._path = path
        else:
            raise TypeError(f"'path' is not a Path,str or None.(Current: {path})")

        if file_type in FILE_TYPE:
            self._file_type = file_type
        else:
            raise ValueError(f"{file_type} is not in {FILE_TYPE}")

        self._get_translation_paths()
        self.load_translations()

    def _load_file(self, f) -> Union[Dict, Any]:
        if self._file_type in ["yaml", "yml"]:
            return yaml.load(f, Loader=yaml.BaseLoader) or {}
        elif self._file_type == "json":
            return json.load(f) or {}

    def _get_translation_paths(self) -> None:
        if not self._path.exists():
            raise FileNotFoundError(f"{self._path} does not exist.")

        self.files = []  # translation files list
        for lang in self._langs:
            _path = self._path / f"{lang}.{self._file_type}"
            if _path.exists():
                self.files.append(_path)
            else:
                raise FileNotFoundError(f"{_path} dose not exist.")

        if self.files is None:
            raise RuntimeError("Couldn't find any translation file.")

    def load_translations(self) -> None:
        self._data = {}
        for lang, file in zip(self._langs, self.files):
            with open(file, "r", encoding="utf-8") as f:
                self._data[lang] = self._load_file(f)

    @property
    def data(self):
        """(Read-Only) The all translation data.It is like {"zh_CN": {"text1": "Some Text"}, "en_US": {"text1": "Some Text"}}"""
        return self._data
