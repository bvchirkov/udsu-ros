import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import math

class TurtleMover():
    def __init__(self) -> None:
        self.pose = None
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/turtle1/pose', Pose, self.callback_handler)
        self.rate = rospy.Rate(10)

    def callback_handler(self, pose:Pose) -> None:
        self.pose = pose

    def wait_turtle(self):
        while self.pose is None:
            rospy.loginfo('Wait turtle (getting Pose)')
            self.rate.sleep()
    
    def move_forward(self, dist):
        start_pose = self.pose
        move_dist = 0
        cmd_vel = Twist()

        while not rospy.is_shutdown():
            move_dist = math.sqrt((start_pose.x - self.pose.x)**2 + (start_pose.y - self.pose.y)**2)
            rospy.loginfo(f"Dist :{move_dist}")
            if (move_dist < dist):
                cmd_vel.linear.x = 1
                self.pub.publish(cmd_vel)
                self.rate.sleep()
            else:
                cmd_vel.linear.x = 0
                self.pub.publish(cmd_vel)
                break
   
    def turn(self, angle):
        start_pose = self.pose
        move_angle = 0
        cmd_vel = Twist()
    
        while not rospy.is_shutdown():
            move_angle = abs(math.degrees(start_pose.theta - self.pose.theta))
            rospy.loginfo(f"It remains to turn: {move_angle}, Start angle: {start_pose.theta}, Current angle: {self.pose.theta}")
            if (move_angle < angle):
                cmd_vel.angular.z = 0.1
                self.pub.publish(cmd_vel)
                self.rate.sleep()
            else:
                cmd_vel.angular.z = 0
                self.pub.publish(cmd_vel)
                break

if __name__ == "__main__":
    rospy.init_node('turtle_rect_node')
    turtle = TurtleMover()
    turtle.wait_turtle()

    while not rospy.is_shutdown():
        turtle.move_forward(2)
        turtle.turn(90)