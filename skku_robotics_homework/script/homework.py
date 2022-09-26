#!/usr/bin/python3
import rospy
from controller import Controller
import numpy as np
""" Import required modules """


"""-------------------------"""

""" Write the function you need """



"""-----------------------------"""

def inversKinemaics(x,y,z,roll,pitch,yaw):
    d1,d2,d3,d4,d5,d6 = 0.0,0.0,0.0,0.0,0.0,0.0
    """ Write the inversKinemaics function """














    """------------------------------------"""
    return [d1,d2,d3,d4,d5,d6]

if __name__ == '__main__':
    rospy.init_node('controller')
    controller = Controller()

    position = rospy.get_param("~position")
    position = position.split(",")

    x = float(position[0])
    y = float(position[1])
    z = float(position[2])
    roll = float(position[3])
    pitch = float(position[4])
    yaw = float(position[5])

    rospy.loginfo("[skku_robotics_homework] set position x:{} y:{} z:{} roll:{} pitch:{} yaw:{}".format(x,y,z,roll,pitch,yaw))
    goal = inversKinemaics(x,y,z,roll,pitch,yaw)
    controller.control(goal)
