#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

pose = Pose()
nowRotating = False #if true rotate

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y

def update_cmd_vel(cmd_vel): 
    global nowRotating
    boundary = 1.0
    if (pose.x < boundary or pose.x > 11.08-boundary or pose.y < boundary or pose.y > 11.08-boundary) and not nowRotating:
        cmd_vel.linear.x = 0.0
        cmd_vel.angular.z = 2.0
        nowRotating = True
    else:
        cmd_vel.linear.x = 2.0
        cmd_vel.angular.z = 0.0
        nowRotating = False
    return cmd_vel

def controller():
    rospy.init_node('turtlesim_controller')
    pub = rospy.Publisher('# write your code here 1#', Twist, queue_size=10) #publisher settings 
    sub = rospy.Subscriber('pose', Pose, update_pose) #subscriber settings

    rate = rospy.Rate(10) #rate of computing

    cmd_vel = Twist()
    cmd_vel.linear.x = 2.0
    cmd_vel.angular.z = 0.0

    while not rospy.is_shutdown():
        cmd_vel = update_cmd_vel(cmd_vel)
        ## write your code here 2# #publish cmd=vel
        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass
