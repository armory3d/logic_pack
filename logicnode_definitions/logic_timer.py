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
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('ArmNodeSocketAction', 'Done')
        self.add_output('NodeSocketBool', 'Running')
        self.add_output('NodeSocketBool', 'Paused')
        self.add_output('NodeSocketFloat', 'Seconds left')
        self.add_output('NodeSocketFloat', 'Progress (in %)')
        self.add_output('NodeSocketInt', 'Repetitions done')

        self.add_input('ArmNodeSocketAction', 'Start')
        self.add_input('NodeSocketBool', 'Pause')
        self.add_input('NodeSocketBool', 'Stop')

        self.add_input('NodeSocketFloat', 'Seconds')
        self.add_input('NodeSocketInt', 'Repetitions (0 for oneshot, negative for unlimited)')

add_node(TimerNode, category='Logic')
