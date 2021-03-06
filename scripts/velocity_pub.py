#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time 


class VelocityPublisher:
    def __init__(self):

        # publisher and subscribers
        self.sub_twist = rospy.Subscriber('/robot2/mobile_base/commands/velocity', Twist, self.get_twist, queue_size=10)
        self.pub_twist = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=10)
        

        # initialize the node 
        # accomodate rate of publishing
        rospy.init_node("velocity_publisher", anonymous=True, disable_signals=True)
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
        rospy.spin()

        # on shutdown
        #rospy.on_shutdown(self.stop_robot)

    # get data from turtlebot and send to publish
    def get_twist(self, msg):
        self.vx = msg.linear.x
        self.vw = msg.angular.z
        self.publish_twist(self.vx, self.vw)

    # set data to a Twist msg
    def publish_twist(self, vx, vw):
        self.twist_msg = Twist()
        self.twist_msg.linear.x = self.vx
        self.twist_msg.angular.z = self.vw
        #publish that twist msg as swarmbot's velocity
        rospy.loginfo("Publishing twist velocity to swarmbot..")
        self.pub_twist.publish(self.twist_msg)
        #rospy.spin()

    @staticmethod
    def stop_robot():
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        rospy.loginfo("Publishing stop velocity")
        pub = rospy.Publisher('/swarmbilly/cmd_vel', Twist, queue_size=10)
        pub.publish(stop_msg)



if __name__ == "__main__":
    try:    
        VelocityPublisher()
        #rospy.spin()  
        
    except KeyboardInterrupt:
        pass
    finally:
        rospy.loginfo("interrupted!")
        VelocityPublisher.stop_robot()
        time.sleep(5)
