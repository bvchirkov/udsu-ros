import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleMover():
    def __init__(self) -> None:
        self.pose = Pose()
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/turtle1/pose', Pose, self.callback)
    
    def callback(self, pose:Pose) -> None:
        self.pose = pose

    def move(self) -> None:
        vel = Twist()

        if self.pose.x >= 7:
            vel.linear.x = 0
        else:
            vel.linear.x = 1
        
        self.pub.publish(vel)

if __name__ == "__main__":
    rospy.init_node('turtle_move_node')
    tm = TurtleMover()

    while not rospy.is_shutdown():
        tm.move()
