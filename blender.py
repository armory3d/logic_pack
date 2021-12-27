"""
Armory logic pack - community-made logic nodes for Armory 3D.

https://github.com/armory3d/logic_pack
"""
import arm.logicnode
import arm.logicnode.arm_nodes as arm_nodes

import logicnode_definitions


def register():
    # Register a category for the logic node package
    arm_nodes.add_category(
        logicnode_definitions.CATEGORY_NAME,
        icon='DISK_DRIVE',
        description='Logic nodes from the Armory Logic Pack (https://github.com/armory3d/logic_pack)'
    )

    # Then register all the nodes
    logicnode_definitions.register_all()
