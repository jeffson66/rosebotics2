"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and PUT_YOUR_NAME_HERE.
"""


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    dude2 = com.MqttClient()
    dude2.connect_to_ev3()
    setup_gui(root,dude2)

    root.mainloop()



def setup_gui(root_window,mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    degree_entry_box = ttk.Entry(frame)
    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    degree_entry_box.grid()
    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt_client)

    frame = ttk.Frame(root_window, padding=30)
    frame.grid()


    go_straight_button = ttk.Button(frame, text="Go straight")
    go_straight_button['command']=lambda : go_straight(speed_entry_box, mqtt_client)
    go_back_button = ttk.Button(frame, text="Go back")
    go_back_button['command']=lambda :go_back(speed_entry_box, mqtt_client)
    turn_left_button = ttk.Button(frame, text="Turn left")
    turn_left_button['command']=lambda :turn_left(degree_entry_box,mqtt_client)
    turn_right_button = ttk.Button(frame, text="Turn right")
    turn_right_button['command'] = lambda: turn_right(degree_entry_box, mqtt_client)


    go_straight_button.grid(row = 0, column = 1)
    go_back_button.grid(row = 2, column = 1)
    turn_left_button.grid( row = 1, column =0)
    turn_right_button.grid(row = 1, column =2,padx = 5, pady =5)




def go_straight(entry_box,mqtt_client):
    speed_string = entry_box.get()
    print("Sending the go_straight message")
    mqtt_client.send_message('go_straight',[speed_string])

def go_back(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print("Sending the go_back message", speed_string)
    mqtt_client.send_message('go_back',[speed_string])

def turn_left(entry_box, mqtt_client):
    degree_string = entry_box.get()
    print("Sending the turn_left message", degree_string)
    mqtt_client.send_message('turn_left', [degree_string])
def turn_right(entry_box, mqtt_client):
    degree_string = entry_box.get()
    print("Sending the turn_right message",degree_string)
    mqtt_client.send_message('turn_right', [degree_string])
def handle_go_forward(entry_box,mqtt_client):
    speed_string = entry_box.get()
    print("Sending the go_forward message with speed", speed_string)
    mqtt_client.send_message('go_forward', [speed_string])
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """



main()
