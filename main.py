import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
import kivy.graphics

from math import cos, sin, pi



class DataWindow(GridLayout):
    pass

class OpensecuApp(App):
    def build(self):
        return DataWindow()


if __name__ == '__main__':
    app = OpensecuApp()
    app.run()