"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""
import time
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as mrmc

name1 = 'me'
name2 = 'robot02'
mqtt_client = mrmc.MqttClient()
mqtt_client.connect(name1, name2)
time.sleep(1)


def run_infrared_beacon_buttons():
    gui = tkinter.Tk()
    gui.title = 'Robot Controller'
    gui.geometry('150x150')
    frame1 = ttk.Frame(gui, padding=10)
    frame1.grid()
    frame2 = ttk.Frame(gui, padding=30)
    frame2.grid()
    redb = ttk.Button(frame1, text='Red Pressed', command=lambda: red_up_on_click())
    redb.grid()
    blueb = ttk.Button(frame2, text='Blue Pressed', command=lambda: blue_up_on_click())
    blueb.grid()
    gui.mainloop()


def red_up_on_click():
    mqtt_client.send_message('move', [11])
    print('Red On Click')


def blue_up_on_click():
    mqtt_client.send_message('move', [-11])
    print('Blue On Click')

