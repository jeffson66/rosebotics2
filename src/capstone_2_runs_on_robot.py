"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and PUT_YOUR_NAME_HERE.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
   robot = rb.Snatch3rRobot()
   rc = RemoteControlEtc(robot)
   dude2 = com.MqttClient(rc)
   dude2.connect_to_pc()

   while True:
       if robot.beacon_button_sensor.is_bottom_red_button_pressed():
           ev3.Sound.beep().wait()
       if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
           ev3.Sound.speak('Project Successfully done').wait()
       time.sleep(0.01)

class RemoteControlEtc(object):
    def __init__(self, robot):
        """

        Stores the robot.
         :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        pass
    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    def go_forward(self, speed_string):
        print("dudo moving!!!!!")
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)
        time.sleep(5)
        self.robot.drive_system.stop_moving()
    def go_straight(self,speed_string):
        print('dudo moving!!!')
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)
        time.sleep(0.01)
        self.robot.drive_system.stop_moving()
        if self.robot.color_sensor == 6:
            ev3.Sound.speak('got you!').wait()
    def go_back(self,speed_string):
        print('dudo moving!!!')
        speed = int(speed_string)
        self.robot.drive_system.start_moving(-speed,-speed)
        time.sleep(0.01)
        self.robot.drive_system.stop_moving()
    def turn_left(self,degree_string):
        print('dudo turning!!!')
        degree = int(degree_string)
        self.robot.drive_system.turn_degrees(degree)
    def turn_right(self,degree_string):
        print('dudo turning!!!')
        degree = int(degree_string)
        self.robot.drive_system.turn_degrees(-degree)


     # For the delegate to do its work


main()