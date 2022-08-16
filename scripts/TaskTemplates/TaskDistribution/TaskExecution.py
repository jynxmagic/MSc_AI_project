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
        "ORANGE" : [6.318845748901367, -1.5968809127807617, -0.005340576171875]
        #"BLUE" : [-0.6246927380561829, 4.903703212738037, -0.0052490234375],
        #"INDIGO" : [4.249742031097412, 4.784639835357666, -0.001434326171875],
        #"VIOLET" : [3.854705572128296, 1.510190725326538, -0.009246826171875],
    } #x, y, z

def sendToMoveBase(location) -> bool:

    goal.target_pose.pose = Pose(Point(location[0], location[1], location[2]), Quaternion(0, 0, 0, 1)) # the goal is actually just a Pose on a map


    client.send_goal(goal)

    result = client.wait_for_result(rospy.Duration(50)) # give the robot 50 seconds to reach goal

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
