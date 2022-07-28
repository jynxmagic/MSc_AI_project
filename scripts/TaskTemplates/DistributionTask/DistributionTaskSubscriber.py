#! /usr/bin/env python

import rospy
from verbal_communication.srv import TaskDistribution, TaskDistributionRequest
from std_msgs.msg import String

rospy.init_node("task_distribution_subscriber")
rospy.wait_for_service("task_dist_service")

req = TaskDistributionRequest()

def update_task(msg):
    robot = "terminator"
    task = msg.data.split(" ")[-1]

    try:
        task_srv = rospy.ServiceProxy("task_dist_service", TaskDistribution)
        req.task = String(task)
        req.robot = String(robot)
        res = task_srv(req)
        print(res)

    except Exception as e:
        print(e)

rospy.Subscriber("decoded_message", String, update_task)

rospy.spin()