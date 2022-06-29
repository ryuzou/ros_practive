#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

pose = Pose()
nowRotating = False #回転中フラグ、真の場合は向きを変えている

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y

def update_cmd_vel(cmd_vel):   #向きを変える処理
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
    pub = rospy.Publisher('#　穴抜け1 cmd_velをpublishするための設定用コード #', Twist, queue_size=10) #publisherの設定
    sub = rospy.Subscriber('pose', Pose, update_pose) #subscriberの設定

    rate = rospy.Rate(10) #制御周期の設定

    cmd_vel = Twist()
    cmd_vel.linear.x = 2.0
    cmd_vel.angular.z = 0.0

    while not rospy.is_shutdown():
        cmd_vel = update_cmd_vel(cmd_vel)
        #　穴抜け2 cmd_velをpublishするためのコード # #cmd_velをpublishする
        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass
