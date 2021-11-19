#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time 


class VelocityPublisher:
    def __init__(self):

        # publisher and subscribers
        self.sub_twist = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, self.get_twist, queue_size=10)
        self.pub_twist = rospy.Publisher('/swarmbilly1/cmd_vel', Twist, queue_size=5)
        self.twist_msg = Twist()

        # initialize the node 
        # accomodate rate of publishing
        rospy.init_node("velocity_publisher", anonymous=True, disable_signals=True)
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
        rospy.spin()


    # get data from turtlebot and send to publish
    def get_twist(self, msg):
        self.vx = msg.linear.x
        self.vw = msg.angular.z
        self.publish_twist(self.vx, self.vw)

    # set data to a Twist msg
    def publish_twist(self, vx, vw):
        
        #self.twist_msg.linear.x = self.vx * 0.16
        #self.twist_msg.angular.z = self.vw * 0.50
        self.twist_msg.linear.x = self.vx * 0.16
        self.twist_msg.angular.z = self.vw 
        #if self.vw > 0: 
            #self.twist_msg.linear.x = 0.0
            #self.twist_msg.angular.z = self.vw * 0.50
        #else:
            #self.twist_msg.angular.z = 0.0
        #publish that twist msg as swarmbot's velocity
        rospy.loginfo("Publishing twist velocity to swarmbot..")
        self.pub_twist.publish(self.twist_msg)
        #rospy.spin()




if __name__ == "__main__":
    try:    
        VelocityPublisher()
        #rospy.spin()  
        
    except KeyboardInterrupt:
        pass
   
        
