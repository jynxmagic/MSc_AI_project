#! /usr/bin/env python
"""Updates task repository with tasks the other robot is assigned to."""
import rospy
from std_msgs.msg import String
from verbal_communication.srv import task_distribution, task_distributionRequest

rospy.init_node("task_distribution_subscriber")
rospy.wait_for_service("task_dist_service")

req = task_distributionRequest()


def update_task(msg: String):
    """Updates the task repository with tasks the other robot is doing.

    Args:
        msg (std_msgs/String): String which contains the task the robot is doing (the last word of the string must be task name).
    """
    robot = "terminator"
    task = msg.data.split(" ")[-1]  # it is always the last word which contains the task name

    try:
        task_srv = rospy.ServiceProxy("task_dist_service", task_distribution)
        req.task = String(task)
        req.robot = String(robot)
        res = task_srv(req)
        print(res)

    except Exception as exception:
        print(exception)


rospy.Subscriber("decoded_message", String, update_task)

rospy.spin()
