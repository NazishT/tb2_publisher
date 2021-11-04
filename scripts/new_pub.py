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
	print  "tb's linear velocity= " + str(v_x)
        w = msg.angular.z  # max z for tb2 is 1.5, max for billy is 0.3
        print "tb's angular velocity= " + str(w)

        if( v_x > 0.01 and v_x < 1):
		vel_msg.linear.x = 0.05
	elif (v_x > 1 and v_x < 5):
		vel_msg.linear.x = 0.1
        else:
		vel_msg.linear.x = 0


        if (w < 0 or w==0):
	  vel_msg.angular.z = 0
        else:
	  vel_msg.angular.z = w 
        pub.publish(vel_msg)

        print "Publishing velocities at swarmbilly ... "
        print "swarmbilly linear x=" +str(vel_msg.linear.x)
        print "swarmbilly angular z=" +str(vel_msg.angular.z)

def myhook():
	print "shutting down!"


if __name__=='__main__':
        rospy.init_node('swarm_subscriber', anonymous=True)
        #sub = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, callback)
        #pub = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=10)
        rate=rospy.Rate(10)
        while not rospy.is_shutdown():
           sub = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, callback)
	   pub = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=20)
           rate.sleep()
        #rospy.on_shutdown(myhook)
