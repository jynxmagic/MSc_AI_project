#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include "std_msgs/String.h"

typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

void objectiveRecieved(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("message recieved was %s", msg->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "task_execution_node");

    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("execute_task", 1, objectiveRecieved);

    ros::spin();

    return 0;
}