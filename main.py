import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.properties import *
from kivy.animation import Animation
import kivy.graphics
from kivy.clock import Clock


from math import cos, sin, pi
from functools import partial


from devconnect import *




def rpm_conversion(rpm):
    return (rpm * (180.5/8000) -135.5)



####################################################
#---------------------- GUI -----------------------#


class DataWindow(GridLayout):


    def rpmupdate(self,dt):
        print(self.level)

        if (float(readings[0]) > 7999):
            #self.level = 22.5
            anim = Animation(level = 45)
            self.rpm = 8000
        elif float(readings[0]) < 1:
            #self.level = -135
            anim = Animation(level = -135)
            self.rpm = 0
        else:
            anim = Animation(level = rpm_conversion(float(readings[0])) )
            self.rpm = readings[0]

        anim.start(self)

    def on_enter(self, value):
        print(value[5:] )
        self.display.text = "ecu> "

        if(value[5:] == "r"):
            anim = Animation(level = rpm_conversion(float(readings[0])) )
            self.rpm = readings[0]
        elif float(value[5:]) > 7999:
            #self.level = 22.5
            anim = Animation(level = 45)
            self.rpm = 8000
        elif float(value[5:]) < 1:
            #self.level = -135
            anim = Animation(level = -135)
            self.rpm = 0
        else:
            # self.level = value[5:]
            anim = Animation(level = rpm_conversion(float(value[5:])) )
            self.rpm = value[5:]

        anim.start(self)

    #Keeps user from deleting name in console
    def bashlook(self,value, crs):
        if(value[:5] != 'ecu> '):
            self.display.text = "ecu> "



class OpensecuApp(App):
    def build(self):
        clock = DataWindow()
        Clock.schedule_interval(clock.rpmupdate, 1)
        return DataWindow()


if __name__ == '__main__':
    serialPort = connect('COM3')
    n=threading.Thread(target=list_ports, args=(serialPort,))
    i=threading.Thread(target=get_input)
    n.start()
    i.start()
    OpensecuApp().run()
