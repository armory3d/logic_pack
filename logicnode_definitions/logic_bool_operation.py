import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class BoolOperationNode(ArmLogicTreeNode):
	"""Boolean Operations"""
	bl_idname = 'LNBoolOperationNode'
	bl_label = 'Boolean Operation'
	bl_icon = 'QUESTION'

	property0: EnumProperty(
		items = [('AND', 'And', 'True, if both inputs are true.'),
				 ('OR', 'Or', 'True, if either of the inputs is true.'),
				 ('XOR', 'Xor', 'True, when an uneven number of inputs is true.'),
				 ('EQUAL', 'Equal', 'True, when both inputs are the same.'),
				 ],
		name='Select Operation', default='AND')

	def __init__(self):
		array_nodes[str(id(self))] = self

	def init(self, context):
		self.inputs.new('NodeSocketBool', 'Invert Output')
		self.inputs.new('NodeSocketBool', 'Input 1')
		self.inputs.new('NodeSocketBool', 'Input 2')
		self.outputs.new('NodeSocketBool', 'Output')

	def draw_buttons(self, context, layout):
		layout.prop(self, 'property0')

		row = layout.row(align=True)
		add_button = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
		add_button.node_index = str(id(self))
		add_button.socket_type = 'NodeSocketBool'
		remove_button =  row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
		remove_button.node_index = str(id(self))

add_node(BoolOperationNode, category='Logic')
