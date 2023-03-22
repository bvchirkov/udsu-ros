# Подъезжаем к стене на роботе

**Общий алгоритм решения**

1) Задаем управляющий сигнал на движение робота к стене (pub, cmd_vel, Twist)
2) Подписываемся на топик /scan
3) Читаем структуру LaserScan
4) 'Вырезаем' из всего массива ranges - нулевой элемент
5) В цикле регулятора сравниваем значение нулевого элемента массива со значением уставки (требуемого расстояния до стены)
6) Если расстояние до стены меньше уставки, отправляем управляющий сигнал на остановку робота


```py
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

rospy.init_node('dalnomer')
target = 0.3
vel = Twist()
pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1)

def callback(scan):
    if scan.ranges[0] > target:
        vel.linear.x = 0.1
    else:
        vel.linear.x = 0
    
    pub.publish(vel)

rospy.Subscriber("/scan", LaserScan, callback)
rospy.spin()
```
