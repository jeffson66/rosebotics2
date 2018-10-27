"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_touch_censor()
    test_color_censor()
def test_touch_censor():
    robot = rb.Snatch3rRobot()
    print('hello')

    robot.touch_sensor.wait_until_pressed()
    print('pressed')
    robot.touch_sensor.wait_until_released()
    print('released')

def test_color_censor():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(100,100)
    robot.color_sensor.wait_until_color_is(2)
    print('blue')


main()
