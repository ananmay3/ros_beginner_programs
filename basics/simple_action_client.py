#! /usr/bin/python

import actionlib
import rospy
from basics.msg import TimerGoal, TimerResult, TimerAction

rospy.init_node("simple_action_client")
client = actionlib.SimpleActionClient('timer',TimerAction)
client.wait_for_server()
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal)
client.wait_for_result()
print('Time Elapsed: %f' %(client.get_result().time_elapsed.to_sec()))
