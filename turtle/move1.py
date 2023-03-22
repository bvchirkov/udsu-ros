import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rospy.init_node('bvchirkov_move_turtle_node')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

def callback_regulator(msg: Pose):
    vel = Twist()
    if msg.x >= 7:
        vel.linear.x = 0
    else:
        vel.linear.x = 0.1
    
    pub.publish(vel)

rospy.Subscriber('/turtle1/pose', Pose, callback_regulator)
rospy.spin()