#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time 


class VelocityPublisher():
    def __init__(self):
    
        # publisher and subscribers
        self.sub_twist = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, self.get_twist, queue_size=10)
        self.pub_twist = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=10)
        

        # initialize the node 
        # accomodate rate of publishing
        rospy.init_node("velocity_publisher", anonymous=True)
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
        self.publish_twist()
        rospy.spin()


        # on shutdown
        rospy.on_shutdown(self.stop_robot)

    # get data from turtlebot 
    def get_twist(self, msg):
        self.vx = msg.linear.x
        self.vw = msg.angular.z

    # set data to a Twist msg
    def publish_twist(self, str_msg = "velocity"):
        self.twist_msg = Twist()
        self.twist_msg.linear.x = self.vx
        self.twist_msg.angular.z = self.vw
        #publish that twist msg as swarmbot's velocity
        rospy.loginfo("Publishing %s to swarmbot.." % str_msg)
        self.pub_twist.publish(self.twist_msg)
    
    def stop_robot(self):
        self.twist_msg.linear.x = 0
        self.twist_msg.angular.z = 0 
        self.publish_twist("stop")



if __name__ == "__main__":
    try:    
        VelocityPublisher()
        #rospy.spin()  
        
    except rospy.ROSInterruptException:
        rospy.signal_shutdown("Shutting down ... ")