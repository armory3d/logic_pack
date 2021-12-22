import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class CompareNumberNode(ArmLogicTreeNode):
    """Compares two numbers"""
    bl_idname = 'LNCompareNumberNode'
    bl_label = 'Compare Numbers'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'logic'
    arm_version = 1

    property0: EnumProperty(
        items = [('EQUAL', 'Equal', 'True, if both inputs are equal.'),
                 ('ALMOST EQUAL', 'Almost Equal', 'True, if both inputs are almost (defined by threshold) equal.'),
                 ('LESS', 'Less', 'True, if A is less than B.'),
                 ('MORE', 'More', 'True, if A is more than B.'),
                 ('LESS EQUAL', 'Less Equal', 'True, if A is less than or equal to B.'),
                 ('MORE EQUAL', 'More Equal', 'True, if A is more than or equal to B.'),
                 ],
        name='Select Operation', default='EQUAL')

    property1: FloatProperty(name='Tolerance', description='Almost Equal threshold', default=0.0001)

    def arm_init(self, context):
        self.add_input('NodeSocketInt', 'A')
        self.add_input('NodeSocketInt', 'B')
        self.add_output('NodeSocketBool', 'Result')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
        if self.property0 == 'ALMOST EQUAL':
            layout.prop(self, 'property1')
