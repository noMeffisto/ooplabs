from abc import ABC, abstractmethod

class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass

class PlainTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text

class BoldFormatter(TextFormatter):
    def __init__(self, wrapped: TextFormatter):
        self.wrapped = wrapped

    def format(self, text: str) -> str:
        return f"**{self.wrapped.format(text)}**"

class ItalicFormatter(TextFormatter):
    def __init__(self, wrapped: TextFormatter):
        self.wrapped = wrapped

    def format(self, text: str) -> str:
        return f"*{self.wrapped.format(text)}*"

class UnderlineFormatter(TextFormatter):
    def __init__(self, wrapped: TextFormatter):
        self.wrapped = wrapped

    def format(self, text: str) -> str:
        return f"_{self.wrapped.format(text)}_"