# Installation
To install this component you have to copy the folder slam_markers and paste in tools from jderobot repository.
After that, you have to compile only the component slam_markers so you have to do:
> $ mkdir build && cd build

> $ cmake -Dbuild-default=OFF -Dbuild_slam_markers=ON ..

> $ make

> $ sudo make install

Then, you have the installed component and you can launch it.

# USAGE
To launch this component you need some files:
- markers.txt: This file contains the pose markers to localizate the robot
- config.yml: This file contains the information to receive the camera information (ICE or ROS topic) and to publish the estimate pose 3d(ICE or ROS topic).
- sim_calib.yml: this file contains the calibration parameters of the camera.
> IMPORTANT: I have calibrated the camera with the fool from jderobot, so if you use other you have to change the names to camera_matrix and distortion_coefficients.

Anyways, to launch the component you have to type:
> $ slam_markers config.yml

Where you launch it, it must contains the files "markers.txt" and "sim_calib.yml".