#! /usr/bin/env python

import rospy
from verbal_communication.srv import TaskDistribution
from std_msgs.msg import String

rospy.init_node("task_distribution_service")

available_tasks = ["RED", "GREEN", "BLUE", "YELLOW", "PURPLE", "ORANGE"]

assignments = {
    "bumblebee" : [],
    "terminator" : []
}

def assignement_update(req):
    task, robot = req.update.data.split(",")
    print("testr", task, robot)
    if task in available_tasks:
        available_tasks.remove(task)
        assignments[robot].append(task)
    print("tasks in service", available_tasks)
    tasks_string = ",".join(available_tasks)
    print(assignments)
    if len(available_tasks) == 0:
        print(assignments)
    return String(tasks_string)

rospy.Service("task_dist_service", TaskDistribution, assignement_update)

rospy.spin()