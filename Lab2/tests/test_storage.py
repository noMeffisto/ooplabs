import os
import pytest
from src.document import DocumentFactory
from src.storage import LocalFileStorage, JSONStorage

def test_local_file_storage_save_and_load():
    # Создаем документ
    doc = DocumentFactory.create_document("plaintext")
    doc.set_content("Тестовый текст")

    # Сохраняем документ в файл
    storage = LocalFileStorage()
    filename = "test_output.txt"
    storage.save(doc, filename)

    # Проверяем, что файл создан
    assert os.path.exists(filename)

    # Загружаем содержимое из файла
    loaded_content = storage.load(filename)
    assert loaded_content == "Тестовый текст"

    # Удаляем тестовый файл
    os.remove(filename)

def test_json_storage_save_and_load():
    # Создаем документ
    doc = DocumentFactory.create_document("plaintext")
    doc.set_content("Тестовый JSON текст")

    # Сохраняем документ в JSON
    storage = JSONStorage()
    filename = "test_output.json"
    storage.save(doc, filename)

    # Проверяем, что файл создан
    assert os.path.exists(filename)

    # Загружаем содержимое из файла
    loaded_content = storage.load(filename)
    assert loaded_content == "Тестовый JSON текст"

    # Удаляем тестовый файл
    os.remove(filename)

def test_local_file_storage_load_nonexistent_file():
    # Проверяем, что загрузка несуществующего файла вызывает ошибку
    storage = LocalFileStorage()
    with pytest.raises(FileNotFoundError):
        storage.load("nonexistent.txt")