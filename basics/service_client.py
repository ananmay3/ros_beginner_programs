#! /usr/bin/python

import rospy
from basics.srv import WordCount
import sys

rospy.init_node("service_client")

while True:
	rospy.wait_for_service("word_count")
	word_counter = rospy.ServiceProxy('word_count',WordCount)
	words = raw_input("Enter a sentence: ")
	print(word_counter(words))

rospy.spin()

