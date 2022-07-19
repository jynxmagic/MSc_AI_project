#! /usr/bin/env python

import rospy
from verbal_communication.srv import TaskDistribution
from std_msgs.msg import String

rospy.init_node("task_distribution_subscriber")
rospy.wait_for_service("task_dist_service")

def update_task(msg):
    robot = "terminator"
    task = msg.data[-1]

    try:
        task_srv = rospy.ServiceProxy("task_dist_service", TaskDistribution)
        res = task_srv(String(task+","+robot))
        print(res)

    except Exception as e:
        print(e)

rospy.Subscriber("encoded_message", String, update_task)

rospy.spin()