#!/usr/bin/env python
import roslib; roslib.load_manifest('robotiq_c_model_control')
import rospy
from robotiq_c_model_control.msg import _CModel_robot_output  as outputMsg
import time

def gripper_activation(command):
    command = outputMsg.CModel_robot_output();
    command.rACT = 1
    command.rGTO = 1
    command.rSP  = 255
    command.rFR  = 150
    print("Gripper Activated")
    print(command)
    return command

def gripper_open(command):
    command.rPR = 0
    print("Gripper Opened")
    return command

def gripper_close(command):
    command.rPR = 255
    print("Gripper Closed")
    return command

def publisher():
    rospy.init_node('CModelSimpleController')
    pub = rospy.Publisher('CModelRobotOutput', outputMsg.CModel_robot_output,queue_size=100)
    command = outputMsg.CModel_robot_output();
    while not rospy.is_shutdown():
        command = gripper_activation(command)
        pub.publish(command)
        print(command)
        time.sleep(5)
        command = gripper_close(command)
        pub.publish(command)
        print(command)
        time.sleep(5)
        command = gripper_open(command)
        pub.publish(command)
        print(command)
        time.sleep(5)
        rospy.sleep(0.1)

if __name__ == '__main__':
    publisher()
