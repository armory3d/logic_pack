import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SeparateQuatNode(ArmLogicTreeNode):
    """SeparateQuatNode"""
    bl_idname = 'LNSeparateQuatNode'
    bl_label = 'Separate Quat'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.add_input('NodeSocketVector', 'Quat')
        self.add_output('NodeSocketFloat', 'X')
        self.add_output('NodeSocketFloat', 'Y')
        self.add_output('NodeSocketFloat', 'Z')
        self.add_output('NodeSocketFloat', 'W')
        self.add_output('NodeSocketVector', 'Euler')

add_node(SeparateQuatNode, category='Value')
