#! /usr/bin/env python

from time import sleep
import pvleopard
import rospy
from std_msgs.msg import String
from gtts import gTTS
import pathlib
from os.path import exists


rospy.init_node("audio_encoder")
leopard = pvleopard.create(access_key='OX9bSVHcnyOpSrYKfmrJOh43DAg7d7kQ6BP0PWatLJMXgdOQrmoNOA==')
decode_publisher = rospy.Publisher("decoded_message", String, queue_size=5)
encode_publisher = rospy.Publisher("encoded_message", String, queue_size=5)
dispatch_file = pathlib.Path(__file__).parent.resolve().__str__()+"/dispatch/message.mp3"


tts_engine = gTTS

def audio_decoder_callback(req: String):
    """Decodes speech from audio file into a string.

    Args:
        req (std_msgs/String): audio file location
    """
    print(req)
    while not exists(req.data):
        sleep(1) # raspberry pi has quite slow disk i/o so we need to wait for the file to appear
    
    decoded_message = String(leopard.process_file(req.data)[0])
    decode_publisher.publish(decoded_message)

def audio_encoder_callback(req: String):
    """Creates an audio file from provided String.

    Args:
        req (std_msgs/String): Text to turn into speech
    """
    tts = gTTS(req.data)
    tts.save(dispatch_file)
    while not exists(dispatch_file): # wait for the file to write before publishing
        sleep(1)
    encode_publisher.publish(dispatch_file)
    sleep(3)
    

rospy.Subscriber("audio_found", String, audio_decoder_callback)
rospy.Subscriber("dispatch_message", String, audio_encoder_callback)
rospy.spin()