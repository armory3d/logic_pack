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
        
def register():
    # Add custom nodes
    add_node(ToBool, category='Logic') 
    # Register newly added nodes
    arm.nodes_logic.register_nodes()
