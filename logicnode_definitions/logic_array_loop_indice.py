import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class ArrayLoopIndiceNode(ArmLogicTreeNode):
    """ArrayLoop node avec indice"""
    bl_idname = 'LNArrayLoopIndiceNode'
    bl_label = 'Array Loop Indice'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'logic'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Array')
        self.add_output('ArmNodeSocketAction', 'Loop')
        self.add_output('NodeSocketInt', 'Value')
        self.add_output('ArmNodeSocketAction', 'Done')
        self.add_output('NodeSocketInt', 'Indice')
