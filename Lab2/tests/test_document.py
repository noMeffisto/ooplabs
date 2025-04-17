import pytest
from src.document import DocumentFactory, PlainTextDocument

def test_document_creation():
    doc = DocumentFactory.create_document("plaintext")
    assert isinstance(doc, PlainTextDocument)
    doc.set_content("Тест")
    assert doc.get_content() == "Тест"

def test_invalid_document_type():
    with pytest.raises(ValueError):
        DocumentFactory.create_document("invalid")