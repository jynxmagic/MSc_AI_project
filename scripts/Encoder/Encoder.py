#! /usr/bin/env python

import pvleopard
import pathlib

import rospy
from std_msgs.msg import String
from verbal_communication.srv import AudioDecoder, AudioDecoderResponse

leopard = pvleopard.create(access_key='OX9bSVHcnyOpSrYKfmrJOh43DAg7d7kQ6BP0PWatLJMXgdOQrmoNOA==')
dir = pathlib.Path(__file__).parent.resolve().__str__()

def audio_decoder_callback(req):
    return String(leopard.process_file(req.file_path.data))
    

rospy.init_node("Encoder")
service = rospy.Service('audio_decoder', AudioDecoder, audio_decoder_callback)


rospy.spin()