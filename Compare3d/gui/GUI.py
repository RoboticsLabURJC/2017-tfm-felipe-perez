from PyQt5.QtWidgets import QWidget, QCheckBox, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from std_msgs.msg import Int8
from widgetplot import MyDynamicMplCanvas
from jderobotTypes.pose3d import Pose3d
from plotWall import loadWorld
from utils.markers import markers
from geometry_msgs.msg import Pose
import jderobot
import numpy as np
import os
import rospy


class MainWindow(QWidget):
    updGUI = pyqtSignal()

    def __init__(self, file_world, markers="markers.txt", path="result", ):

        super(MainWindow, self).__init__()
        self.updGUI.connect(self.updateGUI)
        ### initialize
        self.filename = markers
        self.path_result = path
        self.file_world = file_world
        self.loadmarkers()
        self.loadworld()

        self.pose3dsim_list = []
        self.pose3dreal_list = []
        self.pose3dError_list = []
        rospy.Subscriber("/visual_slam/pose", Pose, self.callback_pose)

        self.initUI()
        self.myplot()

    def initUI(self):

        ### Text out
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 480 + 10)
        self.textbox.resize(640, 80)

        ### To select a different graph
        self.showNow = "showXYZ"

        ## XYZ
        self.cbxyz = QCheckBox('Show XYZ', self)
        self.cbxyz.move(640 + 40, 100)
        self.cbxyz.toggle()
        self.cbxyz.setChecked(True)
        self.cbxyz.stateChanged.connect(self.showXYZ)

        ## RPY
        self.cbRPY = QCheckBox('Show RPY', self)
        self.cbRPY.move(640 + 40, 200)
        self.cbRPY.toggle()
        self.cbRPY.setChecked(False)
        self.cbRPY.stateChanged.connect(self.showRPY)

        ## Error
        self.cbErrorXYZ = QCheckBox('Show ErrorXYZ', self)
        self.cbErrorXYZ.move(640 + 40, 300)
        self.cbErrorXYZ.toggle()
        self.cbErrorXYZ.setChecked(False)
        self.cbErrorXYZ.stateChanged.connect(self.showErrorXYZ)

        ## Error
        self.cbErrorRPY = QCheckBox('Show ErrorRPY', self)
        self.cbErrorRPY.move(640 + 40, 400)
        self.cbErrorRPY.toggle()
        self.cbErrorRPY.setChecked(False)
        self.cbErrorRPY.stateChanged.connect(self.showErrorRPY)

        ### Saving results
        ButtonSave = QPushButton('Save results', self)
        ButtonSave.setCheckable(True)
        ButtonSave.move(640 + 50, 480 + 30)
        ButtonSave.clicked[bool].connect(self.savingResult)

        self.setGeometry(600, 600, 250, 150)
        self.setWindowTitle('Compare')
        self.setFixedSize(10 + 640 + 20 + 150, 600)

    def myplot(self):
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        self.dc = MyDynamicMplCanvas(parent=self.main_widget, option=self.showNow,
                                     map=self.map, id_markers=self.id_markers,
                                     world=self.world,rpy_map=self.rpy_markers,
                                     pose_est=self.pose3dsim_list,
                                     pose_real=self.pose3dreal_list,
                                     pose_error=self.pose3dError_list)
        l.addWidget(self.dc)

    def showXYZ(self, state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show XYZ graph")
            self.showNow = "showXYZ"
            self.dc.setOption(self.showNow)

            self.cbRPY.setChecked(False)
            self.cbErrorXYZ.setChecked(False)
            self.cbErrorRPY.setChecked(False)

    def showRPY(self, state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show RPY graph")
            self.showNow = "showRPY"
            self.cbxyz.setChecked(False)
            self.cbErrorRPY.setChecked(False)
            self.cbErrorXYZ.setChecked(False)
            self.dc.setOption(self.showNow)

    def showErrorXYZ(self, state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show error XYZ graph")
            self.showNow = "showErrorXYZ"
            self.dc.setOption(self.showNow)
            self.cbxyz.setChecked(False)
            self.cbRPY.setChecked(False)
            self.cbErrorRPY.setChecked(False)

    def showErrorRPY(self, state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show error RPY graph")
            self.showNow = "showErrorRPY"
            self.dc.setOption(self.showNow)
            self.cbxyz.setChecked(False)
            self.cbRPY.setChecked(False)
            self.cbErrorXYZ.setChecked(False)

    def savingResult(self):
        self.textbox.setText("Saving result...")
        if not os.path.exists(self.path_result):
            os.mkdir(self.path_result)

        np.save(os.path.join(self.path_result, "pose3dreal_list.npy"), self.pose3dreal_list)
        np.save(os.path.join(self.path_result, "pose3dsim_list.npy"), self.pose3dsim_list)
        np.save(os.path.join(self.path_result, "pose3dError_list.npy"), self.pose3dError_list)
        self.textbox.setText("Done!")
    #
    # def setPose3Dsim(self, pose):
    #     self.pose3dEstimated_client = pose

    def setPose3dreal(self, pose):
        self.pose3dReal_client = pose

    def set_num_markers_detected(self, topic_name):
        self.numMarker_sub = rospy.Subscriber(topic_name, Int8, self.callback_int)

    def callback_int(self, data):
        self.numMarker = data.data
        self.textbox.setText("Number of detected markers : %d" % (int(self.numMarker)))

    def callback_pose(self,data):
        pose3dsim_ros = data
        self.pose3dsim = Pose3d()
        self.pose3dsim.x = pose3dsim_ros.position.x
        self.pose3dsim.y = pose3dsim_ros.position.y
        self.pose3dsim.z = pose3dsim_ros.position.z

        self.pose3dsim.q[0] = pose3dsim_ros.orientation.x
        self.pose3dsim.q[1] = pose3dsim_ros.orientation.y
        self.pose3dsim.q[2] = pose3dsim_ros.orientation.z
        self.pose3dsim.q[3] = pose3dsim_ros.orientation.w

        self.pose3dsim_list.append(self.pose3dsim)
        self.pose3dError = MainWindow.getError(self, poseReal=self.pose3dReal, poseEst=self.pose3dsim)
        self.pose3dError_list.append(self.pose3dError)



    def updateGUI(self):
        self.pose3dReal = self.pose3dReal_client.getPose3d()
        self.pose3dreal_list.append(self.pose3dReal)


    def getError(self, poseReal, poseEst):
        poseError = Pose3d()
        poseError.x = abs(poseReal.x - poseEst.x)
        poseError.y = abs(poseReal.y - poseEst.y)
        poseError.z = abs(poseReal.z - poseEst.z)

        poseError.yaw = abs(poseReal.yaw - poseEst.yaw)
        poseError.roll = abs(poseReal.roll - poseEst.roll)
        poseError.pitch = abs(poseReal.pitch - poseEst.pitch)
        return poseError

    def loadmarkers(self):
        list_pose = []
        mymap = markers(self.filename)
        self.id_markers = mymap.id
        for xyz in mymap.xyz:
            pose = jderobot.Pose3DData()
            pose.x = xyz[0]
            pose.y = xyz[1]
            pose.z = xyz[2]
            list_pose.append(pose)
        self.map = list(list_pose)
        self.rpy_markers = mymap.rpy

    def loadworld(self):
        if self.file_world:
            self.world = loadWorld(path=self.file_world)
        else:
            self.world = None






