import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class GetContactCoordsNode(ArmLogicTreeNode):
    """Get contact coords Node"""
    bl_idname = 'LNGetContactCoordsNode'
    bl_label = 'Get Contact Coords'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'physics'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('ArmNodeSocketArray', 'Array')
        self.add_output('ArmNodeSocketArray', 'Coords')
