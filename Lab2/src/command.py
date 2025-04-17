from abc import ABC, abstractmethod
from src.document import Document

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class EditCommand(Command):
    def __init__(self, document: Document, new_content: str):
        self.document = document
        self.new_content = new_content
        self.old_content = document.get_content()

    def execute(self):
        self.document.set_content(self.new_content)

    def undo(self):
        self.document.set_content(self.old_content)