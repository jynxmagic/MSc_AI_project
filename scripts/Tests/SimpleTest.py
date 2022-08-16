#! /usr/bin/env python

from std_msgs.msg import String
import rospy
import time
import random

rospy.init_node("simple_test")

robot_name = rospy.get_param("robot_name")

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

available_commands = [
    "MOVE FORWARD",
    "ROTATE LEFT",
    "ROTATE RIGHT",
    "STOP"
]

for i in range(0, 20):
    time.sleep(10)

    to = "bumblebee"

    command = available_commands[random.randint(0,3)]

    full_command = to + "... " + command

    publisher.publish(String(full_command))