#! /usr/bin/python

import rospy
import actionlib
from basics.msg import TimerAction, TimerResult, TimerGoal, TimerFeedback
import time

rospy.init_node("fancy_server")

def do_timer(goal):
	start_time = time.time()
	updates_count = 0
	
	if goal.time_to_wait.to_sec() > 60:
		result = TimerResult()
		result.updates_sent = updates_count
		result.time_elapsed = \
			rospy.Duration.from_sec(time.time() - start_time)
		server.set_aborted(result, "Goal Time is too high")
		return

	while time.time() <= start_time + goal.time_to_wait.to_sec():
		if server.is_preempt_requested():
			result = TimerResult()
			result.time_elapsed = \
				rospy.Duration.from_sec(time.time() - 
								start_time)
			result.updates_sent = updates_count
			server.set_preempted(result,"Timer Preempted")
			return
		feedback = TimerFeedback()
		feedback.time_elapsed = \
			rospy.Duration.from_sec(time.time() - start_time)
		feedback.time_remaining = (goal.time_to_wait -
							feedback.time_elapsed)
		server.publish_feedback(feedback)
		updates_count += 1
		
		time.sleep(1.0)
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
	result.updates_sent = updates_count
	server.set_succeeded(result,"Timer completed successfully")
	
server = actionlib.SimpleActionServer('timer',TimerAction,do_timer,False)
server.start()
rospy.spin()
