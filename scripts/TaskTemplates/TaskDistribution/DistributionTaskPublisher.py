#! /usr/bin/env python

from verbal_communication.msg import StringArray
from std_msgs.msg import String
import rospy
import time
import random
from verbal_communication.srv import TaskDistribution, TaskDistributionRequest

rospy.init_node("task_distribution_node")

robot_name = rospy.get_param("robot_name")

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

task_publisher = rospy.Publisher("execute_tasks", StringArray, queue_size=1) #this publisher is for later on

rospy.wait_for_service("task_dist_service")
tasks = []
task_service = ""

try:
    task_service = rospy.ServiceProxy("task_dist_service", TaskDistribution)
except Exception as e:
    print("failed to load service. ", e)


#Get Init Tasks
req = TaskDistributionRequest()
req.task.data = "null"
req.robot.data = "null"
tasks_res = task_service(req)
tasks = tasks_res.remaining.data
print("tasks remaining", len(tasks))

while len(tasks) > 0:
    time.sleep(20)
    req.task.data = "null"
    req.robot.data = "null"
    tasks = task_service(req).remaining.data
    print("tasks remaining", len(tasks))
    remaining_tasks = len(tasks)-1

    if tasks: 
        task_to_assign = tasks[random.randint(0, remaining_tasks)]

        message = "bumblebee... I will do " + task_to_assign

        publisher.publish(String(message))

        req.task = String(task_to_assign)
        req.robot = String(robot_name)

        tasks = task_service(req).remaining.data

#Now all the tasks are distributed, let's execute them

self_assignments = rospy.get_param(robot_name+"_assignments")
other_assignments = rospy.get_param("terminator_assignments")

print("I am assigned to", self_assignments)
print("Terminator is assigned to", other_assignments)
task_publisher.publish(StringArray(self_assignments))


time.sleep(4) #just to ensure the message publishes correctly (the node can shutdown before the message is sent sometimes)