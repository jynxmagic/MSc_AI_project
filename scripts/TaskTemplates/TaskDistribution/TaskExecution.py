#! /usr/bin/env python

from array import array
from typing import List
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from verbal_communication.msg import StringArray
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import String

rospy.init_node("task_execution_node")

client = actionlib.SimpleActionClient("move_base", MoveBaseAction)


message_publisher = rospy.Publisher("dispatch_message", String, queue_size=1)
client.wait_for_server() # wait for move_base server to come online
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"



def get_task_list() -> List:  #these location were taken using rviz "publish point" feature and "rostopic echo clicked_point"
    return {
        "YELLOW" : [-0.44509080052375793, 1.486067771911621, -0.001434326171875],
        "GREEN" :  [4.170343399047852, 0.9470973610877991, -0.001434326171875],
        "ORANGE" : [6.318845748901367, -1.5968809127807617, -0.005340576171875],
        "BLUE" : [-0.42593103647232056, 4.4262542724609375, 0.002471923828125],
        "INDIGO" : [4.249742031097412, 3.6765286922454834, -0.0013427734375],
        "VIOLET" : [4.498147487640381, -1.7070852518081665, 0.002532958984375],
    } #x, y, z

def send_to_move_base(location : array) -> bool:
    """Sends a goal to move base to execute.

    Args:
        location (array): [x, y, z] of location on static map

    Returns:
        bool: True if move_base reached goal in given time
    """

    goal.target_pose.pose = Pose(
        Point(location[0], location[1], location[2]),
        Quaternion(0, 0, 0, 1) #Quaternion is required for map transforms
    ) # the goal is actually just a Pose on a map


    client.send_goal(goal)

    result = client.wait_for_result(rospy.Duration(180)) # wait for a maximum of 180 seconds for the robot to reach location

    if result:
        return True
    return False

def execute_tasks(msg: StringArray):
    """ Executes all tasks the robot is assigned to.

    Args:
        msg (StringArray): List of task names
    """

    print("executing tasks: ",msg.data)

    tasks = get_task_list()

    if type(msg.data) is type([]): # StringArray should always be of type [].
        for task in msg.data:
            if task in tasks:
                location = tasks[task]
                success = send_to_move_base(location)
                if(success):
                    message_publisher.publish(String("completed task "+task))
                else:
                    message_publisher.publish(String("failed to complete task "+task))
            else:
                print("could not find task", task)


rospy.Subscriber("execute_tasks", StringArray, execute_tasks)

print("move_base server is launched and task execution is ready")

rospy.spin()
