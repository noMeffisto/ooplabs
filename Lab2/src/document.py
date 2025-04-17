from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

    @abstractmethod
    def set_content(self, content: str):
        pass

class PlainTextDocument(Document):
    def __init__(self):
        self.content = ""

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str):
        self.content = content

class MarkdownDocument(Document):
    def __init__(self):
        self.content = ""

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str):
        self.content = content

class RichTextDocument(Document):
    def __init__(self):
        self.content = ""

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str):
        self.content = content

class DocumentFactory:
    @staticmethod
    def create_document(doc_type: str) -> Document:
        doc_type = doc_type.lower()
        if doc_type == "plaintext":
            return PlainTextDocument()
        elif doc_type == "markdown":
            return MarkdownDocument()
        elif doc_type == "richtext":
            return RichTextDocument()
        else:
            raise ValueError(f"Неизвестный тип документа: {doc_type}")