#! /usr/bin/env python

import rospy
from verbal_communication.srv import AudioDecoder
from std_msgs.msg import String

rospy.init_node("audio_decoder_main")
rospy.wait_for_service("/audio_decoder")

file_path = String('/home/chris/catkin_ws/src/verbal_communication/scripts/Encoder/audio.wav')

try:
    audio_srv = rospy.ServiceProxy("audio_decoder", AudioDecoder)
    res = audio_srv(file_path)
    rospy.loginfo(res.text.data)

    publisher = rospy.Publisher("move_topic", String, queue_size=1)
    publisher.publish(res.text)

except Exception as e:
    print(e)