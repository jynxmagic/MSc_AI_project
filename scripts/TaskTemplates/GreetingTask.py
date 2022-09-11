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
    """Returns a dict of regex pattern matches to search for within a string, along with mapped functions

    Returns:
        dict: List of strings to search for, and attached functions.
    """
    return {
        "HELLO I AM" : robot_greeting,
        "HELLO ALL" : respond_to_global,
        "ASK GLOBAL" : ask_global
    }

def listener_callback(msg: String):
    """Matches a provided string against the list of available strings, and executes the corresponding task.

    Args:
        msg (String): String with which to match against the available statements.
    """
    msg.data = msg.data.strip()
    for i in [*get_regex_test_list().keys()]:
        regtest = re.compile(r'\b('+i+r')\b') # try to regex match the strings
        if regtest.search(msg.data):
            get_regex_test_list()[i](msg.data)

def respond_to_global(msg : String):
    """Robot replies to a global message.

    Args:
        msg (std_msgs/String): Not required
    """
    message = "jarvis, Hello, I am " + robot_name
    communication_publisher.publish(message)

def ask_global(msg : String):
    """Asks all robots for their names.

    Args:
        msg (std_msgs/String): Not required
    """
    message = "jarvis, Hello all"
    communication_publisher.publish(message)

def robot_greeting(msg : String):
    """Responds to a robot which has initiated greeting.

    Args:
        msg (std_msgs/String): Message recieved from the other robot(/s).
    """
    from_robot = msg.replace("HELLO I AM ", "")
    if from_robot not in known_robots:
        known_robots.append(from_robot)
        message = from_robot +" HELLO, I AM " + robot_name
        communication_publisher.publish(message)
    else:
        print("already know" + from_robot)

rospy.Subscriber(topic_name, String, listener_callback)

    
rospy.spin()
