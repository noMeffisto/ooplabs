class EditorSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "light"
            cls._instance.font_size = 12
        return cls._instance

    def set_theme(self, theme: str):
        self.theme = theme
        print(f"Тема изменена на {theme}")

    def set_font_size(self, size: int):
        if size > 0:
            self.font_size = size
            print(f"Размер шрифта изменен на {size}")
        else:
            print("Ошибка: размер шрифта должен быть положительным")