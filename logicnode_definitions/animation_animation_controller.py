import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class AnimationControllerNode(Node, ArmLogicTreeNode):
    '''AnimationController node'''
    bl_idname = 'LNAnimationControllerNode'
    bl_label = 'AnimationController'
    bl_icon = 'QUESTION'

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')
        self.outputs.new('ArmNodeSocketAction', 'Done')
        
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Animated Object')
        self.inputs[-1].default_value = 'Animated Object'
        self.inputs.new('ArmNodeSocketAnimAction', 'Idle')
        self.inputs[-1].default_value = 'Idle'
        self.inputs.new('NodeSocketFloat', 'Blend Time')
        self.inputs[-1].default_value = 0.2


    def draw_buttons(self, context, layout):
        row1 = layout.row(align=True)
        row2 = layout.row(align=True)

        op = row1.operator('arm.node_add_input', text='New Animation Controller', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketBool'
        
        op2 = row1.operator('arm.node_add_input', text='New Animation', icon='PLUS', emboss=True)
        op2.node_index = str(id(self))
        op2.socket_type = 'ArmNodeSocketAnimAction'
        
        op3 = row2.operator('arm.node_add_input', text='New blend time', icon='PLUS', emboss=True)
        op3.node_index = str(id(self))
        op3.socket_type = 'NodeSocketFloat'
        
        op4 = row2.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op4.node_index = str(id(self))

add_node(AnimationControllerNode, category='Animation')
