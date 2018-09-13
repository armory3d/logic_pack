import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class LookNode(Node, ArmLogicTreeNode):
    '''Look Node'''
    bl_idname = 'LNLookNode'
    bl_label = 'Look'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketVector', 'Vector')
        self.inputs.new('NodeSocketBool', 'Look Y')
        self.inputs.new('NodeSocketBool', 'Look Z')
        self.inputs.new('NodeSocketFloat', 'Minimum')
        self.inputs.new('NodeSocketFloat', 'Maximum')
        self.outputs.new('ArmNodeSocketAction', 'Out')
        
add_node(LookNode, category='Action')
