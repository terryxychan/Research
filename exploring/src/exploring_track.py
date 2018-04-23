#!/usr/bin/env python
import rospy
import time
import string
from exploring.msg import coordinates

def coordinate_gen():
    rospy.init_node('coordinate_gen',anonymous=True)
    pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
    rate = rospy.Rate(10)
    cd = coordinates()
    while not rospy.is_shutdown():
        input_command = raw_input("If you want to go to initial position, press i:")
        i_test = 'i'
        if input_command == i_test:
            # Setting flag
            cd.flag = 1
            # Hardcoding the initial joint coordinates
            cd.base = -2.57
            cd.shoulder = -1.67
            cd.elbow = -2.31
            cd.w1 = -2.34
            cd.w2 = -2.53
            cd.w3 = -3.21
            rospy.loginfo(cd)
            pub.publish(cd)
            time.sleep(10)
            rate.sleep()
        else:
            # Setting flag
            cd.flag = 0
            count = 0
            i = 1
            while (count < 1):
                time.sleep(0.5)
            # Assume the robot is at the initial position already
            # -0.325, " + str(y) + " ,0.116, 0.0165, 2.29, -2.23
                cd.X = -0.325
                cd.Y = -0.345
                cd.Z = 0.116
                cd.Rx = 0.0065
                cd.Ry = 2.29
                cd.Rz = -2.23
                print "Starting to search"
                while (i < 5):
                    cd.Y = -0.345 - i * 0.05
                # print cd.Y
                    rospy.loginfo(cd)
                    pub.publish(cd)
                    time.sleep(10)
                    i = i + 1
                    count = count + 1
                    rate.sleep()
if __name__ == '__main__':
    try:
        coordinate_gen()
    except rospy.ROSInterruptException:
        pass
