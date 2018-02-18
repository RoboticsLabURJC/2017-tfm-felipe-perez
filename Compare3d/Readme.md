# USAGE:
## Simulation:
- First, you have to launch the world (AprilTags_kobuki.world):
> $ gazebo AprilTags_kobuki.world
- Second, you have to launch your algorithm to localizate:
> $ slam_markers config.yml
- Third, launch the visualization tool to view the information:
> python2 ./main path_to_config.yml path_to_markers.txt path_to_gazebo.world






