"""
  Capstone Project.  Code written by PUT_ YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_even_newer as rb


def raise_then_lower_arm():

    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw()
    robot.arm.lower_arm_and_open_claw()


def calibrate():
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate()


def move_arm(position):
    robot = rb.Snatch3rRobot()
    robot.arm.move_arm_to_position(position)


def lower():
    robot = rb.Snatch3rRobot()
    robot.arm.lower_arm_and_open_claw()

lower()