import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class PlayerController(ArmLogicTreeNode):
    '''PlayerController'''
    bl_idname = 'LNPlayerController'
    bl_label = 'Player Controller'
    bl_icon = 'QUESTION'

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')

        self.inputs.new('ArmNodeSocketAction', 'Activate')

        self.inputs.new('ArmNodeSocketObject', 'Player Object')
        self.inputs[-1].default_value = 'Player'

        self.inputs.new('NodeSocketFloat', 'Overall Speed Modifier')
        self.inputs[-1].default_value = 1.0

        self.inputs.new('NodeSocketBool', 'Forward')
        self.inputs.new('NodeSocketFloat', 'Forward Speed')
        self.inputs[-1].default_value = 1.0

        self.inputs.new('NodeSocketBool', 'Left')
        self.inputs.new('NodeSocketFloat', 'Left Speed')
        self.inputs[-1].default_value = 1.0

        self.inputs.new('NodeSocketBool', 'Right')
        self.inputs.new('NodeSocketFloat', 'Right Speed')
        self.inputs[-1].default_value = 1.0

        self.inputs.new('NodeSocketBool', 'Reverse')
        self.inputs.new('NodeSocketFloat', 'Reverse Speed')
        self.inputs[-1].default_value = 1.0

        self.inputs.new('NodeSocketBool', 'Jump')
        self.inputs.new('NodeSocketFloat', 'Jump Height')
        self.inputs[-1].default_value = 1.0

        self.inputs.new('NodeSocketBool', 'Run')
        self.inputs.new('NodeSocketFloat', 'Run Multiplier')
        self.inputs[-1].default_value = 1.5

        self.inputs.new('NodeSocketBool', 'Crouch')
        self.inputs.new('NodeSocketBool', 'Hold for crouch')
        self.inputs[-1].default_value = 1
        self.inputs.new('NodeSocketFloat', 'Crouch Multiplier')
        self.inputs[-1].default_value = 0.5

add_node(PlayerController, category='Action')
