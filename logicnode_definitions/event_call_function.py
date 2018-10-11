import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class CallFunctionNode(Node, ArmLogicTreeNode):
    '''Call Function Node'''
    bl_idname = 'LNCallFunctionNode'
    bl_label = 'Call Function'
    bl_icon = 'GAME'
    min_inputs = 2

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketString', 'Function')
        self.inputs.new('NodeSocketInt', 'ID')

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)

        op = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketShader'
        op2 = row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))
        
add_node(CallFunctionNode, category='Event')
