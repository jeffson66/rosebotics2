"""
  Capstone Project.  Code written by Ao Liu.
  Fall term, 2018-2019.
"""

import rosebotics as rb


# polygon


def draw_polygon(n):
    robot = rb.Snatch3rRobot()
    if n < 3:
        print('A polygon has at least 3 sides.')
    theta = 180-((180 * (n - 2))/n)
    for k in range(n):
        robot.drive_system.go_straight_inches(5)
        if k == n-1:
            break
        robot.drive_system.turn_degrees(theta)
    robot.drive_system.stop_moving()


# follow black line


def follow_black_line():
    robot = rb.Snatch3rRobot()
    theta = 10
    while True:
        robot.drive_system.start_moving()

        if robot.color_sensor.get_color() != 1:
            while True:
                robot.drive_system.turn_degrees(theta)
                if robot.color_sensor.get_color() == 1:
                    break
        robot.drive_system.start_moving()

        if robot.touch_sensor.get_value() == 1:
            robot.drive_system.stop_moving()
            break

# stop when see certain color


def stop_when_see(color):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()

follow_black_line()