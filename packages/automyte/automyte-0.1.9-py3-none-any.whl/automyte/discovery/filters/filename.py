import re

from .base import File, Filter


class FilenameFilter(Filter):
    def __init__(self, contains: str | list[str]) -> None:
        self.text = contains if isinstance(contains, list) else [contains]

    def filter(self, file: File) -> bool:
        return any(re.search(pattern, file.name) for pattern in self.text)
