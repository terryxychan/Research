#!/usr/bin/env python
import rospy
import time
import string
from exploring.msg import coordinates
from exploring.msg import affordance
from robotiq_force_torque_sensor.msg import ft_sensor

# global flag

def action():
    rospy.init_node('Model')
    pub = rospy.Publisher('/affordance',affordance,queue_size = 10)
    rospy.Subscriber("/robotiq_force_torque_sensor",ft_sensor,callback)
    rate = rospy.Rate(2)
    aff = affordance()
    while not rospy.is_shutdown():
    # if flag == 1:
    #     print 'found affordance'
    #     pub.publish(affordance)
    # else:
    #     print 'No affordance'
    #     pub.publish(affordance)
        rospy.loginfo(aff)
        pub.publish(aff)
        rate.sleep()
    rospy.spin()
    time.sleep(5)

def callback(msg):
    # Determining the affordance
    # Receiving the data from the ft_sensor and determining if the affordance should be 0 or 1
    z_force = msg.Fz
    # rospy.loginfo(msg.Fz)
    if z_force < -23:
        affordance.affordance = 1
        # flag = 1
    else:
        affordance.affordance = 0
        # flag = 0

if __name__ == '__main__':
    action()
