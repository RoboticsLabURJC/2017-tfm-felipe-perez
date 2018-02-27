# USAGE:
## Experiments:
### Experiment 0 (ICE)


- First, you have to launch the world (AprilTags_kobuki.world):
> $ gazebo AprilTags_kobuki.world
- Second, you have to launch your algorithm to localizate:
> $ slam_markers path_to_configuration.yml sim_calib.yml
- Third, launch the visualization tool to view the information:
> python2 ./main path_to_config.yml path_to_markers.txt path_to_gazebo.world



### Experiment 1 (ROS)


- First, you have to launch the world (AprilTags_kobukiROS.world):
> (gazebo folder) $ roslaunch AprilTags_kobuki_ROS.launch
- Second, you have to launch your algorithm to localizate:
> (files2visualmarkers) $ slam_markers path_to_configuration.yml sim_calib.yml
- Third, launch the visualization tool to view the information:
> (compare3d) $ python2 ./../../../Compare3d/main.py config_ROS.yml ../files2visualmarkers/markers.txt  ../result ../gazebo/AprilTags_kobuki_ROS.world

or

> (compare3d) $ ./Compare.sh
- Finally, you have to launch kobukiViewer to move the robot:
> (kobukiViewer) $ kobukiViewer kobukiViewerROS.yml


When you finish the expirement, if you would have saved the data with the bottom, you will be able to plot the information with plot_data.py


