import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import (StringProperty, ObjectProperty,NumericProperty)
from kivy.animation import *
import kivy.graphics
from kivy.clock import Clock


from math import cos, sin, pi
from functools import partial
import datetime
import time


from devconnect import *


import random




def rpm_conversion(rpm):
    return (rpm * (180.5/8000) -135.5)

def cnnct():
    try:
        serialPort = connect('COM3')
        read_thread=threading.Thread(target=read_port, args=(serialPort,))
        read_thread.start()
    except:
        print("Make sure ECU is plugged in")
        return


def stp():
    OpensecuApp().stop()
    # serial.Serial('COM3').close()

####################################################
#---------------------- GUI -----------------------#


class OpensecuReadings(Label):
    pass

class OpensecuVE(Label):
    pass


class OpensecuGauge(AnchorLayout):
    gauge_level = NumericProperty(-135)


    def gauge_anim(self,dt):
        anim = Animation(gauge_level = rpm_conversion(float(readings[0])), d=0.5 )
        anim.start(self)


class OpensecuNeedle(Image):
    needle_level = NumericProperty(-135)

    def needle_anim(self,dt):
        # print(level)
        anim = Animation(needle_level = rpm_conversion(float(readings[0])) , d=0.5)
        anim.start(self)


class OpensecuWindow(GridLayout):


    gauge = ObjectProperty(None)
    needle = ObjectProperty(None)
    ve = ObjectProperty(None)

    aa = ObjectProperty(None)

    imp = StringProperty("0")
    amass =StringProperty("0")
    fmass = StringProperty("0")
    freq = StringProperty("0")

    save_flag = NumericProperty(0)


    def start(self):
        Clock.schedule_interval(self.gauge.gauge_anim, 0.5)
        Clock.schedule_interval(self.needle.needle_anim, 0.5)
        Clock.schedule_interval(self.rpm_update, 0.5)
        Clock.schedule_interval(self.set_readings, 0.5)


    def rpm_update(self,dt):
        anim = Animation(rpm = float(readings[0]), d=0.5)
        anim.start(self)

    def set_readings(self,dt):
        self.imp = str(readings[1])
        self.amass = str(readings[3])
        self.fmass = str(readings[4])
        self.freq = str(readings[5])
        if(self.save_flag):
            f = open('data/readings.txt', 'a')
            f.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ",")
            f.write(str(readings[1]) + "," + str(readings[3]) + "," + str(readings[4]) + "," + str(readings[5])+"\n")
            print("Data saved")
            f.close()




    def on_enter(self, value):
        print(value[5:] )
        self.display.text = "ecu> "
        # rand = random.randint(0,8000)
        # print(self.gauge.level)
        if(value[5:] == "r"):
            self.aa.color= 0,0.93,1,0.5
        elif(value[5:]=="connect"):
            cnnct()
            self.start()
        elif(value[5:]=="exit"):
            stp()
        elif(value[5:]=="save"):
            self.display.text += "\nFile succesfully opened, saving readigns"
            self.save_flag = 1
        elif(value[5:]=="save stop"):
            self.display.text += "\nData capturing stopped"
            self.save_flag = 0
        elif(value[5:]=="help"):
            self.display.text += "\nPress enter to clear the console"
            self.display.text += "\nAvailable commands: help, connect, save, exit,"
        else:
            pass


    #Keeps user from deleting name in console
    def bashlook(self,value, crs):
        if(value[:5] != 'ecu> '):
            self.display.text = "ecu> "



class OpensecuApp(App):
    def build(self):
        # clock = OpensecuWindow()
        # Clock.schedule_interval(clock.gauge.rpmupdate, 2)
        connection = OpensecuWindow()
        connection.start()
        return OpensecuWindow()


if __name__ == '__main__':
    OpensecuApp().run()
    exit_app()
    exit()
