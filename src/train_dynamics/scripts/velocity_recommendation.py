#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import numpy as np

def velocity_recommender(data):
    pub = rospy.Publisher('rslidar/movement_authority', Float32, queue_size=10)
    b = 0.8 #Fixed deceleration, tbd
    v = np.sqrt(2*b*data)
    vel_rec = Float32(v)
    pub.publish(vel_rec)


def velocity_recommendation():
    rospy.init_node('velocity_recommendation')
    rospy.Subscriber('rslidar/movement_authority', Float32, velocity_recommender)
    rospy.spin()

if __name__ == '__main__':
    try:
        velocity_recommendation()
    except rospy.ROSInterruptException:
        pass
