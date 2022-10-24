# SKKU ROBOTICS HOMEWORK
## License
[![Build Status](http://build.ros.org/job/Kdev__universal_robot__ubuntu_xenial_amd64/badge/icon)](http://build.ros.org/job/Kdev__universal_robot__ubuntu_xenial_amd64)
[![license - apache 2.0](https://img.shields.io/:license-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.png)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
## Environment

    ubuntu 20.04
    ros noetic
 ###
 [![Download Ros Noetic From Here](https://www.google.com/imgres?imgurl=https%3A%2F%2Fvarhowto.com%2Fwp-content%2Fuploads%2F2020%2F05%2FHow-to-Install-ROS-Noetic-on-Ubuntu-20.04-1200x675.png&imgrefurl=https%3A%2F%2Fvarhowto.com%2Finstall-ros-noetic-ubuntu-20-04%2F&tbnid=D36BFELzJNbpTM&vet=12ahUKEwiE2NmQ4_j6AhVixIsBHesiCjMQMygBegUIARC5AQ..i&docid=yjp9pv185_asFM&w=1200&h=675&q=ros%20noetic&ved=2ahUKEwiE2NmQ4_j6AhVixIsBHesiCjMQMygBegUIARC5AQ)](http://wiki.ros.org/noetic/Installation/Ubuntu)
 

## How to install

### Dependency

    sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-msgs ros-noetic-gazebo-plugins ros-noetic-gazebo-ros-control ros-noetic-rviz ros-noetic-moveit-* ros-noetic-joint-trajectory-controller

## Install package
#### Step 0
    mkdir -p ros_workspace/src
#### Step 1
    cd ~/ros_workspace/src
#### Step 2
    git clone https://github.com/wnsgus-SKKU/SKKU_Robotics_Homework.git
#### Step 3
    cd ~/ros_workspace && catkin_make
#### Step 4
    source ~/ros_workspace/devel/setup.bash

## How to run

### Run simulation

    roslaunch skku_robotics_homework simulator.launch

### Run test

##### goal_joint: target degree each joint (unit: degree)
####
    roslaunch skku_robotics_homework test.launch goal_joint:="0,0,0,0,0,0"

### Run homework

###### position: end-effector's target position  (unit: [x,y,z: m], [roll,pitch,yaw: radian])
####
    roslaunch skku_robotics_homework homework.launch position:="0,0,0,0,0,0"



    

