import kivy
from kivy.app import App
from kivy.uix.label import Label


class SimpleKivy(App):
    def build(self):
        return Label(text="Hello Manas!!!")
        return Label(text="Hello Manasa!!!")


if __name__ == "__main__":
    SimpleKivy().run()
