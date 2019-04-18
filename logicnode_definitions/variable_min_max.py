import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class MinMaxNode(Node, ArmLogicTreeNode):
    '''Min/Max Node'''
    bl_idname = 'LNMinMaxNode'
    bl_label = 'Clamp Variable'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketShader', 'Value')
        self.inputs.new('NodeSocketFloat', 'Min')
        self.inputs.new('NodeSocketFloat', 'Max')
        self.outputs.new('ArmNodeSocketAction', 'Out')
        
add_node(MinMaxNode, category='Variable')
