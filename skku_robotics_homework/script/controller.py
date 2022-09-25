#!/usr/bin/python3
import rospy
import numpy as np
from moveit_msgs.msg import MoveGroupAction
from moveit_msgs.msg import MoveGroupGoal
from moveit_msgs.msg import MotionPlanRequest
from moveit_msgs.msg import WorkspaceParameters
from moveit_msgs.msg import Constraints
from moveit_msgs.msg import JointConstraint
import actionlib

class Controller:
    def __init__(self):
        self.__setAction__()
        self.dof = 6
        self.joint_name = ["shoulder_pan_joint",\
                           "shoulder_lift_joint",\
                           "elbow_joint",\
                           "wrist_1_joint",\
                           "wrist_2_joint",\
                           "wrist_3_joint"]
                    

    def __setGoal__(self,radians):
        goal = MoveGroupGoal()

        # set workspace parameters
        workspace_parameters = WorkspaceParameters()
        workspace_parameters.min_corner.x = -1.0
        workspace_parameters.min_corner.y = -1.0
        workspace_parameters.min_corner.z = -1.0
        workspace_parameters.max_corner.x = 1.0
        workspace_parameters.max_corner.y = 1.0
        workspace_parameters.max_corner.z = 1.0

        # set goal_constraints
        goal_constraints = Constraints()
        for index in range(self.dof):
            joint_contraint = JointConstraint()
            joint_contraint.joint_name = self.joint_name[index]
            joint_contraint.position = radians[index]
            joint_contraint.tolerance_above = 0.0001
            joint_contraint.tolerance_below = 0.0001
            joint_contraint.weight = 1.0
            goal_constraints.joint_constraints.append(joint_contraint)

        goal.request.workspace_parameters = workspace_parameters
        goal.request.goal_constraints = [goal_constraints]
        goal.request.group_name = "manipulator"
        goal.request.num_planning_attempts = 10
        goal.request.allowed_planning_time = 5.0
        goal.request.max_velocity_scaling_factor = 0.1
        goal.request.max_acceleration_scaling_factor = 0.1
        goal.request.max_cartesian_speed = 0

        return goal

    def __setAction__(self):
        self.client = actionlib.SimpleActionClient('move_group', MoveGroupAction)

    def control(self,radians):
        self.client.wait_for_server()
        goal = self.__setGoal__(radians)
        self.client.send_goal(goal)
        self.client.wait_for_result()
        return self.client.get_result()

    def toRadinan(self,degree):
        return np.radians(degree)

    def toDegree(self,radian):
        return np.rad2deg(radian)




if __name__ == '__main__':
    rospy.init_node('controller')
    controller = Controller()

    goal_joint = rospy.get_param("~goal_joint")
    goal_joint = goal_joint.split(",")
    for index in range(len(goal_joint)):
        goal_joint[index] = float(goal_joint[index])

    rospy.loginfo("[skku_robotics_homework] set joint: {}".format(goal_joint))
    controller.control(controller.toRadinan(goal_joint))