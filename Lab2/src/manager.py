from typing import Dict, List
from src.document import Document, DocumentFactory
from src.command import Command, EditCommand
from src.observer import DocumentObserver
from src.storage import StorageStrategy

class DocumentManager:
    def __init__(self):
        self.documents: Dict[str, Document] = {}
        self.undo_stack: List[Command] = []
        self.redo_stack: List[Command] = []
        self.observers: List[DocumentObserver] = []
        self.storage_strategy: StorageStrategy = None

    def create_document(self, doc_type: str, name: str):
        try:
            doc = DocumentFactory.create_document(doc_type)
            self.documents[name] = doc
            self.notify_observers(f"Документ {name} создан")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def edit_document(self, name: str, content: str):
        if name in self.documents:
            command = EditCommand(self.documents[name], content)
            command.execute()
            self.undo_stack.append(command)
            self.redo_stack.clear()
            self.notify_observers(f"Документ {name} отредактирован")
        else:
            print(f"Документ {name} не найден")

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
            self.notify_observers("Выполнена отмена")
        else:
            print("Нечего отменять")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
            self.notify_observers("Выполнен повтор")
        else:
            print("Нечего повторять")

    def save_document(self, name: str, filename: str):
        if name in self.documents and self.storage_strategy:
            try:
                self.storage_strategy.save(self.documents[name], filename)
            except Exception as e:
                print(f"Ошибка сохранения: {e}")
        else:
            print("Документ не найден или не выбран способ хранения")

    def load_document(self, name: str, filename: str):
        if self.storage_strategy:
            try:
                content = self.storage_strategy.load(filename)
                self.documents[name] = DocumentFactory.create_document("plaintext")
                self.documents[name].set_content(content)
                self.notify_observers(f"Документ {name} загружен")
            except Exception as e:
                print(f"Ошибка загрузки: {e}")
        else:
            print("Не выбран способ хранения")

    def set_storage_strategy(self, strategy: StorageStrategy):
        self.storage_strategy = strategy
        print("Способ хранения изменен")

    def add_observer(self, observer: DocumentObserver):
        self.observers.append(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)