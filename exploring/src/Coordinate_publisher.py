#!/usr/bin/env python
import rospy
import time
from exploring.msg import coordinates
from exploring.msg import j_c_flag
# from exploring.msg import coordinates

def init_pos():
    rospy.init_node('init_pos',anonymous=True)
    pub = rospy.Publisher('/jA', jointAngles, queue_size = 100)
    # pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
    rate = rospy.Rate(10)
    jt = jointAngles()
    # cd = coordinates()
    while not rospy.is_shutdown():
        count = 0
        # i = 1
        # j = 1
        while (count < 1):
            time.sleep(0.5)
            jt.base = -2.57
            jt.shoulder = -1.67
            jt.elbow = -2.31
            jt.w1 = -2.34
            jt.w2 = -2.53
            jt.w3 = -3.21
            time.sleep(10)
            print "Moving to the position"
            # -0.325, " + str(y) + " ,0.116, 0.0165, 2.29, -2.23
            # cd.X = -0.325
            # cd.Y = -0.345
            # cd.Z = 0.116
            # cd.Rx = 0.0165
            # cd.Ry = 2.29
            # cd.Rz = -2.23
            # print "Starting to search"
            # while (i < 5):
            #     cd.Y = -0.345 - i * 0.05
            #     print cd.Y
            #     i = i + 1
            # time.sleep(10)
            count = count + 1
        rospy.loginfo(jt)
        # rospy.loginfo(cd)
        pub.publish(jt)
        # pub.publish(cd)
        rate.sleep()
if __name__ == '__main__':
    try:
        init_pos()
    except rospy.ROSInterruptException:
        pass
