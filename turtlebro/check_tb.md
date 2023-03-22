# Проверка робота

**Проверка батареи**. Вывод напряжения батареи в топике: `rostopic echo /bat -n 1`

**Проверка Лидара**. Облако точек лидара в топике:` rostopic echo /scan -n 1`

**Проверка одометрии колес**. В первом терминале: Команда: `rostopic echo /odom`

В другом терминале команды: 
```
rostopic pub -1 /cmd_vel geometry_msgs/Twist (x = 0.05)
rostopic pub -1 /cmd_vel geometry_msgs/Twist (x = -0.05)
rostopic pub -1 /cmd_vel geometry_msgs/Twist (x = 0; z = 0.5)
rostopic pub -1 /cmd_vel geometry_msgs/Twist (x = 0; z = -0.5)
```

**Проверка IMU датчика**. Данные IMU датчика в консоли: `rostopic echo /imu -n 1`
