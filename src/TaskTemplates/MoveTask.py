import TaskTemplate
import rospy
from geometry_msgs.msg import Twist

class MoveTask(TaskTemplate):
    def __init__(self) -> None:
        self.task_name="movement"
        self.topic_name="/move_topic"
        self.cmd_vel_publisher = rospy.Publisher("cmd_vel", Twist)
        super().__init__()()
    
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
        message.linear.x, message.linear.y, message.linear.z = 0
        message.angular.x, message.angular.y, message.angular.z = 0
        self.cmd_vel_publisher.publish(message)

