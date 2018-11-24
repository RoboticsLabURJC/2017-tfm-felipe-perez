from easydict import EasyDict as edict
import matplotlib.pyplot as plt

import numpy as np
import yaml

class trajectory_yml():
    def __init__(self,path):
        with open(path_yml, 'r') as stream:
            self.data = yaml.load(stream)
        self.camera = edict(self.data["camera"])
        self.pose = self.get_trajectory()

    def get_trajectory(self):
        pose = [keyframe["pose"] for keyframe in self.data["keyframes"]]
        pose = np.array([pose]).reshape(-1,7)
        return pose

    def plot_aerial_trajectory(self,markers=False):
        xy = self.pose[:,:2]
        plt.plot(xy[:,0],xy[:,1],"-k")
        if markers:
            for id,xyz in zip(self.id_markers,self.xyz_markers):
                plt.plot(xyz[0],xyz[1],"xk")
                plt.annotate("%d"%(id),xy=tuple(xyz[:2]))
        plt.grid(True)
        plt.show()

    def set_map_marker(self,id_markers,xyz):
        self.id_markers=id_markers
        self.xyz_markers = xyz



if __name__ == '__main__':

    path_yml="/home/f/URJC/2017-tfm-felipe-perez/compareSDvsVisual/exp0/sdslam/trajectory_ROS.yaml"
    path_marker = "/home/f/URJC/2017-tfm-felipe-perez/compareSDvsVisual/exp0/visualmarkers/markers.txt"
    myTrajectory = trajectory_yml(path_yml)
    mymap = markers(path_marker)
    myTrajectory.set_map_marker(mymap.id,mymap.xyz)
    myTrajectory.plot_aerial_trajectory(markers=False)

    print("a")
