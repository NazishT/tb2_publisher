#!/usr/bin/env python


import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

v_x = 0
w= 0

def callback(msg):
        vel_msg = Twist()
        global v_x, w
        v_x = msg.linear.x
        w = msg.angular.z  # max z for tb2 is 1.5, max for billy is 0.3
        if( v_x > 0.1 and v_x < 0.5):
	  vel_msg.linear.x = 0.05
        if (v_x > 0.5):
	  vel_msg.linear.x= 0.1
	if ( w < 0):
	  vel_msg.angular.z = -0.15
	if ( w > 0.01 and w < 1):
	  vel_msg.angular.z = 0.15 
	if (w >= 1):
	  vel_msg.angular.z = 0.3          
        pub.publish(vel_msg)
        print "Taking over teleop control at master ... "
        #print "velocity linear x=" +str(v_x)
        #print "velocity angular z=" +str(w)


if __name__=='__main__':
        rospy.init_node('odom_reader_at_master', anonymous=True)
        sub = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, callback)
        pub = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=10)
        rate=rospy.Rate(10)
       

        while not rospy.is_shutdown():
           rate.sleep()
