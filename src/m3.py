"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""
import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # test_touch_sensor()
    # test_color_sensor()
    test_proximity_sensor()
def test_touch_sensor():
    robot = rb.Snatch3rRobot()
    print('hello')

    robot.touch_sensor.wait_until_pressed()
    print('pressed')
    robot.touch_sensor.wait_until_released()
    print('released')

def test_color_sensor():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(100,100)
    robot.color_sensor.wait_until_color_is(2)
    print('blue')

def test_proximity_sensor():
    robot = rb.Snatch3rRobot()
    ev3 = rb.ev3
    distance = robot.proximity_sensor.get_distance_to_nearest_object()
    inch = robot.proximity_sensor.get_distance_to_nearest_object_in_inches(distance)
    while True:
        if 0 < inch < 100:
            ev3.Sound.beep()

        break





main()
