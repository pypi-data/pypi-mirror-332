# my_gui_lib/main.py
class Application:
    def __init__(self, title="My GUI App"):
        self.title = title
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)

    def run(self):
        print(f"Running application: {self.title}")
        for widget in self.widgets:
            print(f"Widget: {widget}")

        # Здесь можно добавить логику для отображения окна и обработки событий