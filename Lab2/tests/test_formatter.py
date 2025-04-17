from src.formatter import PlainTextFormatter, BoldFormatter, ItalicFormatter

def test_formatter():
    formatter = BoldFormatter(ItalicFormatter(PlainTextFormatter()))
    result = formatter.format("Тест")
    assert result == "***Тест***"