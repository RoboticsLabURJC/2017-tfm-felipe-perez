#include "rosPublisher.h"


void rosPublisher::publishPose(float x,float y,float z,float roll, float pitch, float yaw)
{
geometry_msgs::Pose Pose;
std::printf("Publish\n");
std::cout<<"Topic: "<<m_topic<<std::endl;
m = Eigen::AngleAxisf(yaw, Eigen::Vector3f::UnitZ())
* Eigen::AngleAxisf(pitch, Eigen::Vector3f::UnitY())
* Eigen::AngleAxisf(roll, Eigen::Vector3f::UnitX());
Eigen::Quaternionf quatFromRot2(m);
quatFromRot2.normalize();

Pose.position.x=x;
Pose.position.y=y;
Pose.position.z=z;

Pose.orientation.x=quatFromRot2.x();
Pose.orientation.y=quatFromRot2.y();
Pose.orientation.z=quatFromRot2.z();
Pose.orientation.w=quatFromRot2.w();
pub.publish(Pose);



}

void rosPublisher::setTopic(std::string topic)
{	
	
	m_topic =  topic;
	std::cout<<"Topic: "<<m_topic<<std::endl;
	pub = n.advertise <geometry_msgs::Pose> (m_topic, 1);
}
