#!/usr/bin/env python
import rospy
from std_msgs.msg import Int8,Float64
import time

class suscriber():
    def __init__(self):
        self.numMarker_sub = rospy.Subscriber("/visual_slam/numMarker", Int8, self.callback_int)
        self.time_sub = rospy.Subscriber("/visual_slam/time", Float64, self.callback_float)


    def callback_int(self,data):
        print "numMarker:",data.data
    def callback_float(self,data):
        print "Time: ",time.ctime(data.data)





if __name__ == '__main__':
    rospy.init_node('suscriber', anonymous=True)
    mySuscriber = suscriber()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
