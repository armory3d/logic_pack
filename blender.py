from bpy.types import Node
from arm.logicnode.arm_nodes import *
import arm.nodes_logic

class ToBool(Node, ArmLogicTreeNode):
    '''To Bool'''
    bl_idname = 'LNToBool'
    bl_label = 'ToBool'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.outputs.new('NodeSocketBool', 'Bool')

class minmaxnode(Node, ArmLogicTreeNode):
    '''Min/Max Node'''
    bl_idname = 'LNminmaxnode'
    bl_label = 'minmaxnode'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')

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
    add_node(ToBool, category='Logic')
    add_node(minmaxnode, category='Variable')
    add_node(InverseNode, category='Logic')
    # Register newly added nodes
    arm.nodes_logic.register_nodes()
