#! /usr/bin/env python

from typing import List
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal
import actionlib
from verbal_communication.msg import StringArray

rospy.init_node("task_execution_node")

client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
client.wait_for_server()
goal = MoveBaseActionGoal()
#setting some default values for the goal - we only change x/y values
goal.target_pose.header.frame_id = "map"
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.0
goal.target_pose.pose.orientation.w = 0.0

def getTaskList() -> List:
    return {
        "YELLOW" : [1.0, 1.0],
        "GREEN" :  [2.0, 2.0],
        "ORANGE" : [3.0, 3.0],
        "BLUE" : [4.0, 4.0],
        "INDIGO" : [5.0, 5.0],
        "VIOLET" : [6.0, 6.0],
    }

def moveBaseAction(location) -> bool:
    goal.target_pose.pose.position.x = location[0]
    goal.target_pose.pose.position.y = location[1]

    client.send_goal(goal)

    result = client.wait_for_result(rospy.Duration(50)) # give the robot 50 seconds to reach goal

    if result:
        return True
    return False

def executeTask(msg):
    tasks = getTaskList()

    if type(msg.data) is type([]):
        for task in msg.data:
            if task in tasks:
                location = tasks[task]
                success = MoveBaseAction(location)
                if(success):
                    print("completed task", task)
                else:
                    print("failed to complete task", task)
            else:
                print("could not find task", task)


rospy.Subscriber("execute_tasks", StringArray, executeTask)

rospy.spin()
