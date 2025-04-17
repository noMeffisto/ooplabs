from abc import ABC, abstractmethod

class DocumentObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class User(DocumentObserver):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def update(self, message: str):
        print(f"Уведомление для {self.name} ({self.role}): {message}")