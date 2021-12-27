import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class AnimationControllerNode(ArmLogicTreeNode):
    """AnimationController node"""
    bl_idname = 'LNAnimationControllerNode'
    bl_label = 'AnimationController'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'controllers'
    arm_version = 1

    def __init__(self):
        array_nodes[str(id(self))] = self

    def arm_init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('ArmNodeSocketAction', 'Done')

        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Animated Object', default_value='Animated Object')
        self.add_input('ArmNodeSocketAnimAction', 'Idle', default_value='Idle')
        self.add_input('NodeSocketFloat', 'Blend Time', default_value=0.2)


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
