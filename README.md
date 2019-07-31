# ROS-Intro

## Start turtlesim

roscore
rosrun turtlesim turtlesim_node 
rosrun turtlesim turtle_teleop_key

## Topics

rostopic list
rostopic echo topic-name

### Measuring

rostopic hz topic-name 
rostopic bw topic-name

### Manual messaging

rostopic pub -r rate-in-hz topic-name message-type message-content
rostopic pub -r 1 /turtle1/cmd_vel geometry_msgs/Twist ’[2, 0, 0]’ ’[0, 0, 0]’
