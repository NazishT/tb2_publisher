#!/usr/bin/env python
import rospy
import roslib
from geometry_msgs.msg import Twist


class VelocityPublisher():
    def __init__(self):
    
        # initialize the node 
        rospy.init_node("velocity_publisher", anonymous=True)
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
        # publisher and subscribers
        self.pub_twist = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=10)
        self.sub_twist = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, self.get_twist, queue_size=10)

    # get data from turtlebot 
    def get_twist(self, msg):
        self.vx = msg.linear.x
        self.vw = msg.angular.z

    # set data to a Twist msg
    def set_twist(self):
        self.twist_msg = Twist()
        self.twist_msg.linear.x = self.vx
        self.twist_msg.angular.z = self.vw
        #publish that twist msg as swarmbot's velocity
        self.pub_twist.publish(self.twist_msg)
    
    def shut_down(self):
        self.twist_msg.linear.x = 0
        self.twist_msg.angular.z = 0 
        self.pub_twist.publish(self.twist_msg)



if __name__ == "__main__":
    try:    
        VelocityPublisher()
        rospy.spin()  
        
    except rospy.ROSInterruptException:
        print("shutting down")

