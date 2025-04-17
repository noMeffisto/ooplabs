import pytest
from src.manager import DocumentManager
from src.storage import LocalFileStorage
from src.observer import User

def test_create_and_edit_document():
    # Создаем менеджер
    manager = DocumentManager()

    # Создаем документ
    manager.create_document("plaintext", "doc1")

    # Проверяем, что документ создан
    assert "doc1" in manager.documents

    # Редактируем документ
    manager.edit_document("doc1", "Тестовый текст")

    # Проверяем, что текст изменился
    assert manager.documents["doc1"].get_content() == "Тестовый текст"

def test_undo_redo():
    # Создаем менеджер
    manager = DocumentManager()

    # Создаем и редактируем документ
    manager.create_document("plaintext", "doc1")
    manager.edit_document("doc1", "Текст 1")
    manager.edit_document("doc1", "Текст 2")

    # Отменяем последнее изменение (undo)
    manager.undo()

    # Проверяем, что текст вернулся к предыдущему состоянию
    assert manager.documents["doc1"].get_content() == "Текст 1"

    # Повторяем отмененное действие (redo)
    manager.redo()

    # Проверяем, что текст вернулся к последнему состоянию
    assert manager.documents["doc1"].get_content() == "Текст 2"

def test_observer_notification():
    # Создаем менеджер и наблюдателя
    manager = DocumentManager()
    user = User("Тестовый пользователь", "Editor")
    manager.add_observer(user)

    # Создаем документ (должно вызвать уведомление)
    with pytest.capture_output() as captured:
        manager.create_document("plaintext", "doc1")
        assert "Уведомление для Тестовый пользователь (Editor): Документ doc1 создан" in captured.stdout