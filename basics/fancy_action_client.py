#! /usr/bin/python

import rospy
from basics.msg import TimerAction, TimerGoal
import actionlib

rospy.init_node("fancy_client")

def feedback(fb):
	print('[FB] Time Elapsed: %f' %fb.time_elapsed.to_sec())
	print('[FB] Time Remaining: %f' %fb.time_remaining.to_sec())

client = \
	actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal, feedback_cb = feedback)

client.wait_for_result()
result = client.get_result()
print("[RT] Time Elapsed: %f" %result.time_elapsed.to_sec())
print('[RT] Updates Sent: %f' %result.updates_sent)
print('[RT] State: %f' %client.get_state())
print('[RT] Status: %s' %client.get_goal_status_text())
	 
