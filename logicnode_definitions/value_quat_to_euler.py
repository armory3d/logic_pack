import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class QuatToEulerNode(Node, ArmLogicTreeNode):
    '''QuatToEulerNode'''
    bl_idname = 'LNQuatToEulerNode'
    bl_label = 'Quat To Euler'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketFloat', 'X')
        self.inputs.new('NodeSocketFloat', 'Y')
        self.inputs.new('NodeSocketFloat', 'Z')
        self.inputs.new('NodeSocketFloat', 'W')
        self.outputs.new('NodeSocketVector', 'Euler')
 

add_node(QuatToEulerNode, category='Value')
