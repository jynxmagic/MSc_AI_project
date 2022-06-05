#! /usr/bin/env python

from TaskTemplate import TaskTemplate
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class MoveTask(TaskTemplate):
    def __init__(self) -> None:
        self.task_name="movement"
        self.topic_name="/move_topic"
        rospy.Subscriber(self.topic_name, String, self.listener_callback)
        rospy.init_node(self.task_name)
        self.cmd_vel_publisher = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        print("test")
    
    def get_task_list(self) -> dict:
        return {
            "move forward" : self.move_forward,
            "stop" : self.stop
        }

    def move_forward(self) -> None:
        message = Twist()
        message.linear.x = 1.0
        self.cmd_vel_publisher.publish(message)
    
    def stop(self) -> None:
        message = Twist()
        message.linear.x=0
        message.linear.y=0
        message.linear.z=0
        message.angular.x=0
        message.angular.y=0
        message.angular.z=0
        self.cmd_vel_publisher.publish(message)


mt = MoveTask()
rospy.spin()
