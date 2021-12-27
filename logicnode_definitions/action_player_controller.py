import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *

import logicnode_definitions


class PlayerController(ArmLogicTreeNode):
    """PlayerController"""
    bl_idname = 'LNPlayerController'
    bl_label = 'Player Controller'

    arm_category = logicnode_definitions.CATEGORY_NAME
    arm_section = 'controllers'
    arm_version = 1

    def arm_init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')

        self.add_input('ArmNodeSocketAction', 'Activate')

        self.add_input('ArmNodeSocketObject', 'Player Object', default_value='Player')

        self.add_input('NodeSocketFloat', 'Overall Speed Modifier', default_value=1.0)

        self.add_input('NodeSocketBool', 'Forward')
        self.add_input('NodeSocketFloat', 'Forward Speed', default_value=1.0)

        self.add_input('NodeSocketBool', 'Left')
        self.add_input('NodeSocketFloat', 'Left Speed', default_value=1.0)

        self.add_input('NodeSocketBool', 'Right')
        self.add_input('NodeSocketFloat', 'Right Speed', default_value=1.0)

        self.add_input('NodeSocketBool', 'Reverse')
        self.add_input('NodeSocketFloat', 'Reverse Speed', default_value=1.0)

        self.add_input('NodeSocketBool', 'Jump')
        self.add_input('NodeSocketFloat', 'Jump Height', default_value=1.0)

        self.add_input('NodeSocketBool', 'Run')
        self.add_input('NodeSocketFloat', 'Run Multiplier', default_value=1.5)

        self.add_input('NodeSocketBool', 'Crouch')
        self.add_input('NodeSocketBool', 'Hold for crouch', default_value=1)
        self.add_input('NodeSocketFloat', 'Crouch Multiplier', default_value=0.5)
