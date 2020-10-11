import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *


class CameraController(ArmLogicTreeNode):
    """CameraController"""
    bl_idname = 'LNCameraController'
    bl_label = 'Camera Controller'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')

        self.add_input('ArmNodeSocketAction', 'Activate')

        self.add_input('ArmNodeSocketObject', 'Player Object', default_value='Player')

        self.add_input('ArmNodeSocketObject', 'Camera Object', default_value='Camera')

        self.add_input('NodeSocketFloat', 'Speed Modifier', default_value=1.0)
        self.add_input('NodeSocketBool', 'Additional Modifier (e.g. sniper)')
        self.add_input('NodeSocketFloat', 'Modifier', default_value=0.25)
        self.add_input('NodeSocketBool', 'Invert Horizontal')
        self.add_input('NodeSocketBool', 'Invert Vertical')

        self.add_input('NodeSocketFloat', 'Horizontal Axis Movement')
        self.add_input('NodeSocketFloat', 'Horizontal Speed', default_value=1.0)
        self.add_input('NodeSocketBool', 'Restrict Horizontal')
        self.add_input('NodeSocketFloat', 'hMin (Radians)')
        self.add_input('NodeSocketFloat', 'hMax (Radians)')

        self.add_input('NodeSocketFloat', 'Vertical Axis Movement')
        self.add_input('NodeSocketFloat', 'Vertical Speed', default_value=1.0)
        self.add_input('NodeSocketBool', 'Restrict Vertical')
        self.add_input('NodeSocketFloat', 'vMin (Radians)')
        self.add_input('NodeSocketFloat', 'vMax (Radians)')


add_node(CameraController, category='Action')
