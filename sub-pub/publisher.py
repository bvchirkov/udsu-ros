import rospy
from std_msgs.msg import String

rospy.init_node("udsu_ros_node_pub")
pub = rospy.Publisher("udsu_ros_topic", String, queue_size=10)

r = rospy.Rate(10)
s = String()
s.data = 'Hello, user!'

while not rospy.is_shutdown():
    pub.publish(s)
    r.sleep()