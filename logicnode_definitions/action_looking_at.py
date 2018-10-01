import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class LookingAtNode(Node, ArmLogicTreeNode):
	'''Looking at Node'''
	bl_idname = 'LNLookingAtNode'
	bl_label = 'Looking At'
	bl_icon = 'GAME'
	
	def init(self, context):
		self.inputs.new('ArmNodeSocketAction', 'Activate')
		self.inputs.new('ArmNodeSocketObject', 'From Object')
		self.inputs.new('ArmNodeSocketObject', 'To Object')
		self.inputs.new('NodeSocketVector', 'Front Facing')
		self.inputs.new('NodeSocketVector', 'Main Rotation Axis')
		self.inputs.new('NodeSocketBool', 'Disable Primary Roatation')
		self.inputs.new('NodeSocketBool', 'Disable Secodary Roatation')
		self.inputs.new('NodeSocketBool', 'Restrict Primary Rotation')
		self.inputs.new('NodeSocketFloat', 'min Primary Rotation')
		self.inputs.new('NodeSocketFloat', 'max Primary Rotation')
		self.inputs.new('NodeSocketBool', 'Restrict Secondary Rotation')
		self.inputs.new('NodeSocketFloat', 'min Secondary Rotation')
		self.inputs.new('NodeSocketFloat', 'max Secondary Rotation')

add_node(LookingAtNode, category='Action')
