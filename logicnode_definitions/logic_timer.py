import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class TimerNode(ArmLogicTreeNode):
    """TimerNode"""
    bl_idname = 'LNTimerNode'
    bl_label = 'Timer Node'
    bl_icon = 'QUESTION'

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

add_node(TimerNode, category='Logic')
