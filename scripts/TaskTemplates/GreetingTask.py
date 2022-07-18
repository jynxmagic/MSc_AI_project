#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import re


task_name="greeting"
topic_name="decoded_message"
robot_name = rospy.get_param("robot_name")

known_robots = [robot_name.upper()]

rospy.init_node(task_name)

communication_publisher = rospy.Publisher("dispatch_message", String, queue_size=1)

def get_regex_test_list() -> dict:
    return {
        "HELLO I AM" : robot_greeting,
        "HELLO ALL" : respond_to_global,
        "ASK GLOBAL" : ask_global
    }

def listener_callback(msg) -> None:
    print("HIT TASK")
    print(msg)
    msg.data = msg.data.strip()
    for i in [*get_regex_test_list().keys()]:
        regtest = re.compile(r'\b('+i+r')\b')
        if regtest.search(msg.data):
            print("matched", i)
            get_regex_test_list()[i](msg.data)
    return


def respond_to_global(msg) -> None:
    message = "jarvis, Hello, I am " + robot_name
    communication_publisher.publish(message)

def ask_global(msg) -> None:
    message = "jarvis, Hello all"
    communication_publisher.publish(message)

def robot_greeting(msg) -> None:
    from_robot = msg.replace("HELLO I AM ", "")
    if from_robot not in known_robots:
        known_robots.append(from_robot)
        message = from_robot +" HELLO, I AM " + robot_name
        communication_publisher.publish(message)
    else:
        print("already know" + from_robot)

rospy.Subscriber(topic_name, String, listener_callback)

    
rospy.spin()
