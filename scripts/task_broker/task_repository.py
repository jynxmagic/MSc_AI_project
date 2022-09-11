#! /usr/bin/env python
"""Updates and controls the tasks available to the robot."""
import rospy
from verbal_communication.msg import string_array
from verbal_communication.srv import task_distributionRequest, task_distribution

rospy.init_node("conversation_broker_node")

available_tasks = [
    "ORANGE",
    "YELLOW",
    "GREEN",
    "INDIGO",
    "VIOLET"
]

assignments = {
    "bumblebee" : [],
    "terminator" : []
}


def assignement_update(req: task_distributionRequest) -> string_array:
    """Assigns a robot to a task, and returns the available tasks.

    Args:
        req (task_distributionRequest): Service request containing task at req.task.data and robot name at req.robot.data

    Returns:
        string_array: Remaining tasks
    """
    task = req.task.data
    robot = req.robot.data

    if task in available_tasks:
        available_tasks.remove(task)
        assignments[robot].append(task)

    print("tasks in service", available_tasks)

    for robot in [*assignments.keys()]:
        rospy.set_param(robot + "_assignments", assignments[robot])  # the parameter server also contains the other robots tasks

    return string_array(available_tasks)


rospy.Service("task_dist_service", task_distribution, assignement_update)

rospy.spin()
