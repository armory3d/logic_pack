import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SeparateQuatNode(Node, ArmLogicTreeNode):
    '''SeparateQuatNode'''
    bl_idname = 'LNSeparateQuatNode'
    bl_label = 'Separate Quat'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketVector', 'Quat')
        self.outputs.new('NodeSocketFloat', 'X')
        self.outputs.new('NodeSocketFloat', 'Y')
        self.outputs.new('NodeSocketFloat', 'Z')
        self.outputs.new('NodeSocketFloat', 'W')
        self.outputs.new('NodeSocketVector', 'Euler')

add_node(SeparateQuatNode, category='Value')
