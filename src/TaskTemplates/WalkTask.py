import TaskTemplate
import rospy
from geometry_msgs.msg import Twist

class WalkTask(TaskTemplate):
    def __init__(self) -> None:
        super().__init__()()
        self.task_name="walk"
        self.cmd_vel_publisher = rospy.Publisher("cmd_vel", Twist)
    
    def get_task_list(self) -> dict:
        return {
            "walk forward" : self.walk_forward()
        }

    def walk_forward(self) -> None:
        message = Twist()
        message.linear.x = 1.0
        self.cmd_vel_publisher.publish(message)


