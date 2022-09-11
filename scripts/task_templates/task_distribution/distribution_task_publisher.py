#! /usr/bin/env python
"""Publishes tasks which the robot has assigned itself to."""
import random
import time

import rospy
from std_msgs.msg import String
from verbal_communication.msg import string_array
from verbal_communication.srv import task_distribution, task_distributionRequest

rospy.init_node("task_distribution_node")

robot_name = rospy.get_param("robot_name")

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

task_publisher = rospy.Publisher("execute_tasks", string_array, queue_size=1)  # this publisher is for later on

rospy.wait_for_service("task_dist_service")
tasks = []
TASK_SERVICE = ""

try:
    TASK_SERVICE = rospy.ServiceProxy("task_dist_service", task_distribution)
except Exception as exception:
    print("failed to load service. ", exception)


# get the initial tasks
req = task_distributionRequest()
req.task.data = "null"
req.robot.data = "null"
tasks_res = TASK_SERVICE(req)
tasks = tasks_res.remaining.data
print("tasks remaining", len(tasks))

while len(tasks) > 0:
    time.sleep(20)
    req.task.data = "null"
    req.robot.data = "null"
    tasks = TASK_SERVICE(req).remaining.data
    print("tasks remaining", len(tasks))
    remaining_tasks = len(tasks) - 1

    if tasks: 
        task_to_assign = tasks[random.randint(0, remaining_tasks)]

        message = "bumblebee... I will do " + task_to_assign

        publisher.publish(String(message))

        req.task = String(task_to_assign)
        req.robot = String(robot_name)

        tasks = TASK_SERVICE(req).remaining.data

# now all the tasks are distributed, publish the tasks the robot is assigned to
self_assignments = rospy.get_param(robot_name + "_assignments")
other_assignments = rospy.get_param("terminator_assignments")

print("I am assigned to", self_assignments)
print("Terminator is assigned to", other_assignments)
task_publisher.publish(string_array(self_assignments))


time.sleep(4)  # just to ensure the message publishes correctly (the node can shutdown before the message is sent sometimes)
