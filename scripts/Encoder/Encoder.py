#! /usr/bin/env python

import pvleopard
import rospy
from std_msgs.msg import String
from gtts import gTTS
import pathlib

rospy.init_node("audio_encoder")
leopard = pvleopard.create(access_key='OX9bSVHcnyOpSrYKfmrJOh43DAg7d7kQ6BP0PWatLJMXgdOQrmoNOA==')
decode_publisher = rospy.Publisher("decoded_message", String, queue_size=1)
encode_publisher = rospy.Publisher("encoded_message", String, queue_size=1)
dispatch_file = pathlib.Path(__file__).parent.resolve().__str__()+"/dispatch/message.mp3"


tts_engine = gTTS

def audio_decoder_callback(req):
    print(req)
    decoded_message = String(leopard.process_file(req.data))
    decode_publisher.publish(decoded_message)

def audio_encoder_callback(req):
    tts = gTTS(req.data)
    tts.save(dispatch_file)
    encode_publisher.publish(dispatch_file)
    

rospy.Subscriber("audio_found", String, audio_decoder_callback)
rospy.Subscriber("dispatch_message", String, audio_encoder_callback)
rospy.spin()