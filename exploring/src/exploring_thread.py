#!/usr/bin/env python
import rospy
import time
import string
from exploring.msg import coordinates
from exploring.msg import affordance
import thread

aff_flag = 0;

def robot_search():
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
            # rospy.loginfo(cd)
            pub.publish(cd)
            time.sleep(2)
        else:
            # Setting flag
            cd.flag = 0
            count = 0
            i = 1
            j = 0
            while (count < 1):
                time.sleep(0.5)
            # Assume the robot is at the initial position already
            # -0.325, " + str(y) + " ,0.116, 0.0165, 2.29, -2.23
                # position1 = str("movej(p[-0.325,-0.345,0.116,0.0065,2.29,-2.23], a=1.0, v=0.3)")
                cd.X = -0.325
                cd.Y = -0.345
                cd.Z = 0.116
                cd.Rx = 0.0065
                cd.Ry = 2.29
                cd.Rz = -2.23
                # print "Starting to search"
                while (j<10):
                    cd.Y = -0.345
                    pub.publish(cd)
                    time.sleep(3)
                    cd.X =  -0.325 - 0.065 * j
                    pub.publish(cd)
                    time.sleep(3)
                    print "X+", j
                    i = 1
                    while (i < 20):
                        # print "String", aff_flag
                        if aff_flag == 0:
                            cd.Y = -0.345 - i * 0.01
                            print "Y++"
                            wait_time = 3 + i*0.2;
                            # print wait_time
                            # print "Still going"
                            # rospy.loginfo(cd)
                            pub.publish(cd)
                            time.sleep(3)
                            # cd.Y = -0.345
                            # pub.publish(cd)
                            # time.sleep(wait_time)
                            i = i + 1
                            count = count + 1

                            # rate.sleep()
                        else:
                            cd.flag = 1
                            cd.w3 = -3.74
                            pub.publish(cd)
                            time.sleep(3)
                            cd.w3 = -2.71
                            pub.publish(cd)
                            time.sleep(3)
                            cd.w3 = -3.74
                            pub.publish(cd)
                            time.sleep(3)
                            cd.w3 = -2.71
                            pub.publish(cd)
                            time.sleep(3)
                            cd.w3 = -3.21
                            pub.publish(cd)
                            time.sleep(3)
                            # cd.flag = 0
                            # cd.Y = -0.345 - i * 0.01 + 0.02
                            # pub.publish(cd)
                            # time.sleep(3)
                            # print "Open gripper"
                            # # Open the gripper
                            # cd.Y = -0.345 - i * 0.01
                            # pub.publish(cd)
                            # time.sleep(3)
                            # while aff_flag == 0:
                            #     cd.Y = cd.Y - 0.005
                            #     pub.publish(cd)
                            #     time.sleep(3)
                            # # Close gripper
                            # print "close gripper"
                            # cd.Z = cd.Z + 0.05
                            # pub.publish(cd)
                            # time.sleep(3)
                            # cd.X = -0.325
                            # cd.Y = -0.345
                            # cd.Z = 0.116
                            # cd.Rx = 0.0065
                            # cd.Ry = 2.29
                            # cd.Rz = -2.23
                            # pub.publish(cd)
                            # time.sleep(5)
                            i = 20
                            j = 10
                    j = j + 1
def coordinate_gen():
    rospy.init_node('coordinate_gen',anonymous=True)
    pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
    aff_sub = rospy.Subscriber('/affordance',affordance,callback)
    rate = rospy.Rate(10)
    rate = rospy.Rate(10)
    cd = coordinates()
    # print "calling spin"
    thread.start_new_thread(robot_search,())
    rospy.spin()
    # print "Spinning"


def callback(msg):
    global aff_flag
    aff_flag = msg.affordance
    # rospy.loginfo(aff_flag)
    # print "Callback"

if __name__ == '__main__':
    try:
        # coordinate_gen()
        rospy.init_node('coordinate_gen',anonymous=True)
        pub = rospy.Publisher('/XYZR',coordinates, queue_size = 100)
        aff_sub = rospy.Subscriber('/affordance',affordance,callback)
        rate = rospy.Rate(10)
        rate = rospy.Rate(10)
        cd = coordinates()
        # print "calling spin"
        thread.start_new_thread(robot_search,())
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
