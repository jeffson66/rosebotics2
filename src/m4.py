"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time



""" polygon """

def draw_polygon(n):
    robot = rb.Snatch3rRobot()
    theta = 180-((180 * (n - 2))/n)
    for k in range(n):
        robot.drive_system.go_straight_inches(25)
        if k == n-1:
            break
        robot.drive_system.turn_degrees(100, 0, theta)
    robot.drive_system.stop_moving()


draw_polygon(3)