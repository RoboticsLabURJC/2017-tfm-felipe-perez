import numpy as np
class markers():
    def __init__(self,path):
        lines = open(path).read().splitlines()[1:]
        idxyz = [line.split(" ") for line in lines]
        self.id = np.array(idxyz)[:, 0].astype(np.int)
        self.xyz = np.array(idxyz)[:, 1:4].astype(np.float32)
        self.rpy = np.array(idxyz)[:, 4:].astype(np.float32)
