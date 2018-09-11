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
        self.inputs.new('NodeSocketVector', 'Quat')
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
        self.inputs.new('NodeSocketBool', 'Hold for crouch')
        self.inputs[-1].default_value = 1
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
        self.inputs.new('NodeSocketBool', 'Additional Modifier (e.g. sniper)')
        self.inputs.new('NodeSocketFloat', 'Modifier')
        self.inputs[-1].default_value = 0.25
        self.inputs.new('NodeSocketBool', 'Invert Horizontal')
        self.inputs.new('NodeSocketBool', 'Invert Vertical')

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

class AnimationControllerNode(Node, ArmLogicTreeNode):
    '''AnimationController node'''
    bl_idname = 'LNAnimationControllerNode'
    bl_label = 'AnimationController'
    bl_icon = 'GAME'

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')
        self.outputs.new('ArmNodeSocketAction', 'Done')
        
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Animated Object')
        self.inputs[-1].default_value = 'Animated Object'
        self.inputs.new('ArmNodeSocketAnimAction', 'Idle')
        self.inputs[-1].default_value = 'Idle'
        self.inputs.new('NodeSocketFloat', 'Blend Time')
        self.inputs[-1].default_value = 0.2


    def draw_buttons(self, context, layout):
        row1 = layout.row(align=True)
        row2 = layout.row(align=True)

        op = row1.operator('arm.node_add_input', text='New Animation Controller', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketBool'
        
        op2 = row1.operator('arm.node_add_input', text='New Animation', icon='PLUS', emboss=True)
        op2.node_index = str(id(self))
        op2.socket_type = 'ArmNodeSocketAnimAction'
        
        op3 = row2.operator('arm.node_add_input', text='New blend time', icon='PLUS', emboss=True)
        op3.node_index = str(id(self))
        op3.socket_type = 'NodeSocketFloat'
        
        op4 = row2.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op4.node_index = str(id(self))

class TimerNode(Node, ArmLogicTreeNode):
    '''TimerNode'''
    bl_idname = 'LNTimerNode'
    bl_label = 'Timer Node'
    bl_icon = 'GAME'

    def init(self, context):
        self.outputs.new('ArmNodeSocketAction', 'Out')
        self.outputs.new('ArmNodeSocketAction', 'Done')
        self.outputs.new('NodeSocketBool', 'Running')
        self.outputs.new('NodeSocketBool', 'Paused')
        self.outputs.new('NodeSocketFloat', 'Seconds left')
        self.outputs.new('NodeSocketFloat', 'Progress (in %)')
        self.outputs.new('NodeSocketInt', 'Repetitions done')

        self.inputs.new('ArmNodeSocketAction', 'Start')
        self.inputs.new('NodeSocketBool', 'Pause')
        self.inputs.new('NodeSocketBool', 'Stop')

        self.inputs.new('NodeSocketFloat', 'Seconds')
        self.inputs.new('NodeSocketInt', 'Repetitions (0 for oneshot, negative for unlimited)')

class LerpVectorsNode(Node, ArmLogicTreeNode):
    '''Lerp Vectors node'''
    bl_idname = 'LNLerpVectorsNode'
    bl_label = 'Lerp Vectors'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketVector', 'Starting Vector')
        self.inputs.new('NodeSocketVector', 'End Vector')
        self.inputs.new('NodeSocketFloat', 'Time For Change')
        self.inputs.new('NodeSocketBool', 'Stop Interpolation')
        self.outputs.new('NodeSocketVector', 'Vector')

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
    add_node(AnimationControllerNode, category='Animation')
    add_node(TimerNode, category='Logic')
    add_node(LerpVectorsNode, category='Value')

    # Register newly added nodes
    arm.nodes_logic.register_nodes()
