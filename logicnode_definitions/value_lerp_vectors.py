import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class LerpVectorsNode(ArmLogicTreeNode):
    """Lerp Vectors node"""
    bl_idname = 'LNLerpVectorsNode'
    bl_label = 'Lerp Vectors'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketVector', 'Starting Vector')
        self.inputs.new('NodeSocketVector', 'End Vector')
        self.inputs.new('NodeSocketFloat', 'Time For Change')
        self.inputs.new('NodeSocketBool', 'Stop Interpolation')
        self.outputs.new('NodeSocketVector', 'Vector')

add_node(LerpVectorsNode, category='Value')
