#!/bin/bash

rm -rf build; mkdir build; cd build
cmake .. \
-DJderobotInterfaces=/opt/jderobot/lib/libJderobotInterfaces.so \
-Dcomm=/opt/jderobot/lib/libcomm.so \
-Djderobotutil=/opt/jderobot/lib/libjderobotutil.so \
-DparallelIce=/opt/jderobot/lib/libparallelIce.so \
-Dcolorspacesmm=/opt/jderobot/lib/libcolorspacesmm.so \
-DxmlParser=/opt/jderobot/lib/libxmlParser.so \
-Dprogeo=/opt/jderobot/lib/libprogeo.so \
-Dconfig=/opt/jderobot/lib/libconfig.so \
-Dlogger=/opt/jderobot/lib/liblogger.so \
-DlibjderobotHandlers=/opt/jderobot/lib/libjderobotHandlers.so \
-DGlog=/usr/lib/x86_64-linux-gnu/libglog.so
-DlibIceStorm=/usr/lib/x86_64-linux-gnu/libIceStorm++11.so.36 \ 
make
