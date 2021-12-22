import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket

from arm.logicnode.arm_nodes import *


# class <NodeName>(ArmLogicTreeNode):
#    """<Short Desciption (optional)>"""
#    bl_idname = 'LN<NodeName>'
#    bl_label = '<Name of the Node inside Blender>'
#
#    arm_category = '<Category of the node>'
#    arm_section = '<Section of the node inside the category>'
#    arm_version = 1
#
#    def arm_init(self, context):
#        self.add_input('<SocketType>', '<SocketName>')
#        self.add_output('<SocketType>', '<SocketName>')
