import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class LookNode(ArmLogicTreeNode):
    """Look Node"""
    bl_idname = 'LNLookNode'
    bl_label = 'Look'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketVector', 'Vector')
        self.add_input('NodeSocketBool', 'Look Y')
        self.add_input('NodeSocketBool', 'Look Z')
        self.add_input('NodeSocketFloat', 'Minimum')
        self.add_input('NodeSocketFloat', 'Maximum')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(LookNode, category='Action')
