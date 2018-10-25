"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

def test_touching_censor():
    robot = rb.Snatch3rRobot()
    print('hello')
    robot.touch_sensor.wait_until_pressed()
    print('pressed')


main()
