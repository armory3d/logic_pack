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
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketVector', 'Starting Vector')
        self.add_input('NodeSocketVector', 'End Vector')
        self.add_input('NodeSocketFloat', 'Time For Change')
        self.add_input('NodeSocketBool', 'Stop Interpolation')
        self.add_output('NodeSocketVector', 'Vector')

add_node(LerpVectorsNode, category='Value')
