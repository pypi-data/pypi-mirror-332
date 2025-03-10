from Gui_lib import Application, Button, Label

def on_button_click():
    print("Button clicked!")

app = Application("Simple GUI")
button = Button("Click Me", on_button_click)
label = Label("Hello, World!")

app.add_widget(button)
app.add_widget(label)
app.run()