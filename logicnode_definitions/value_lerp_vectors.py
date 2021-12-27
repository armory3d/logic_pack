import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class LerpVectorsNode(ArmLogicTreeNode):
    """Lerp Vectors node"""
    bl_idname = 'LNLerpVectorsNode'
    bl_label = 'Lerp Vectors'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'value'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketVector', 'Starting Vector')
        self.add_input('NodeSocketVector', 'End Vector')
        self.add_input('NodeSocketFloat', 'Time For Change')
        self.add_input('NodeSocketBool', 'Stop Interpolation')
        self.add_output('NodeSocketVector', 'Vector')
