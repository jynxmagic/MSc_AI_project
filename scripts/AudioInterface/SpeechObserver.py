#! /usr/bin/env python
from std_msgs.msg import String
import rospy
from pvrecorder import PvRecorder
import pvporcupine
import time
import wave
import struct
import pathlib

TIME_TO_RECORD_FOR = 3
file_name = pathlib.Path(__file__).parent.resolve().__str__()+"/recieved/message.wav"

rospy.init_node("audio_recorder")
robot_name = rospy.get_param("SpeechObserver/robot_name")
print("this robot is called ", robot_name)
publisher = rospy.Publisher("audio_found", String, queue_size=1)
message = String()
message.data = file_name

devices = PvRecorder.get_audio_devices()
porcupine = pvporcupine.create(
    access_key='OX9bSVHcnyOpSrYKfmrJOh43DAg7d7kQ6BP0PWatLJMXgdOQrmoNOA==',
    keywords=[robot_name]
    )


recorder = PvRecorder(device_index=-1, frame_length=512)

key_pressed = False
rospy.loginfo("recorder started")
recorder.start()

time_then = time.time()
passed = False
while True:
    pcm = recorder.read()
    
    result = porcupine.process(pcm)
    
    if result >= 0:
        rospy.loginfo("Key word hit")
        time_then = time.time()
        time_passed = False
        wav_file = wave.open(file_name, "w")
        wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        while time_passed is False:
            pcm_to_record = recorder.read()
            wav_file.writeframes(struct.pack("h" * len(pcm_to_record), *pcm_to_record))
            if(time.time() - time_then > TIME_TO_RECORD_FOR):
                time_passed = True
                wav_file.close()
                publisher.publish(message)
        rospy.loginfo("saved input")