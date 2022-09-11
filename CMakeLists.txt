cmake_minimum_required(VERSION 3.0.2)
project(verbal_communication)

# search for required packes
find_package(catkin REQUIRED COMPONENTS 
  roscpp 
  std_msgs 
  message_generation
  geometry_msgs
  move_base
  move_base_msgs
  actionlib
  message_runtime
  )

#add messages
add_message_files(
  FILES
  string_array.msg
)

#add services
add_service_files(
 FILES
 task_distribution.srv
)

#compile messages and services
generate_messages(
  DEPENDENCIES
  std_msgs
  move_base_msgs 
  verbal_communication
)

#define compilation dependencies
catkin_package(
  CATKIN_DEPENDS std_msgs geometry_msgs rospy message_runtime move_base_msgs actionlib message_generation move_base
)

#install python files into ROS
catkin_install_python(PROGRAMS
  scripts/audio_interface/speech_observer.py
  scripts/audio_interface/speaker.py
  scripts/encoder/encoder.py
  scripts/task_broker/task_repository.py
  scripts/task_templates/move_task.py
  scripts/task_templates/greeting_task.py
  scripts/task_templates/task_distribution/distribution_task_publisher.py
  scripts/task_templates/task_distribution/distribution_task_subscriber.py
  scripts/task_templates/task_distribution/task_execution.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
