import cmd
from src.manager import DocumentManager
from src.settings import EditorSettings
from src.observer import User
from src.storage import LocalFileStorage, JSONStorage, XMLStorage
from src.formatter import PlainTextFormatter, BoldFormatter, ItalicFormatter, UnderlineFormatter

class EditorCLI(cmd.Cmd):
    prompt = "(Редактор) "
    intro = "Консольный текстовый редактор. Введите 'help' для списка команд."

    def __init__(self):
        super().__init__()
        self.manager = DocumentManager()
        self.settings = EditorSettings()
        self.manager.add_observer(User("Админ", "Admin"))

    def do_create(self, arg):
        """create <type> <name>: Создать документ (plaintext, markdown, richtext)"""
        try:
            doc_type, name = arg.split()
            self.manager.create_document(doc_type, name)
        except ValueError:
            print("Использование: create <type> <name>")

    def do_edit(self, arg):
        """edit <name> <content>: Редактировать документ"""
        try:
            name, content = arg.split(maxsplit=1)
            self.manager.edit_document(name, content)
        except ValueError:
            print("Использование: edit <name> <content>")

    def do_format(self, arg):
        """format <name> <style> <text>: Форматировать текст (bold, italic, underline)"""
        try:
            name, style, text = arg.split(maxsplit=2)
            formatter = PlainTextFormatter()
            if style.lower() == "bold":
                formatter = BoldFormatter(formatter)
            elif style.lower() == "italic":
                formatter = ItalicFormatter(formatter)
            elif style.lower() == "underline":
                formatter = UnderlineFormatter(formatter)
            else:
                print("Неизвестный стиль форматирования")
                return
            formatted_text = formatter.format(text)
            self.manager.edit_document(name, formatted_text)
        except ValueError:
            print("Использование: format <name> <style> <text>")

    def do_save(self, arg):
        """save <name> <filename> <type>: Сохранить документ (txt, json, xml)"""
        try:
            name, filename, storage_type = arg.split()
            storage_type = storage_type.lower()
            if storage_type == "txt":
                self.manager.set_storage_strategy(LocalFileStorage())
            elif storage_type == "json":
                self.manager.set_storage_strategy(JSONStorage())
            elif storage_type == "xml":
                self.manager.set_storage_strategy(XMLStorage())
            else:
                print("Неизвестный тип хранения")
                return
            self.manager.save_document(name, filename)
        except ValueError:
            print("Использование: save <name> <filename> <type>")

    def do_load(self, arg):
        """load <name> <filename> <type>: Загрузить документ (txt, json, xml)"""
        try:
            name, filename, storage_type = arg.split()
            storage_type = storage_type.lower()
            if storage_type == "txt":
                self.manager.set_storage_strategy(LocalFileStorage())
            elif storage_type == "json":
                self.manager.set_storage_strategy(JSONStorage())
            elif storage_type == "xml":
                self.manager.set_storage_strategy(XMLStorage())
            else:
                print("Неизвестный тип хранения")
                return
            self.manager.load_document(name, filename)
        except ValueError:
            print("Использование: load <name> <filename> <type>")

    def do_undo(self, arg):
        """undo: Отменить последнее действие"""
        self.manager.undo()

    def do_redo(self, arg):
        """redo: Повторить отмененное действие"""
        self.manager.redo()

    def do_theme(self, arg):
        """theme <theme>: Установить тему"""
        if arg:
            self.settings.set_theme(arg)
        else:
            print("Использование: theme <theme>")

    def do_fontsize(self, arg):
        """fontsize <size>: Установить размер шрифта"""
        try:
            size = int(arg)
            self.settings.set_font_size(size)
        except ValueError:
            print("Использование: fontsize <size>")

    def do_view(self, arg):
        """view <name>: Просмотреть содержимое документа"""
        if arg in self.manager.documents:
            print(self.manager.documents[arg].get_content())
        else:
            print(f"Документ {arg} не найден")

    def do_exit(self, arg):
        """exit: Выйти из редактора"""
        print("Выход...")
        return True

if __name__ == "__main__":
    EditorCLI().cmdloop()