import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class LookingAtNode(ArmLogicTreeNode):
    """Looking at Node"""
    bl_idname = 'LNLookingAtNode'
    bl_label = 'Looking At'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'transform'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('NodeSocketVector', 'From Position')
        self.add_input('NodeSocketVector', 'To Position')
        self.add_input('NodeSocketVector', 'Front Facing', default_value=[1, 0, 0])
        self.add_input('NodeSocketVector', 'Main Rotation Axis', default_value=[0, 0, 1])
        self.add_input('NodeSocketBool', 'Disable Primary Roatation')
        self.add_input('NodeSocketBool', 'Disable Secodary Roatation')
        self.add_input('NodeSocketBool', 'Restrict Primary Rotation')
        self.add_input('NodeSocketFloat', 'min Primary Rotation')
        self.add_input('NodeSocketFloat', 'max Primary Rotation')
        self.add_input('NodeSocketBool', 'Restrict Secondary Rotation')
        self.add_input('NodeSocketFloat', 'min Secondary Rotation')
        self.add_input('NodeSocketFloat', 'max Secondary Rotation')
        self.add_output('NodeSocketVector', 'Rotation (Euler)')
        self.add_output('NodeSocketVector', 'Rotation (Quat)')
        self.add_output('NodeSocketBool', 'Is in field of view')
