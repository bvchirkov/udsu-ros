# Робот лазерный дальномер

**Общий алгоритм**
1) Подписываемся на топик /scan
2) Читаем структуру LaserScan
3) 'Вырезаем' из всего массива ranges - нулевой элемент
4) Выводим значение расстояния в нулевом элементе на экран

**Пример решения**
```python
import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('udsu_ros_rangefinder')

def callback(scan):
    print(scan.ranges[0])

rospy.Subscriber("/scan", LaserScan, callback)
rospy.spin()
```
