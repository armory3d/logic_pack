import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class GetContactCoordsNode(ArmLogicTreeNode):
    """Get contact coords Node"""
    bl_idname = 'LNGetContactCoordsNode'
    bl_label = 'Get Contact Coords'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('ArmNodeSocketArray', 'Array')
        self.add_output('ArmNodeSocketArray', 'Coords')

add_node(GetContactCoordsNode, category='Physics')
