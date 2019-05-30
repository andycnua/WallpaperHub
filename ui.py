import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.config import Config
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '720')
Config.write()

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class MyApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()