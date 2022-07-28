#! /usr/bin/env python

from std_msgs.msg import String
import rospy
import time
import random
from verbal_communication.srv import TaskDistribution, TaskDistributionRequest

rospy.init_node("task_distribution_node")

robot_name = rospy.get_param("robot_name")

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

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

while len(tasks):
    time.sleep(random.randint(30, 120))
    req.task.data = "null"
    req.robot.data = "null"
    tasks = task_service(req).remaining.data
    print("tasks remaining", len(tasks))
    remaining_tasks = len(tasks)-1

    if tasks: 
        task_to_assign = tasks[random.randint(0, remaining_tasks)]

        message = "terminator, I will do " + task_to_assign

        publisher.publish(String(message))

        req.task = String(task_to_assign)
        req.robot = String(robot_name)

        tasks = task_service(req).remaining.data