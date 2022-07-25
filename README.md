# INSTALLATION
1. Run the command in requirements.txt file
2. run "mics.py" to display current USB ports and replace the value "device_index" in scripts/AudioInterface/SpeechObserver.py with the USB index of your microphone.


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
