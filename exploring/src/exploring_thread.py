#!/usr/bin/env python
import rospy
import time
import string
from exploring.msg import coordinates
from exploring.msg import affordance
import thread
import roslib; roslib.load_manifest('robotiq_c_model_control')
from robotiq_c_model_control.msg import _CModel_robot_output  as outputMsg

aff_flag = 0;

# This activates the gripper
def gripper_activation(command):
    command = outputMsg.CModel_robot_output();
    command.rACT = 1
    command.rGTO = 1
    command.rSP  = 255
    command.rFR  = 150
    print("Gripper Activated")
    print(command)
    time.sleep(3)
    return command

#This opens the gripper
def gripper_open(command):
    command.rPR = 0
    print("Gripper Opened")
    return command

# This closes it
def gripper_close(command):
    command.rPR = 255
    print("Gripper Closed")
    return command

# This is the exploring and picking objects up
def robot_search():
    while not rospy.is_shutdown():
        command = outputMsg.CModel_robot_output();
        command = gripper_activation(command)
        print(command)
        grip.publish(command)
        command = gripper_close(command)
        grip.publish(command)
        input_command = raw_input("If you want to go to initial position, press i:")
        i_test = 'i'
        # If the user wanted the initial position
        if input_command == i_test:
            # Setting flag
            # Reading the joint coordinates
            cd.flag = 1
            # Hardcoding the initial joint coordinates
            # Going to the initial position
            cd.base = -2.57
            cd.shoulder = -1.67
            cd.elbow = -2.31
            cd.w1 = -2.34
            cd.w2 = -2.53
            cd.w3 = -3.21
            # rospy.loginfo(cd)
            pub.publish(cd)
            time.sleep(2)
        else:
            # Setting flag
            # Reading the TCP coordinate
            cd.flag = 0
            count = 0
            i = 1
            j = 0
            while (count < 1):
                time.sleep(0.5)
            # Assume the robot is at the initial position already
            # -0.325, -0.345 ,0.116, 0.0165, 2.29, -2.23
            # start from the initial position
                cd.X = -0.325
                cd.Y = -0.345
                cd.Z = 0.116
                cd.Rx = 0.0065
                cd.Ry = 2.29
                cd.Rz = -2.23
                # print "Starting to search"
                while (j<5):
                    # This is the x direction explore
                    cd.Y = -0.345
                    pub.publish(cd)
                    time.sleep(3)
                    cd.X =  -0.325 - 0.065 * j
                    pub.publish(cd)
                    time.sleep(3)
                    print "X+", j
                    i = 1
                    while (i < 5):
                        # This is the y direction explore
                        if aff_flag == 0:
                            # Explore in the Y direction
                            cd.Y = -0.345 - i * 0.01
                            print "Y++"
                            wait_time = 3 + i*0.2;
                            pub.publish(cd)
                            time.sleep(3)
                            i = i + 1
                            count = count + 1
                        else:
                            # Open close gripper
                            cd.flag = 0
                            # Back up a little bit
                            cd.Y = -0.345 - i * 0.01 + 0.02
                            pub.publish(cd)
                            time.sleep(3)
                            print "Open gripper"
                            command = gripper_open(command)
                            grip.publish(command)
                            # Open the gripper
                            cd.Y = -0.345 - i * 0.01
                            pub.publish(cd)
                            time.sleep(3)
                            # aff_flag = 0
                            # Trying to find the affordance again with gripper open
                            while aff_flag == 0:
                                cd.Y = cd.Y - 0.005
                                pub.publish(cd)
                                time.sleep(3)
                            # Close gripper
                            print "close gripper"
                            command = gripper_close(command)
                            grip.publish(command)
                            cd.Z = cd.Z + 0.05
                            pub.publish(cd)
                            time.sleep(3)
                            # Goes to another position and drop the object
                            cd.X = -0.325
                            cd.Y = -0.345
                            cd.Z = 0.116
                            cd.Rx = 0.0065
                            cd.Ry = 2.29
                            cd.Rz = -2.23
                            pub.publish(cd)
                            time.sleep(5)
                            command = gripper_open(command)
                            grip.publish(command)
                            i = 20
                            j = 10
                    j = j + 1

def callback(msg):
    global aff_flag
    aff_flag = msg.affordance

if __name__ == '__main__':
    try:
        rospy.init_node('coordinate_gen',anonymous=True)
        pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
        grip = rospy.Publisher('CModelRobotOutput', outputMsg.CModel_robot_output,queue_size=100)
        aff_sub = rospy.Subscriber('/affordance',affordance,callback)
        rate = rospy.Rate(10)
        rate = rospy.Rate(10)
        cd = coordinates()
        command = outputMsg.CModel_robot_output();
        thread.start_new_thread(robot_search(),())
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
