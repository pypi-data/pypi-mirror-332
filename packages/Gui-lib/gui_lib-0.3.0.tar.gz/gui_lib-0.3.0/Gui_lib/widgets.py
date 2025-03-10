# my_gui_lib/widgets.py
class Button:
    def __init__(self, text, command=None):
        self.text = text
        self.command = command

    def click(self):
        if self.command:
            self.command()
        
    def __repr__(self):
        return f"Button({self.text})"


class Label:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Label({self.text})"
