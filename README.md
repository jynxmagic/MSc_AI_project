# INSTALLATION

 sudo apt update && sudo apt install espeak ffmpeg libespeak1
 sudo apt install coreutils
 sudo apt-get install libportaudio2
 sudo apt install portaudio19-dev python3-pyaudio
 
 install all pip dependencies from requirements.txt file

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