#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from playsound import playsound
from os import remove
rospy.init_node("speaker")


def speak(req):
    playsound(req.data)
    remove(req.data) # delete the file once done

rospy.Subscriber("encoded_message", String, speak)

rospy.spin()