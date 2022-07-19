#! /usr/bin/env python

from std_msgs.msg import String
import rospy
import time
import random
from verbal_communication.srv import TaskDistribution

rospy.init_node("task_distribution_publisher")

robot_name = rospy.get_param("robot_name")

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

rospy.wait_for_service("task_dist_service")
tasks = []
task_service = ""

try:
    task_service = rospy.ServiceProxy("task_dist_service", TaskDistribution)
except Exception as e:
    print("failed to load service. ", e)
tasks_res = task_service(String("null,null"))
print("tasks res", tasks_res)
tasks = tasks_res.remaining.data.split(",")

print("tasks remaining", len(tasks))
while len(tasks):
    time.sleep(random.randint(30, 120))
    print("tasks remaining", len(tasks))
    remaining_tasks = len(tasks)-1

    task_to_assign = tasks[random.randint(0, remaining_tasks)]

    message = "terminator, I will do " + task_to_assign

    publisher.publish(String(message))

    tasks_res = task_service(String(task_to_assign+","+robot_name))
    tasks = tasks_res.remaining.data.split(",")
