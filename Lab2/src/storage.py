from abc import ABC, abstractmethod
from src.document import Document
import json
import xml.etree.ElementTree as ET

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, document: Document, filename: str):
        pass

    @abstractmethod
    def load(self, filename: str) -> str:
        pass

class LocalFileStorage(StorageStrategy):
    def save(self, document: Document, filename: str):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(document.get_content())
            print(f"Сохранено в {filename}")
        except IOError:
            print(f"Ошибка при сохранении файла {filename}")

    def load(self, filename: str) -> str:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")

class JSONStorage(StorageStrategy):
    def save(self, document: Document, filename: str):
        try:
            data = {"content": document.get_content()}
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
            print(f"Сохранено в {filename} как JSON")
        except IOError:
            print(f"Ошибка при сохранении файла {filename}")

    def load(self, filename: str) -> str:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data["content"]
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")

class XMLStorage(StorageStrategy):
    def save(self, document: Document, filename: str):
        try:
            root = ET.Element("document")
            content = ET.SubElement(root, "content")
            content.text = document.get_content()
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='unicode')
            print(f"Сохранено в {filename} как XML")
        except IOError:
            print(f"Ошибка при сохранении файла {filename}")

    def load(self, filename: str) -> str:
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            return root.find("content").text or ""
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")