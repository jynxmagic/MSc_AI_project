#! /usr/bin/env python
"""This is a simple test to execute from a 2nd robot to make the robot issue commands to the first robot for the movement task."""
import time

import rospy
from std_msgs.msg import String

#import random

rospy.init_node("simple_test")

robot_name = rospy.get_param("robot_name")

publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

#available_commands = [
#    "MOVE FORWARD",
#    "ROTATE LEFT",
#    "ROTATE RIGHT",
#    "STOP"
#]

for i in range(0, 20):
    time.sleep(10)

    TO = "bumblebee"

#    command = available_commands[random.randint(0,3)]

    full_command = TO + "... " + "MOVE FORWARD"

    publisher.publish(String(full_command))


#This simple test was used to make the robot say 20 times, "move forward". The other robot involved would then execute the commands
