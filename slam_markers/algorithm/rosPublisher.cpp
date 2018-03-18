#include "rosPublisher.h"

rosPublisher::rosPublisher(const std::string& topic)
{
	//std::cout<<"Constructor"<<std::endl;
	pub_ = n.advertise <geometry_msgs::Pose> (topic, 1);
	std::cout<<"just do it"<<std::endl;
}
void rosPublisher::publishPose(float x,float y,float z,float roll, float pitch, float yaw)
{
geometry_msgs::Pose Pose;


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
pub_.publish(Pose);



}

void rosPublisher::setTopic(std::string topic)
{	
	
	std::cout<<"RosPublisher topic: "<<topic<<std::endl;
	pub = n.advertise <geometry_msgs::Pose> (topic, 1);
	std::cout<<"Incializado"<<std::endl;
}


void rosPublisher::setPublisher(ros::Publisher pub)
{

	std::cout<<"setPubliser"<<std::endl;
	pub_ = pub;
	std::cout<<"Publisher conected"<<std::endl; 
}

void rosPublisher::setPose(const Ardrone::Pose p)
{
geometry_msgs::Pose Pose;


m = Eigen::AngleAxisf(p.GetYaw(), Eigen::Vector3f::UnitZ())
* Eigen::AngleAxisf(p.GetPitch(), Eigen::Vector3f::UnitY())
* Eigen::AngleAxisf(p.GetRoll(), Eigen::Vector3f::UnitX());
Eigen::Quaternionf quatFromRot2(m);
quatFromRot2.normalize();

Pose.position.x=p.GetX();
Pose.position.y=p.GetY();
Pose.position.z=p.GetZ();


Pose.orientation.x=quatFromRot2.x();
Pose.orientation.y=quatFromRot2.y();
Pose.orientation.z=quatFromRot2.z();
Pose.orientation.w=quatFromRot2.w();
pub_.publish(Pose);

}
