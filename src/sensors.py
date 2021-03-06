"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""
import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    # test_touch_sensor()
    # test_color_sensor()
    #test_proximity_sensor()
    camera()
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
    while True:
        if 9 < robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 15:
            print('hello111')
            ev3.Sound.beep().wait()
        break
def camera():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.camera.get_biggest_blob().get_area() > 600:
            ev3.Sound.beep().wait()
        else:
            pass
main()
