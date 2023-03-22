import rospy
from std_msgs.msg import String

rospy.init_node('udsu_ros_node_sub')

def callback(data: String):
    print(data)

sub = rospy.Subscriber('udsu_ros_topic', String, callback)

rospy.spin()