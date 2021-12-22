import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class BoolOperationNode(ArmLogicTreeNode):
    """Boolean Operations"""
    bl_idname = 'LNBoolOperationNode'
    bl_label = 'Boolean Operation'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'logic'
    arm_version = 1

    property0: EnumProperty(
        items = [('AND', 'And', 'True, if both inputs are true.'),
                 ('OR', 'Or', 'True, if either of the inputs is true.'),
                 ('XOR', 'Xor', 'True, when an uneven number of inputs is true.'),
                 ('EQUAL', 'Equal', 'True, when both inputs are the same.'),
                 ],
        name='Select Operation', default='AND')

    def __init__(self):
        array_nodes[str(id(self))] = self

    def arm_init(self, context):
        self.add_input('NodeSocketBool', 'Invert Output')
        self.add_input('NodeSocketBool', 'Input 1')
        self.add_input('NodeSocketBool', 'Input 2')
        self.add_output('NodeSocketBool', 'Output')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

        row = layout.row(align=True)
        add_button = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        add_button.node_index = str(id(self))
        add_button.socket_type = 'NodeSocketBool'
        remove_button =  row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        remove_button.node_index = str(id(self))
