#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

import random

max_count = 80


def controller():
    rospy.init_node('timer_controler')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10) #publisherの設定、turtlesimに向きの情報を渡す

    rate = rospy.Rate(10) #制御周期の設定

    cmd_vel = Twist()
    cmd_vel.linear.x = 2.0
    cmd_vel.angular.z = 0.0

    count = 0
    rotate = 0

    while not rospy.is_shutdown(): #プログラムが終了していないときは無限ループ
        if count <= max_count:
            if not rotate == 0:
                cmd_vel.linear.x = 0.0
                cmd_vel.angular.z = 2.0
                pub.publish(cmd_vel) #cmd_velをpublishする
                rotate = rotate - 1
            count = count + 1
        else:
            count = 0
            rotate = random.randint(1, 10)

        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass
