#ifndef THREADGUI_H
#define THREADGUI_H

#include <iostream>
#include <sys/time.h>
#include "mainwindow.h"
#include "sensors.h"


#define cycle_gui 70 //miliseconds

class threadGUI : public QThread
{
public:
    threadGUI(Sensors* sensors, int option, std::string topic);

private:
    MainWindow* gui;
    Sensors* sensors;
	int option;
	std::string topic;

protected:
    void run();
};

#endif // THREADGUI_H