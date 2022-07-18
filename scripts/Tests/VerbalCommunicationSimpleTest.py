#! /usr/bin/env python

from std_msgs.msg import String
import rospy
import time
import random

rospy.init_node("simple_test")

robot_name = rospy.get_param("robot_name")

known_robots = ["jarvis", "bumblebee", "terminator", "fake name"]
known_robots.remove(robot_name)

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

available_commands = [
    "HELLO ALL",
    "MOVE FORWARD",
    "ROTATE LEFT",
    "ROTATE RIGHT",
    "STOP"
]

for i in range(0, 20):
    time.sleep(random.randint(10, 20))

    to = known_robots[random.randint(0,2)]

    command = available_commands[random.randint(0,4)]

    full_command = to + ", " + command

    publisher.publish(String(full_command))