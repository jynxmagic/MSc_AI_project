#! /usr/bin/env python

import rospy
from verbal_communication.srv import TaskDistribution
from verbal_communication.msg import StringArray

rospy.init_node("conversation_broker_node")

available_tasks = ["ORANGE", "YELLOW", "GREEN", "INDIGO", "VIOLET"]

assignments = {
    "bumblebee" : [],
    "terminator" : []
}

def assignement_update(req):
    task = req.task.data
    robot = req.robot.data

    print("testr", task, robot)
    if task in available_tasks:
        available_tasks.remove(task)
        assignments[robot].append(task)
    else:
        print(robot, " could not be assinged to task ", task, ", it does not exist")

    print("tasks in service", available_tasks)

    for k in [*assignments.keys()]:
        rospy.set_param(k+"_assignments", assignments[k])


    return StringArray(available_tasks)

rospy.Service("task_dist_service", TaskDistribution, assignement_update)

rospy.spin()
