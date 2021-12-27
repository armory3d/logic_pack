import arm.logicnode

CATEGORY_NAME = 'Armory Logic Pack'


def register_all():
    """Import all nodes in this node package."""
    arm.logicnode.init_nodes(__path__, __package__)
