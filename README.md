# INSTALLATION
1. Run the command in requirements.txt file.
2. Run "mics.py" to display current USB ports and replace the value "device_index" in scripts/AudioInterface/SpeechObserver.py with the USB index of your microphone.
3. Run ```catkin_make``` in the root catkin directory.
4. Source the setup.bash file after catkin_make
5. You can test the code is working by running the command ```roslaunch verbal_communication greeting_and_movement.launch```


 # TESTS

  ## MOVING ROBOT 1
  1. roslaunch verbal_communication move_launch.launch
  2. rostopic pub /dispatch_message std_msgs/String -1 -- "terminator, move forward"
  3. rostopic pub /dispatch_message std_msgs/String -1 -- "terminator, stop"
  4. rostopic pub /dispatch_message std_msgs/String -1 -- "terminator, rotate left"
  5. rostopic pub /dispatch_message std_msgs/String -1 -- "terminator, rotate right"

  ## MOVING ROBOT 2
  1. roslaunch verbal_communication move_launch.launch
  2. rostopic pub /dispatch_message std_msgs/String -1 -- "snow boy, move forward"
  3. rostopic pub /dispatch_message std_msgs/String -1 -- "snow boy, stop"
  4. rostopic pub /dispatch_message std_msgs/String -1 -- "snow boy, rotate left"
  5. rostopic pub /dispatch_message std_msgs/String -1 -- "snow boy, rotate right"
