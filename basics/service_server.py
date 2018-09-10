#! /usr/bin/python

import rospy
from basics.srv import WordCount, WordCountResponse

rospy.init_node("service_server")

def count_words(request):
	return WordCountResponse(len(request.words.split()))

service = rospy.Service('word_count',WordCount,count_words)

rospy.spin()
