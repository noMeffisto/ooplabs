import pytest
from src.document import DocumentFactory
from src.command import EditCommand

def test_edit_command_execute():
    # Создаем документ
    doc = DocumentFactory.create_document("plaintext")
    doc.set_content("Начальный текст")

    # Создаем команду для редактирования
    command = EditCommand(doc, "Новый текст")
    command.execute()

    # Проверяем, что текст изменился
    assert doc.get_content() == "Новый текст"

def test_edit_command_undo():
    # Создаем документ
    doc = DocumentFactory.create_document("plaintext")
    doc.set_content("Начальный текст")

    # Создаем команду для редактирования
    command = EditCommand(doc, "Новый текст")
    command.execute()

    # Отменяем изменение
    command.undo()

    # Проверяем, что текст вернулся к исходному
    assert doc.get_content() == "Начальный текст"