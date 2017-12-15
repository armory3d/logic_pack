from bpy.types import Node
from arm.logicnode.arm_nodes import *
import arm.nodes_logic

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
    add_node(InverseNode, category='Action')
    # Register newly added nodes
    arm.nodes_logic.register_nodes()
