import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.properties import *
from kivy.animation import Animation
import kivy.graphics

from math import cos, sin, pi
from functools import partial


class DataWindow(GridLayout):

    def gaugeChange(self, rpm):
        if rpm:
            try:
                self.gauge
            except Exception:
                self.cmd.text: "Error"

    def on_enter(self, value):
        print(value[5:] )
        self.display.text = "ecu> "
        if float(value[5:]) > 45:
            #self.level = 22.5
            anim = Animation(level = 45)
        elif float(value[5:]) < -135:
            #self.level = -135
            anim = Animation(level = -135)
        else:
            # self.level = value[5:]
            anim = Animation(level = float(value[5:]))

        anim.start(self)

    #Keeps user from deleting name in console
    def bashlook(self,value, crs):
        if(value[:5] != 'ecu> '):
            self.display.text = "ecu> "



class OpensecuApp(App):
    def build(self):
        return DataWindow()


if __name__ == '__main__':
    OpensecuApp().run()