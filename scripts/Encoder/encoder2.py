import pyttsx3
import pathlib


file_name = pathlib.Path(__file__).parent.resolve().__str__()+"/dispatch/message.wav"

engine = pyttsx3.init()

engine.save_to_file("terminator... move forward", file_name)

engine.runAndWait()
