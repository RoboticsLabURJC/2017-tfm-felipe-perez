#include <QApplication>
#include "mainwindow.h"
#include <Ice/Ice.h>
#include <IceUtil/IceUtil.h>
#include "threadgui.h"
#include "sensors.h"
#include "threadsensors.h"
#include "pose3di.h"
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <gtkmm.h>
#include <gtkglmm.h>
#include <gdkglmm.h>
#include <iostream>

#include "jderobot/config/config.h"
#include "jderobot/comm/communicator.hpp"
#include <ros/ros.h>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    Ice::CommunicatorPtr ic;
	ros::init(argc, argv, "slam_markers");
    try
    {	
		//-----------------Comm----------------//
		Config::Properties props = Config::load(argc, argv);	
        Comm::Communicator* jdrc = new Comm::Communicator(props);

		int serverPose=props.asInt("CamAutoloc.Pose3D.Server");
		std::string topic = props.asString("CamAutoloc.Pose3D.Topic");
		std::cout<<"Topic: "<<topic<<std::endl;
		

		


        Sensors* sensors = new Sensors(jdrc);
        threadGUI* gui = new threadGUI(sensors,serverPose,topic);
        ThreadSensors* threadSensors = new ThreadSensors(sensors);

        threadSensors->start();
        gui->start();
		
		// Publish Pose3d with ICE
		if (serverPose==1)
		{
		ic = Ice::initialize(argc, argv);
		
        std::string endpoint = props.asString("CamAutoloc.Pose3D.Proxy");


        Ice::ObjectAdapterPtr adapter = ic->createObjectAdapterWithEndpoints("Pose3D", endpoint);
        Ice::ObjectPtr object = new Pose3DI();
        adapter->add(object, ic->stringToIdentity("Pose3D"));
        adapter->activate();
        //ic->waitForShutdown();
		}
    }
    catch(const Ice::Exception& ex)
    {
        std::cerr << ex << std::endl;
        exit(-1);
    }
    catch (const char* msg)
    {
        std::cerr << msg << std::endl;
        exit(-1);
    }


    return a.exec();
}
