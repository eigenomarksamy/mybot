#! /usr/bin/python


import roslib
import rospy
from sensor_msgs.msg import Imu
import matplotlib.pyplot as plt


def plot():
	global imu_data_list_laccx, imu_data_list_laccy, imu_data_list_laccz, imu_data_list_oriex, imu_data_list_oriey, imu_data_list_oriez, imu_data_list_angvx, imu_data_list_angvy, imu_data_list_angvz, seq_list
	#fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(3, 3)
	fig1, ((ax1, ax2, ax3)) = plt.subplots(3, 1)
	fig2, ((ax4, ax5, ax6)) = plt.subplots(3, 1)
	fig3, ((ax7, ax8, ax9)) = plt.subplots(3, 1)
	ax1.plot(seq_list, imu_data_list_laccx, 'b-', label = 'LinearAccelerationX', linewidth = 1)
	ax1.set_title("LinearAccelerationX")
	#ax1.plot(x_path, y_path, 'g-', label = 'Required Path', linewidth = 2)
	ax2.plot(seq_list, imu_data_list_laccy, 'b-', label = 'LinearAccelerationY', linewidth = 1)
	ax2.set_title("LinearAccelerationY")
	#ax2.plot(time_list, x_path, 'g-', label = 'Required x', linewidth = 2)
	ax3.plot(seq_list, imu_data_list_laccz, 'b-', label = 'LinearAccelerationZ', linewidth = 1)
	ax3.set_title("LinearAccelerationZ")
	#ax3.plot(time_list, y_path, 'g-', label = 'Required y', linewidth = 2)
	ax4.plot(seq_list, imu_data_list_angvx, 'b-', label = 'AngularVelocityX', linewidth = 1)
	ax4.set_title("AngularVelocityX")
	#ax4.plot(time_list, yaw_path, 'g-', label = 'Required yaw', linewidth = 2)
	ax5.plot(seq_list, imu_data_list_angvy, 'b-', label = 'AngularVelocityY', linewidth = 1)
	ax5.set_title("AngularVelocityY")
	ax6.plot(seq_list, imu_data_list_angvz, 'b-', label = 'AngularVelocityZ', linewidth = 1)
	ax6.set_title("AngularVelocityZ")
	ax7.plot(seq_list, imu_data_list_oriex, 'b-', label = 'OrientationX', linewidth = 1)
	ax7.set_title("OrientationX")
	ax8.plot(seq_list, imu_data_list_oriey, 'b-', label = 'OrientationY', linewidth = 1)
	ax8.set_title("OrientationY")
	ax9.plot(seq_list, imu_data_list_oriez, 'b-', label = 'OrientationZ', linewidth = 1)
	ax9.set_title("OrientationZ")
	plt.show()
	while True:
		print "DONE"


def imu_callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]"
    #.format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))
	global imu_data_list_laccx, imu_data_list_laccy, imu_data_list_laccz, imu_data_list_oriex, imu_data_list_oriey, imu_data_list_oriez, imu_data_list_angvx, imu_data_list_angvy, imu_data_list_angvz, seq_list
	#imu_data.append(data)
	seq				= data.header.seq
	imu_data_laccx 	= data.linear_acceleration.x
	imu_data_laccy 	= data.linear_acceleration.y
	imu_data_laccz 	= data.linear_acceleration.z
	imu_data_angvx 	= data.angular_velocity.x
	imu_data_angvy 	= data.angular_velocity.y
	imu_data_angvz 	= data.angular_velocity.z
	imu_data_oriex 	= data.orientation.x
	imu_data_oriey 	= data.orientation.y
	imu_data_oriez 	= data.orientation.z
	if seq < 50:
		seq_list.append(seq)
		imu_data_list_laccx.append(imu_data_laccx)
		imu_data_list_laccy.append(imu_data_laccy)
		imu_data_list_laccz.append(imu_data_laccz)
		imu_data_list_angvx.append(imu_data_angvx)
		imu_data_list_angvy.append(imu_data_angvy)
		imu_data_list_angvz.append(imu_data_angvz)
		imu_data_list_oriex.append(imu_data_oriex)
		imu_data_list_oriey.append(imu_data_oriey)
		imu_data_list_oriez.append(imu_data_oriez)
		print "Sequence: ", 			seq
		print "LinearAcceleration X: ", imu_data_laccx
		print "LinearAcceleration Y: ", imu_data_laccy
		print "LinearAcceleration Z: ", imu_data_laccz
		print "AngularVelocity X:    ", imu_data_angvx
		print "AngularVelocity Y:    ", imu_data_angvy
		print "AngularVelocity Z:    ", imu_data_angvz
		print "Orientation X:        ", imu_data_oriex
		print "Orientation Y:        ", imu_data_oriey
		print "Orientation Z:        ", imu_data_oriez
		print "---------------------------------------"
	else:
		plot()


def listener():
	rospy.init_node('listener', anonymous = True)
	rospy.Subscriber('/imu', Imu , imu_callback) 
	rospy.spin()


if __name__ == '__main__':
    	global imu_data_list_laccx, imu_data_list_laccy, imu_data_list_laccz, imu_data_list_oriex, imu_data_list_oriey, imu_data_list_oriez, imu_data_list_angvx, imu_data_list_angvy, imu_data_list_angvz, seq_list
    #imu_data = []
    	seq_list = []
	imu_data_list_laccx = []
	imu_data_list_laccy = []
	imu_data_list_laccz = []
	imu_data_list_angvx = []
	imu_data_list_angvy = []
	imu_data_list_angvz = []
	imu_data_list_oriex = []
	imu_data_list_oriey = []
	imu_data_list_oriez = []
	seq = 0
    	listener()
