import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *


class CameraController(Node, ArmLogicTreeNode):
    '''CameraController'''
    bl_idname = 'LNCameraController'
    bl_label = 'Camera Controller'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')

        self.inputs.new('ArmNodeSocketAction', 'Activate')

        self.inputs.new('ArmNodeSocketObject', 'Player Object')
        self.inputs[-1].default_value = 'Player'

        self.inputs.new('ArmNodeSocketObject', 'Camera Object')
        self.inputs[-1].default_value = 'Camera'

        self.inputs.new('NodeSocketFloat', 'Speed Modifier')
        self.inputs[-1].default_value = 1.0
        self.inputs.new('NodeSocketBool', 'Additional Modifier (e.g. sniper)')
        self.inputs.new('NodeSocketFloat', 'Modifier')
        self.inputs[-1].default_value = 0.25
        self.inputs.new('NodeSocketBool', 'Invert Horizontal')
        self.inputs.new('NodeSocketBool', 'Invert Vertical')

        self.inputs.new('NodeSocketFloat', 'Horizontal Axis Movement')
        self.inputs.new('NodeSocketFloat', 'Horizontal Speed')
        self.inputs[-1].default_value = 1.0
        self.inputs.new('NodeSocketBool', 'Restrict Horizontal')
        self.inputs.new('NodeSocketFloat', 'hMin (Radians)')
        self.inputs.new('NodeSocketFloat', 'hMax (Radians)')

        self.inputs.new('NodeSocketFloat', 'Vertical Axis Movement')
        self.inputs.new('NodeSocketFloat', 'Vertical Speed')
        self.inputs[-1].default_value = 1.0
        self.inputs.new('NodeSocketBool', 'Restrict Vertical')
        self.inputs.new('NodeSocketFloat', 'vMin (Radians)')
        self.inputs.new('NodeSocketFloat', 'vMax (Radians)')


add_node(CameraController, category='Action')
