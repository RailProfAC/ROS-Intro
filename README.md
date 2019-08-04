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

### Plotting

rosrun rqt_plot rqt_plot

### Manual messaging

rostopic pub -r rate-in-hz topic-name message-type message-content
rostopic pub -r 1 /turtle1/cmd_vel geometry_msgs/Twist ’[2, 0, 0]’ ’[0, 0, 0]’

### Console

rosrun rqt_console rqt_console


## Create package

At src:
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]

At ws:
catkin_make
. ~/catkin_ws/devel/setup.bash

## Build package

In a catkin workspace
$ catkin_make [make_targets] [-DCMAKE_VARIABLES=...]