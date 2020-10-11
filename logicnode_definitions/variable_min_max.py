import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class MinMaxNode(ArmLogicTreeNode):
    """Min/Max Node"""
    bl_idname = 'LNMinMaxNode'
    bl_label = 'Clamp Variable'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Value')
        self.add_input('NodeSocketFloat', 'Min')
        self.add_input('NodeSocketFloat', 'Max')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(MinMaxNode, category='Variable')
