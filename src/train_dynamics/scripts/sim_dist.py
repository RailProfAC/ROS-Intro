#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import numpy as np

def sim_dist():
    rospy.init_node('sim_dist')
    pub = rospy.Publisher('rslidar/movement_authority', Float32, queue_size=10)
    dist = Float32(30*np.random.rand())
    rate = rospy.Rate(10) # 10Hz
    while not rospy.is_shutdown():
        pub.publish(dist)
        rate.sleep()

if __name__ == '__main__':
    try:
        sim_dist()
    except rospy.ROSInterruptException:
        pass
