import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class CompareNumberNode(Node, ArmLogicTreeNode):
	'''Compares two numbers'''
	bl_idname = 'LNCompareNumberNode'
	bl_label = 'Compare Numbers'
	bl_icon = 'GAME'
	
	property0 = EnumProperty(
		items = [('EQUAL', 'Equal', 'True, if both inputs are equal.'),
				 ('ALMOST EQUAL', 'Almost Equal', 'True, if both inputs are almost (defined by threshold) equal.'),
				 ('LESS', 'Less', 'True, if A is less than B.'),
				 ('MORE', 'More', 'True, if A is more than B.'),
				 ('LESS EQUAL', 'Less Equal', 'True, if A is less than or equal to B.'),
				 ('MORE EQUAL', 'More Equal', 'True, if A is more than or equal to B.'),
				 ],
		name='', default='EQUAL')

	property1 = FloatProperty(name='Tolerance', description='Almost Equal threshold', default=0.0001)

	def init(self, context):
		self.inputs.new('NodeSocketInt', 'A')
		self.inputs.new('NodeSocketInt', 'B')
		self.outputs.new('NodeSocketBool', 'Result')
	
	def draw_buttons(self, context, layout):
		layout.prop(self, 'property0')
		if self.property0 == 'ALMOST EQUAL':
			layout.prop(self, 'property1')

add_node(CompareNumberNode, category='Logic')
