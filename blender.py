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

class TranslateOnLocalAxisNode(Node, ArmLogicTreeNode):
    '''TranslateOnLocalAxisNode'''
    bl_idname = 'LNTranslateOnLocalAxisNode'
    bl_label = 'Translate On Local Axis'
    bl_icon = 'GAME'
   

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketFloat', 'Speed')
        self.inputs.new('NodeSocketInt', 'Forward/Up/Right')
        self.inputs.new('NodeSocketBool', 'Inverse')
        self.outputs.new('ArmNodeSocketAction', 'Out')


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

class ToBoolNode(Node, ArmLogicTreeNode):
    '''To Bool Node'''
    bl_idname = 'LNToBoolNode'
    bl_label = 'To Bool'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.outputs.new('NodeSocketBool', 'Bool')

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

class InverseNode(Node, ArmLogicTreeNode):
    '''Inverse node'''
    bl_idname = 'LNInverseNode'
    bl_label = 'Inverse'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.outputs.new('ArmNodeSocketAction', 'Out')

def register():
    # Add custom nodes
    add_node(QuatToEulerNode, category= 'Value')
    add_node(SeparateQuatNode, category='Value')
    add_node(TranslateOnLocalAxisNode, category='Action')
    add_node(ArrayLoopIndiceNode, category='Logic')
    add_node(ToBoolNode, category='Logic')
    add_node(MinMaxNode, category='Variable')
    add_node(InverseNode, category='Logic')
    add_node(LookNode, category='Action')

    # Register newly added nodes
    arm.nodes_logic.register_nodes()
