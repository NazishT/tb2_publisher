#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time 



def callback(event): 
    print ("20 seconds have passed!")
    rospy.signal_shutdown("Stopping the robot")


rospy.init_node('velocity_publisher', anonymous=True)
rate=rospy.Rate(10)
rospy.Timer(rospy.Duration(20), callback)

pub_cmd_vel = rospy.Publisher('/swarmbilly1/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
vel_msg.linear.x = 0.0 
vel_msg.angular.z = 0.1

    
while not rospy.is_shutdown():
    rospy.loginfo("Publishing velocities")
    pub_cmd_vel.publish(vel_msg)
    rate.sleep()
