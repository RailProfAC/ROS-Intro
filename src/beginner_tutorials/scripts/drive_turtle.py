#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import numpy as np

def drive_turtle():
    rospy.init_node('drive_turtle')
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        vel_msg.linear.x = 10*np.random.rand()
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 10*np.random.rand()
        rospy.loginfo(vel_msg)
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        drive_turtle()
    except rospy.ROSInterruptException:
        pass
