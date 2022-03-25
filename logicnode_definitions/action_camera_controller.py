import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class CameraController(ArmLogicTreeNode):
    """Camera Controller"""
    bl_idname = 'LNCameraController'
    bl_label = 'Camera Controller'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'controllers'
    arm_version = 1

    def arm_init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')

        self.add_input('ArmNodeSocketAction', 'Activate')

        self.add_input('ArmNodeSocketObject', 'Player Object')

        self.add_input('ArmNodeSocketObject', 'Camera Object')

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
