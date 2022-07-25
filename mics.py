#! /usr/bin/env python

from pvrecorder import PvRecorder

devices = PvRecorder.get_audio_devices()

print(devices)
