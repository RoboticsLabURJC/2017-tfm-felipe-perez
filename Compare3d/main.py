import sys
import comm
import config
import signal
from PyQt5.QtWidgets import QApplication
from gui.GUI import MainWindow
from gui.threadgui import ThreadGui

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    cfg = config.load(sys.argv[1])
    path_to_markers = sys.argv[2]
    path_to_result = sys.argv[3]
    if len(sys.argv)>4:
        file_world = sys.argv[4]
    else:
        file_world = None


    # starting comm
    jdrc = comm.init(cfg, "compare3d")
    x = jdrc.getConfig()


    pose_real = jdrc.getPose3dClient("compare3d.Pose3DReal")
    # pose_sim = jdrc.getPose3dClient("compare3d.Pose3DEstimated")

    app = QApplication(sys.argv)
    frame = MainWindow(file_world=file_world,markers=path_to_markers,path=path_to_result)
    # frame.setPose3Dsim(pose_sim)
    frame.setPose3dreal(pose_real)
    topic_name_numMarker=cfg.getProperty("compare3d")["numMarker"]["Topic"]
    frame.set_num_markers_detected(topic_name_numMarker)


    frame.show()

    t2 = ThreadGui(frame)
    t2.daemon = True
    t2.start()

    sys.exit(app.exec_())