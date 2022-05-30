import rospy
from std_msgs.msg import String

class TaskTemplate:
    def __init__(self) -> None:
        rospy.init_node(self.task_name if self.task_name else "default_task")
        rospy.Subscriber(self.topic_name if self.topic_name else "/default_task_topic", String, self.listener_callback)
        rospy.spin()

    
    def listener_callback(self, data) -> None:
        if data in self.get_task_list().keys():
            self.get_task_list()[data]()
        else:
            print("Couldn't find task ", data)
        return

    def get_task_list() -> dict:
        return {}