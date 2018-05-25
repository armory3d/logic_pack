import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *
import arm.nodes_logic

class QuatToEulerNode(Node, ArmLogicTreeNode):
    '''QuatToEulerNode'''
    bl_idname = 'LNQuatToEulerNode'
    bl_label = 'Quat To Euler'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketFloat', 'X')
        self.inputs.new('NodeSocketFloat', 'Y')
        self.inputs.new('NodeSocketFloat', 'Z')
        self.inputs.new('NodeSocketFloat', 'W')
        self.outputs.new('NodeSocketVector', 'Euler')

class SeparateQuatNode(Node, ArmLogicTreeNode):
    '''SeparateQuatNode'''
    bl_idname = 'LNSeparateQuatNode'
    bl_label = 'Separate Quat'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', 'Transform')
        self.outputs.new('NodeSocketFloat', 'X')
        self.outputs.new('NodeSocketFloat', 'Y')
        self.outputs.new('NodeSocketFloat', 'Z')
        self.outputs.new('NodeSocketFloat', 'W')
        self.outputs.new('NodeSocketVector', 'Euler')

class LookNode(Node, ArmLogicTreeNode):
    '''Look Node'''
    bl_idname = 'LNLookNode'
    bl_label = 'Look'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketVector', 'Vector')
        self.inputs.new('NodeSocketBool', 'Look Y')
        self.inputs.new('NodeSocketBool', 'Look Z')
        self.inputs.new('NodeSocketFloat', 'Minimum')
        self.inputs.new('NodeSocketFloat', 'Maximum')
        self.outputs.new('ArmNodeSocketAction', 'Out')

class ArrayLoopIndiceNode(Node, ArmLogicTreeNode):
    '''ArrayLoop node avec indice'''
    bl_idname = 'LNArrayLoopIndiceNode'
    bl_label = 'Array Loop Indice'
    bl_icon = 'CURVE_PATH'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketShader', 'Array')
        self.outputs.new('ArmNodeSocketAction', 'Loop')
        self.outputs.new('NodeSocketInt', 'Value')
        self.outputs.new('ArmNodeSocketAction', 'Done')
        self.outputs.new('NodeSocketInt', 'Indice')

class MinMaxNode(Node, ArmLogicTreeNode):
    '''Min/Max Node'''
    bl_idname = 'LNMinMaxNode'
    bl_label = 'MinMax'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketShader', 'Value')
        self.inputs.new('NodeSocketShader', 'Value')
        self.inputs.new('NodeSocketShader', 'Value')
        self.outputs.new('ArmNodeSocketAction', 'Out')

class PlayerController(Node, ArmLogicTreeNode):
    '''PlayerController'''
    bl_idname = 'LNPlayerController'
    bl_label = 'Player Controller'
    bl_icon = 'GAME'

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
        self.inputs.new('NodeSocketFloat', 'Crouch Multiplier')
        self.inputs[-1].default_value = 0.5

class CameraController(Node, ArmLogicTreeNode):
    '''CameraController'''
    bl_idname = 'LNCameraController'
    bl_label = 'Camera Controller'
    bl_icon = 'GAME'

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')

        self.inputs.new('ArmNodeSocketAction', 'Activate')

        self.inputs.new('ArmNodeSocketObject', 'Player Object')
        self.inputs[-1].default_value = 'Player'

        self.inputs.new('ArmNodeSocketObject', 'Camera Object')
        self.inputs[-1].default_value = 'Camera'

        self.inputs.new('NodeSocketFloat', 'Speed Modifier')
        self.inputs[-1].default_value = 1.0
        self.inputs.new('NodeSocketBool', 'Invert Vertical')
        self.inputs.new('NodeSocketBool', 'Invert Horizontal')

        self.inputs.new('NodeSocketFloat', 'Horizontal Axis Movement')
        self.inputs.new('NodeSocketFloat', 'Horiontal Speed')
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

def register():
    # Add custom nodes
    # TODO: separate into single .py file per logic node, similar to the main Armory repository
    add_node(QuatToEulerNode, category='Value')
    add_node(SeparateQuatNode, category='Value')
    add_node(ArrayLoopIndiceNode, category='Logic')
    add_node(MinMaxNode, category='Variable')
    add_node(LookNode, category='Action')
    add_node(PlayerController, category='Action')
    add_node(CameraController, category='Action')

    # Register newly added nodes
    arm.nodes_logic.register_nodes()
