#!/usr/bin/env python
import rospy
import time
import string
from mechanism.msg import coordinates
from mechanism.msg import affordance

def coordinate_gen():
    rospy.init_node('coordinate_gen',anonymous=True)
    pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
    aff_sub = rospy.Subscriber('/affordance',affordance,callback)
    rate = rospy.Rate(10)
    rate = rospy.Rate(10)
    cd = coordinates()
    # print "calling spin"
    rospy.spin()
    # print "Spinning"
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
                    print aff_flag
                    if aff_flag == 0:
                        cd.Y = -0.345 - i * 0.05
                        print "Still going"
                        rospy.loginfo(cd)
                        pub.publish(cd)
                        time.sleep(2)
                        i = i + 1
                        count = count + 1
                        rate.sleep()
                    else:
                        cd.flag = 1
                        cd.base = 0.00
                        cd.shoulder = 1.95
                        cd.elbow = 0.854
                        cd.w1 = -2.47
                        cd.w2 = 0.736
                        cd.w3 = 0
                        print "I hit something"
                        rospy.loginfo(cd)
                        pub.publish(cd)
                        time.sleep(10)
                        i = 5
                        count = count + 1
                        rate.sleep()

def callback(msg):
    aff_flag = msg.affordance
    rospy.loginfo(aff_flag)

if __name__ == '__main__':
    try:
        coordinate_gen()
    except rospy.ROSInterruptException:
        pass
