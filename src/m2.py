"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def stop_when_sees_color(color):
    """ sees color """
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(100, 100)
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()


stop_when_sees_color(5)
