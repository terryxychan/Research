#!/usr/bin/env python
import rospy
import socket
import time
from mechanism.msg import coordinates

def callback(msg):
    HOST = "192.168.1.3" # The remote host
    PORT = 30002

    # print "Starting Program"
    count = 0

    while (count < 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        time.sleep(0.5)
        flag = msg.flag
        # print "Robot moving"
        if flag == 0:
            position1 = str("movej(p[" + str(msg.X) + "," + str(msg.Y) + "," + str(msg.Z) + ","+ str(msg.Rx) + "," + str(msg.Ry) + "," + str(msg.Rz) + "], a=0.3, v=0.3)")
            s.send(position1 + "\n")
            time.sleep(1)
            # print position1
            print "Flag is 0"
            # print "I'm exploring"
            count = count + 1
            # print "The count is:", count
            # print "Program finish"
            rospy.loginfo("X is %f", msg.X)
            rospy.loginfo("Y is %f", msg.Y)
            rospy.loginfo("Z is %f", msg.Z)
            rospy.loginfo("Rx is %f", msg.Rx)
            rospy.loginfo("Ry is %f", msg.Ry)
            rospy.loginfo("Rz is %f", msg.Rz)
        else:
            position2 = str("movej([" + str(msg.base) + "," + str(msg.shoulder) + "," + str(msg.elbow) + ","+ str(msg.w1) + "," + str(msg.w2) + "," + str(msg.w3) + "], a=0.3, v=0.3)")
            s.send(position2 + "\n")
            time.sleep(1)
            # print position2
            print "Flag is 1"
            # print "I'm at home"
            count = count + 1
            # print "The count is:", count
            # print "Program finish"
            rospy.loginfo("Base is %f", msg.base)
            rospy.loginfo("Shoulder is %f", msg.shoulder)
            rospy.loginfo("Elbow is %f", msg.elbow)
            rospy.loginfo("w1 is %f", msg.w1)
            rospy.loginfo("w2 is %f", msg.w2)
            rospy.loginfo("w3 is %f", msg.w3)
        time.sleep(1)
        data = s.recv(1024)

        s.close()
        # print ("Received", repr(data))

    print "Status data received from robot"



def moving_coordinates():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('moving_coordinates', anonymous=True)
    rospy.Subscriber("/XYZR", coordinates, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    moving_coordinates()
