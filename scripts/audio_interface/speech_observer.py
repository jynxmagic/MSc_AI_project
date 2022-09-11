#! /usr/bin/env python
"""Module which observes speech and then records a sound file if a key word is hit"""
import pathlib
import struct
import time
import wave

import pvporcupine
import rospy
from pvrecorder import PvRecorder
from std_msgs.msg import String

# init some params
TIME_TO_RECORD_FOR = 3
FILE_NAME = str(pathlib.Path(__file__).parent.resolve()) + "/recieved/message.wav"

rospy.init_node("audio_recorder")
robot_name = rospy.get_param("robot_name")
print("this robot is called ", robot_name)
publisher = rospy.Publisher("audio_found", String, queue_size=1)
message = String()
message.data = FILE_NAME

devices = PvRecorder.get_audio_devices()
porcupine = pvporcupine.create(
    access_key='OX9bSVHcnyOpSrYKfmrJOh43DAg7d7kQ6BP0PWatLJMXgdOQrmoNOA==',
    keywords=[robot_name, "jarvis"]  # jarvis is the global identifier for all robots
)


recorder = PvRecorder(device_index=-1, frame_length=512)

rospy.loginfo("recorder started")
recorder.start()

time_then = time.time()

# begin recording
while True:
    pcm = recorder.read()  # read sound data
    result = porcupine.process(pcm)  # process if sound data contains key word

    if result >= 0:
        rospy.loginfo("Key word hit")
        time_then = time.time()
        TIME_PASSED = False
        wav_file = wave.open(FILE_NAME, "w")
        wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        while TIME_PASSED is False:  # record the next 3 seconds of input
            pcm_to_record = recorder.read()
            wav_file.writeframes(struct.pack("h" * len(pcm_to_record), *pcm_to_record))
            if time.time() - time_then > TIME_TO_RECORD_FOR:
                TIME_PASSED = True
                wav_file.close()
                publisher.publish(message)  # publish sound file location after record time has passed
        rospy.loginfo("saved input")
