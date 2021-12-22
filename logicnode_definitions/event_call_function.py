import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class CallFunctionNode(ArmLogicTreeNode):
    """Call Function Node"""
    bl_idname = 'LNCallFunctionNode'
    bl_label = 'Call Function'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'event'
    arm_version = 1

    min_inputs = 2

    def __init__(self):
        array_nodes[str(id(self))] = self

    def arm_init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Function')
        self.add_input('NodeSocketInt', 'ID')

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)

        op = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketShader'
        op2 = row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))
