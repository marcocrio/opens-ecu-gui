from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.graphics import *


class DataWindow(Widget):
    pass

class OpensecuApp(App):
    def build(self):
        return DataWindow()


if __name__ == '__main__':
    OpensecuApp().run()