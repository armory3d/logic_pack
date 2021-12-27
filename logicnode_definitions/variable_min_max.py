import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class MinMaxNode(ArmLogicTreeNode):
    """Min/Max Node"""
    bl_idname = 'LNMinMaxNode'
    bl_label = 'Clamp Variable'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'value'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Value')
        self.add_input('NodeSocketFloat', 'Min')
        self.add_input('NodeSocketFloat', 'Max')
        self.add_output('ArmNodeSocketAction', 'Out')
