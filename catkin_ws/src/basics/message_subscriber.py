#! /usr/bin/python

import rospy
from basics.msg import Complex

rospy.init_node("message_subscriber")

def callback(msg):
	print ("Real:", msg.real)
	print ("Iaginary", msg.imaginary)
	print

sub = rospy.Subscriber("complex",Complex,callback)

rospy.spin()

