#!/usr/bin/env python

import rospy
import roslib
import tf
import math

from geometry_msgs.msg import PoseArray
round_list = []

#Defining a class
class Marker_detect():

	def __init__(self):
		rospy.init_node('marker_detection',anonymous=False) # initializing a ros node with name marker_detection

		self.whycon_marker = {}	# Declaring dictionaries

		rospy.Subscriber('/whycon/poses',PoseArray,self.whycon_data)	# Subscribing to topic

	# Callback for /whycon/poses
	# Please fill in the function
	def whycon_data(self,msg):
		#print(msg.poses[0].position.x)
		len_target = len(msg.poses)
		for i in range(len_target):

			round_list.append([round(msg.poses[i].position.x,3),round(msg.poses[i].position.y,3),round(msg.poses[i].position.z,3)])

		for i in range(len_target):
			self.whycon_marker[i] = round_list[i]

		print(self.whycon_marker)



if __name__=="__main__":
	marker = Marker_detect()
	while not rospy.is_shutdown():
		rospy.spin()
