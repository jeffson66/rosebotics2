"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def reset1(n):
    n = 10
    return n





# black line
def black_line():
    robot = rb.Snatch3rRobot()

    angle = 10

    for j in range(30):
        angle = reset1(angle)

        robot.drive_system.start_moving(100, 100)
        robot.color_sensor.wait_until_color_is(6)

        while True:

            if robot.color_sensor.get_color() == 1:
                break



            robot.drive_system.turn_degrees(100, 0, angle)

            angle = angle + 5




black_line()