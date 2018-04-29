#!/usr/bin/env python

import rospy
from robotiq_force_torque_sensor.msg import ft_sensor

def callback1(rosMsg1):   #for pose_euler
    with open('ft_data.csv','a') as fid_euler:
	fid_euler.write('%.6f, %.6f, %.6f, %.6f, %.6f, %.6f\n' %(rosMsg1.Fx,rosMsg1.Fy,rosMsg1.Fz,rosMsg1.Mx,rosMsg1.My,rosMsg1.Mz))
def main():
    rospy.init_node('Data_record', anonymous='True')
    rospy.Subscriber('robotiq_force_torque_sensor', ft_sensor, callback1)
    rospy.spin()
if __name__ == '__main__':
    main()
