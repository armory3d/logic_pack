import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class QuatToEulerNode(ArmLogicTreeNode):
    """QuatToEulerNode"""
    bl_idname = 'LNQuatToEulerNode'
    bl_label = 'Quat To Euler'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'value'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('NodeSocketFloat', 'X')
        self.add_input('NodeSocketFloat', 'Y')
        self.add_input('NodeSocketFloat', 'Z')
        self.add_input('NodeSocketFloat', 'W')
        self.add_output('NodeSocketVector', 'Euler')
