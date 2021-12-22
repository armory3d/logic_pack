import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class LookNode(ArmLogicTreeNode):
    """Look Node"""
    bl_idname = 'LNLookNode'
    bl_label = 'Look'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'transform'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketVector', 'Vector')
        self.add_input('NodeSocketBool', 'Look Y')
        self.add_input('NodeSocketBool', 'Look Z')
        self.add_input('NodeSocketFloat', 'Minimum')
        self.add_input('NodeSocketFloat', 'Maximum')
        self.add_output('ArmNodeSocketAction', 'Out')
