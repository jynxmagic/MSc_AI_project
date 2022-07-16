#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from playsound import playsound

rospy.init_node("speaker")


def speak(req):
    playsound(req.data)

rospy.Subscriber("encoded_message", String, speak)

rospy.spin()