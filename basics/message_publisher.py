#! /usr/bin/env python

import rospy
from basics.msg import Complex
from random import random

rospy.init_node('message_publisher')
pub = rospy.Publisher("complex",Complex,queue_size=10,latch=True)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
	msg = Complex()
	msg.real = random()
	msg.imaginary = random()
	pub.publish(msg)
	rate.sleep()
