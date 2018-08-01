#!/usr/bin/env python
import rospy
import time
import string
from mechanism.msg import coordinates
from mechanism.msg import affordance
import thread
import roslib; roslib.load_manifest('robotiq_c_model_control')
from robotiq_c_model_control.msg import _CModel_robot_output  as outputMsg
# from robotiq_force_torque_sensor.msg import ft_sensor

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

# # Data Collection
# def data_record(rosMsg1):   #for pose_euler
#     with open('ft_data.csv','a') as fid_euler:
# 	fid_euler.write('%.6f, %.6f, %.6f, %.6f, %.6f, %.6f\n' %(rosMsg1.Fx,rosMsg1.Fy,rosMsg1.Fz,rosMsg1.Mx,rosMsg1.My,rosMsg1.Mz))

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
            cd.base = 0.74
            cd.shoulder = -1.576
            cd.elbow = 1.4217
            cd.w1 = -1.41424
            cd.w2 = -1.56782
            cd.w3 = 0
            # rospy.loginfo(cd)
            pub.publish(cd)
            time.sleep(2)
            # Wait for user input to start action
            input_command2 = raw_input("Start? If yes, press y: ")
            i_start = 'y'
            if input_command2 == i_start:
                # Start data Collection
                # data_record()
                # Set flag
                # Read JA
                cd.flag = 1
                # Hardcoding the initial joint coordinates
                # Going to the initial position
                cd.base = 0.74
                cd.shoulder = -1.56
                cd.elbow = 1.81
                cd.w1 = -1.82
                cd.w2 = -1.57
                cd.w3 = 0
                pub.publish(cd)
                time.sleep(2)
        # Need to add data collection
def callback(msg):
    global aff_flag
    aff_flag = msg.affordance

if __name__ == '__main__':
    try:
        # Coordinate Movement Nodes
        rospy.init_node('coordinate_gen',anonymous=True)
        pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
        # Gripper Node
        grip = rospy.Publisher('CModelRobotOutput', outputMsg.CModel_robot_output,queue_size=100)
        # # Data Node
        # rospy.init_node('Data_record', anonymous='True')
        # rospy.Subscriber('robotiq_force_torque_sensor', ft_sensor, data_record)
        # Affordance Node
        aff_sub = rospy.Subscriber('/affordance',affordance,callback)
        rate = rospy.Rate(10)
        rate = rospy.Rate(10)
        cd = coordinates()
        command = outputMsg.CModel_robot_output();
        thread.start_new_thread(robot_search(),())
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
