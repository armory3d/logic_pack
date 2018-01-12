from bpy.types import Node
from arm.logicnode.arm_nodes import *
import arm.nodes_logic

class TestNode(Node, ArmLogicTreeNode):
    '''Test node'''
    bl_idname = 'LNTestNode'
    bl_label = 'Test'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketShader', 'Value')
        self.inputs.new('NodeSocketShader', 'Value')
        self.inputs.new('NodeSocketShader', 'Value')
        self.outputs.new('ArmNodeSocketAction', 'Out')

def register():
    # Add custom nodes
    add_node(TestNode, category='Variable')
    # Register newly added nodes
    arm.nodes_logic.register_nodes()
