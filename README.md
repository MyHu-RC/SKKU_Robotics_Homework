# SKKU ROBOTICS HOMEWORK

## Environment

    ubuntu 20.04
    ros noetic

## How to install

### Dependency

    $ sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-msgs ros-noetic-gazebo-plugins ros-noetic-gazebo-ros-control ros-noetic-rviz ros-noetic-moveit-* ros-noetic-joint-trajectory-controller

### Install package

    $ cd $(ros_workspace)/src
    $ git clone https://github.com/wnsgus-SKKU/SKKU_Robotics_Homework.git
    $ cd $(ros_workspace) && catkin_make
    $ source $(ros_workspace)/devel.setup.bash

## How to run

### Run simulation

    $ roslaunch skku_robotics_homework simulator.launch

### Run test

    # goal_joint: target degree each joint (unit: degree)
    $ roslaunch skku_robotics_homework test.launch goal_joint:="0,0,0,0,0,0"

### Run homework

    # position: end-effector's target position  (unit: [x,y,z: m], [roll,pitch,yaw: radian])
    $ roslaunch skku_robotics_homework homework.launch position:="0,0,0,0,0,0"



    

