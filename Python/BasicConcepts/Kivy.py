import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SimpleKivy(App):
    def build(self):
        return Label(text="Hello Manas!!!")

    def on_enter(instance, value):
        print('User Press enter in', instance)

    textinput = TextInput(text='Hello world', multiline=False)
    textinput.bind(on_text_validate=on_enter)


if __name__ == "__main__":
    SimpleKivy().run()
