#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include "ros/ros.h"
#include <geometry_msgs/Pose.h>
#include <math.h>
#include <eigen3/Eigen/Geometry>
#include <jderobot/pose3d.h>
#include "geometryutils.h"





using namespace std;
class rosPublisher {
private:

	ros::NodeHandle n;
	ros::Publisher pub;
	ros::Publisher pub_;
	geometry_msgs::Pose pose3d;
	Eigen::Matrix3f m;
	std::string m_topic;

public:
	rosPublisher(const std::string& topic);
	void setTopic(std::string topic);	
	void publishPose(float x,float y,float z,float roll, float yaw, float pitch);
	void setPose(const Ardrone::Pose p);
	void setPublisher(ros::Publisher pub);

};
