#!/usr/bin/env python
import rospy
import socket
import time
from exploring.msg import jointAngles
from exploring.msg import coordinates
def callback(msg):
    HOST = "192.168.1.3" # The remote host
    PORT = 30002 # The sa        y_2 = -0.345 - j * 0.05
    print "Starting Program"
    count = 0
    i = 1
    j = 1
    while (count < 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        time.sleep(0.5)
        print "Robot starts Moving to starting position"
        initial_pos = str("movej([" + str(msg.base) + "," + str(msg.shoulder) + "," + str(msg.elbow) + ","+ str(msg.w1) + "," + str(msg.w2) + "," + str(msg.w3) + "], a=1.0, v=0.3)")
        s.send(initial_pos + "\n")
        time.sleep(10)
        print initial_pos
        print "I'm here"
        # while (i < 5):
        #     y = -0.345 - i * 0.05
        #     track_1 = str("movej(p[-0.325, " + str(y) + " ,0.116, 0.0165, 2.29, -2.23], a=1.0, v=0.1)")
        #     s.send (track_1 + "\n")
        #     time.sleep(5)
        #     i = i + 1
        #     print "I'm on track 1"
        # s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
        # time.sleep(10)
        # while (j < 5):
        #     x = -0.325 - j * 0.05
        #     y_2 = -0.345 - j * 0.05
        #     track_2 = str("movej(p["+ str(x) +" ," + str(y_2) + " ,0.116, 0.0165, 2.29, -2.23], a=1.0, v=0.1)")
        #     s.send (track_2 + "\n")
        #     time.sleep(5)
        #     j = j + 1
        #     print "I'm on track 2"
        # s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
        # time.sleep(10)
        # while (k < 5):
        #     x = -0.325 + k * 0.05
        #     y_3 = -0.345 - k * 0.05
        #     track_3 = str("movej(p["+ str(x) +" ," + str(y_3) + " ,0.116, 0.0165, 2.29, -2.23], a=1.0, v=0.1)")
        #     s.send (track_3 + "\n")
        #     time.sleep(5)
        #     k = k + 1
        #     print "I'm on track 3"
        # s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
        # time.sleep(10)
        count = count + 1
        print "The count is:", count
        print "Program finish"

        time.sleep(1)
        data = s.recv(1024)

        s.close()
        # print ("Received", repr(data))

    print "Status data received from robot"

    rospy.loginfo("Base joint angle is %f", msg.base)
    rospy.loginfo("Shoulder joint angle is %f", msg.shoulder)
    rospy.loginfo("Elbow joint angle is %f", msg.elbow)
    rospy.loginfo("Wrist 1 joint angle is %f", msg.w1)
    rospy.loginfo("Wrist 2 joint angle is %f", msg.w2)
    rospy.loginfo("Wrist 3 joint angle is %f", msg.w3)

def test_sub():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('test_sub', anonymous=True)

    rospy.Subscriber("/jA", jointAngles, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    test_sub()
