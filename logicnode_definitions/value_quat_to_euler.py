import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class QuatToEulerNode(ArmLogicTreeNode):
    """QuatToEulerNode"""
    bl_idname = 'LNQuatToEulerNode'
    bl_label = 'Quat To Euler'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.add_input('NodeSocketFloat', 'X')
        self.add_input('NodeSocketFloat', 'Y')
        self.add_input('NodeSocketFloat', 'Z')
        self.add_input('NodeSocketFloat', 'W')
        self.add_output('NodeSocketVector', 'Euler')


add_node(QuatToEulerNode, category='Value')
