#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String


task_name="movement"
topic_name="decoded_message"

rospy.init_node(task_name)

cmd_vel_publisher = rospy.Publisher("cmd_vel", Twist, queue_size=1)

def get_task_list() -> dict:
    """Returns a list of availble tasks to the robot.

    Returns:
        dict: dict mapping strings to search for against functions to run.
    """
    return {
        "MOVE FORWARD" : move_forward,
        "STOP" : stop,
        "ROTATE LEFT" : rotate_left,
        "ROTATE RIGHT" : rotate_right 
    }

def listener_callback(msg : String):
    """Searches for the task of a provided string and executes it.

    Args:
        msg (std_msgs/String): Task to search for
    """
    msg.data = msg.data.strip()
    if msg.data in [*get_task_list().keys()]:
        get_task_list()[msg.data]()
    else:
        print("Couldn't find task ", msg.data)
    return

def move_forward():
    """Moves the robot forward."""
    message = Twist()
    message.linear.x = 0.3
    cmd_vel_publisher.publish(message)

def stop():
    """Stops the robot."""
    message = Twist()
    message.linear.x=0
    message.linear.y=0
    message.linear.z=0
    message.angular.x=0
    message.angular.y=0
    message.angular.z=0
    cmd_vel_publisher.publish(message)

def rotate_left():
    """Makes the robot rotate left."""
    message = Twist()
    message.angular.z = 0.3
    cmd_vel_publisher.publish(message)

def rotate_right():
    """Makes the robot rotate right."""
    message = Twist()
    message.angular.z = -0.3
    cmd_vel_publisher.publish(message)


rospy.Subscriber(topic_name, String, listener_callback)

    
rospy.spin()
