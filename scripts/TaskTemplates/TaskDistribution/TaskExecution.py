#! /usr/bin/env python

from email import message
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
#while not client.wait_for_server(rospy.Duration(5)): # wait for the server to come online
#    print("waiting for move base server")

client.wait_for_server()
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"



def getTaskList() -> List:
    return {
        "YELLOW" : [-0.44509080052375793, 1.486067771911621, -0.001434326171875], #these location were taken using rviz "publish point" feature and "rostopic echo clicked_point"
        "GREEN" :  [4.170343399047852, 0.9470973610877991, -0.001434326171875],
        "ORANGE" : [6.318845748901367, -1.5968809127807617, -0.005340576171875],
        "BLUE" : [-0.42593103647232056, 4.4262542724609375, 0.002471923828125],
        "INDIGO" : [4.249742031097412, 3.6765286922454834, -0.0013427734375],
        "VIOLET" : [4.498147487640381, -1.7070852518081665, 0.002532958984375],
    } #x, y, z

def sendToMoveBase(location) -> bool:

    goal.target_pose.pose = Pose(Point(location[0], location[1], location[2]), Quaternion(0, 0, 0, 1)) # the goal is actually just a Pose on a map


    client.send_goal(goal)

    result = client.wait_for_result(rospy.Duration(120)) # wait for a maximum of 120 seconds for the robot to reach location

    if result:
        return True
    return False

def executeTask(msg):
    print("executing tasks, ",msg.data)

    tasks = getTaskList()

    if type(msg.data) is type([]):
        for task in msg.data:
            if task in tasks:
                location = tasks[task]
                success = sendToMoveBase(location)
                if(success):
                    message_publisher.publish(String("completed task "+task))
                else:
                    message_publisher.publish(String("failed to complete task "+task))
            else:
                print("could not find task", task)


rospy.Subscriber("execute_tasks", StringArray, executeTask)

print("move_base server is launched and task execution is ready")

rospy.spin()
