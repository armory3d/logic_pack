import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *
import arm.nodes_logic
from logicnode_definitions import *

def register():
    # Add custom nodes
    # TODO: separate into single .py file per logic node, similar to the main Armory repository
    # DONE!
    
    # Register newly added nodes
    arm.nodes_logic.register_nodes()
