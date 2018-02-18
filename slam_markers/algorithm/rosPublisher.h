#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include "ros/ros.h"
#include <geometry_msgs/Pose.h>
#include <math.h>
#include <eigen3/Eigen/Geometry>





using namespace std;
class rosPublisher {
private:

	ros::NodeHandle n;
	ros::Publisher pub;
	geometry_msgs::Pose pose3d;
	Eigen::Matrix3f m;
	std::string m_topic;

public:
	void setTopic(std::string topic);	
	void publishPose(float x,float y,float z,float roll, float yaw, float pitch);


};
