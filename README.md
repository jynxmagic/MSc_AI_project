# INSTALLATION
1. Run the command in requirements.txt file.
2. Run "mics.py" to display current USB ports and replace the value "device_index" in scripts/audio_interface/speech_observer.py with the USB index of your microphone.
3. Run ```catkin_make``` in the root catkin directory.
4. Source the setup.bash file after catkin_make
5. You can test the code is working by running the command ```roslaunch verbal_communication greeting_and_movement.launch```


 # TESTS

  ## MOVING ROBOT
  1. roslaunch verbal_communication greeting_and_movement.launch
  2. rostopic pub /decoded_message std_msgs/String -1 -- "MOVE FORWARD"
  3. rostopic pub /decoded_message std_msgs/String -1 -- "STOP"
  4. rostopic pub /decoded_message std_msgs/String -1 -- "ROTATE LEFT"
  5. rostopic pub /decoded_message std_msgs/String -1 -- "ROTATE RIGHT"

  ## MOVING ROBOT (no rostopic)
  1. roslaunch verbal_communication greeting_and_movement.launch
  2. say "[robot_name] [command]"

  ## GREETING ROBOT
  1. roslaunch verbal_communication greeting_and_movement.launch
  2. rostopic pub /decoded_message std_msgs/String -1 -- "HELLO I AM CHRIS" (robot should reply with its name)

  ## GREETING ROBOT (no rostopic)
  1. roslaunch verbal_communication greeting_and_movement.launch
  2. say "jarvis, hello I am [your_name]"

  ## TASK DISTRIBUTION
  1. roslaunch verbal_communication task_distribution.launch
  2. the robot should begin assigning itself to tasks: yellow, green, orange, blue, indigo, violet
  3. to say you will complete one of the following say: "[robot_name], I will do [task]"
  4. or: rostopic pub /decoded_message std_msgs/String -1 -- "I WILL DO [task]"

Note. All messages are translated into full caps. If you publish a message to the robot rather than speak, you should always publish the message with full caps.
