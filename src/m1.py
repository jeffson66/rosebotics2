"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_touching_censor()
    test_color_censor()
def test_touching_censor():
    robot = rb.Snatch3rRobot()
    print('hello')
    robot.touch_sensor.wait_until_pressed()
    print('pressed')
    robot.touch_sensor.wait_until_released()
    print('released')

def test_color_censor():
    robot = rb.Snatch3rRobot()
    print('hello again color sensor')
    robot.color_sensor.wait_until_color_is('red')
    print('red')
    robot.color_sensor.wait_until_color_is('white')
    print('white')
    robot.color_sensor.wait_until_color_is('blue')
    print('blue')
    robot.color_sensor.wait_until_color_is('green')
    print('green')

main()
else:
robot.drive_system.turn_degrees(0, 100, 100)
for j in range(15):
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_color_is(6)
    robot.drive_system.stop_moving()

    while robot.color_sensor.get_color() != 1:
        robot.drive_system.turn_degrees(0, 100, theta)
        theta = theta + 3