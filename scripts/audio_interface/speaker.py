#! /usr/bin/env python
"""Module for playing sound files."""
from os import remove

import rospy
from playsound import playsound
from std_msgs.msg import String

rospy.init_node("speaker")


def speak(req: String):
    """Plays the sound file found at location: req.data

    Args:
        req (std_msgs/String): Location of sound file
    """
    playsound(req.data)
    remove(req.data)  # delete the file once done


rospy.Subscriber("encoded_message", String, speak)

rospy.spin()
