import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

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
        
add_node(ArrayLoopIndiceNode, category='Logic')
