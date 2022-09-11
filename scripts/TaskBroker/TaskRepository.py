#! /usr/bin/env python
import rospy
from verbal_communication.srv import TaskDistribution, TaskDistribtuionRequest
from verbal_communication.msg import StringArray

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

def assignement_update(req: TaskDistribtuionRequest) -> StringArray:
    """Assigns a robot to a task, and returns the available tasks.

    Args:
        req (TaskDistribtuionRequest): Service request containing task at req.task.data and robot name at req.robot.data

    Returns:
        StringArray: Remaining tasks
    """
    task = req.task.data
    robot = req.robot.data

    if task in available_tasks:
        available_tasks.remove(task)
        assignments[robot].append(task)

    print("tasks in service", available_tasks)

    for robot in [*assignments.keys()]:
        rospy.set_param(robot+"_assignments", assignments[robot]) # the parameter server also contains the other robots tasks


    return StringArray(available_tasks)

rospy.Service("task_dist_service", TaskDistribution, assignement_update)

rospy.spin()
