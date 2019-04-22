import bpy
import arm
import os
import importlib

class SaveSelectedNodesOperator(bpy.types.Operator):
    bl_idname = "node.save_selected_nodes"
    bl_label = "Save Nodes To Library"

    name: bpy.props.StringProperty(name = "Node Name: ", description = "The Name of the exported Nodes", default = "exported_node")
    library: bpy.props.StringProperty(name = "Library Name: ", description = "The Name of the Library into which the noder are being exported", default = "exported_nodes")
    category: bpy.props.StringProperty(name = "Node Category: ", description = "The Category of the exported Nodes", default = "exported_nodes")
    
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    def execute(self, context):

        invalidCharacters = [" ", ".", "/", "\\", ":", ";"]
        def replaceInvalidCharacters(name):
            valid = name
            for c in invalidCharacters:
                valid = valid.replace(c, "_")
            return valid

        library_name = self.library
        node_name = self.name
        fp = arm.utils.get_fp()

        lfp = fp+"/Libraries"
        
        if not os.path.exists(lfp):
            os.makedirs(lfp)

        enfp = lfp+"/"+library_name
        
        if not os.path.exists(enfp):
            os.makedirs(enfp)

        # create blender.py to load the nodes
        bl_file = open(enfp+"/blender.py", "w")
        bl_file.write("import arm.nodes_logic\n")
        bl_file.write("from "+library_name+"_definitions import *\n")
        bl_file.write("def register():\n")
        bl_file.write("\tarm.nodes_logic.register_nodes()\n")
        
        ndfp = enfp+"/"+library_name+"_definitions"

        if not os.path.exists(ndfp):
            os.makedirs(ndfp)

        # create init so this dir can be imported

        init_file = open(ndfp+"/__init__.py", "w")
        init_file.write("# Import all nodes\n")
        init_file.write("from os.path import dirname, basename, isfile\n")
        init_file.write("import glob\n")
        init_file.write("modules = glob.glob(dirname(__file__)+\"/*.py\")\n")
        init_file.write("__all__ = [basename(f)[:-3] for f in modules if isfile(f)]\n")

        # since the file name is hardcoded, append an index to avoid overriding the file
        file_name = node_name + "_"
        index = 0
        while os.path.isfile(ndfp+"/"+file_name+str(index)+".py"):
            index += 1
        file_name += str(index) + ".py"
            
        node_file = open(ndfp+"/"+file_name,"w")
        node_file.write("import bpy\n")
        node_file.write("from bpy.props import *\n")
        node_file.write("from bpy.types import Node, NodeSocket\n")
        node_file.write("from arm.logicnode.arm_nodes import *\n")
        
        # give the node the same name that is used for the file for now...
        node_file.write("class {0}(Node, ArmLogicTreeNode):\n".format(node_name+"_"+str(index)))
        node_file.write("\t'''{0}'''\n".format(node_name+"_"+str(index)))
        node_file.write("\tbl_idname=\"LN{0}\"\n".format(node_name+"_"+str(index)))
        node_file.write("\tbl_label=\"{0}\"\n".format(node_name))
        node_file.write("\tbl_icon=\"QUESTION\"\n")
        
        node_file.write("\tdef init(self, context):\n")
        node_file.write("\t\t# convenience functions\n")
        node_file.write("\t\tdef placeNodeWithOffset(node, reference, offset):\n")
        node_file.write("\t\t\tnode.location = [reference[0]+offset[0], reference[1]+offset[1]]\n\n")
            
        # node_file.write("\t\tdef selectNodes(node_tree, nodes):\n")
        # node_file.write("\t\t\tfor node in nodes:\n")
        # node_file.write("\t\t\t\tnode.select = True\n\n")
                    
        # node_file.write("\t\tdef frameNodes(node_tree, nodes, title):\n")
        # node_file.write("\t\t\tbpy.ops.node.select_all(action='DESELECT')\n")
        # node_file.write("\t\t\tselectNodes(node_tree, nodes)\n")
        # node_file.write("\t\t\tbpy.ops.node.join()\n")
        # node_file.write("\t\t\tframe = node_tree.active\n")
        # node_file.write("\t\t\tframe.label = title\n")
        # node_file.write("\t\t\treturn frame\n\n")
            
        node_file.write("\t\tdef linkNodes(node_links, node_1, node_2, output_socket_index, input_socket_index):\n")
        node_file.write("\t\t\tlinks.new(node_1.outputs[output_socket_index], node_2.inputs[input_socket_index])\n\n")

        node_file.write("\t\t# easy access\n")
        node_file.write("\t\tnode_tree_nodes = bpy.context.space_data.node_tree.nodes\n")
        node_file.write("\t\tlinks = bpy.context.space_data.node_tree.links\n")
        node_file.write("\t\tloc = bpy.context.space_data.cursor_location\n\n")
        
        
        node_tree = context.space_data.node_tree
        nodes = context.selected_nodes
        links = node_tree.links

        node_file.write("\t\t# add nodes to the tree\n")
        averageX = 0
        averageY = 0
        # add all nodes, also "compute" the average location
        for node in nodes:
            node_file.write("\t\tnode_{0} = node_tree_nodes.new(\"{1}\")\n".format(replaceInvalidCharacters(node.name), node.bl_idname))
            averageX += node.location[0]/len(nodes)
            averageY += node.location[1]/len(nodes)
        
        # position nodes, based on their distance to the average location
        node_file.write("\t\t# create node layout\n")
        for node in nodes:
            # print(node.bl_idname)
            if node.bl_idname != "NodeFrame":
                off_x = 0
                off_y = 0
                parent = node.parent
                while parent is not None:
                    # print("add "+parent.bl_idname+" offset")
                    off_x += parent.location[0]
                    off_y += parent.location[1]
                    parent = parent.parent
                node_file.write("\t\tplaceNodeWithOffset(node_{0}, loc, [{1}, {2}])\n".format(replaceInvalidCharacters(node.name), node.location[0] + off_x - averageX, node.location[1] + off_y - averageY))
                
        # handle frames
        node_file.write("\t\t# handle parenting, this is needed for frames\n")
        for node in nodes:
            if node.parent is not None:
                node_file.write("\t\tnode_{0}.parent = node_{1}\n".format(replaceInvalidCharacters(node.name), replaceInvalidCharacters(node.parent.name)))

        # handle labels
        node_file.write("\t\t# create labels\n")
        for node in nodes:
            node_file.write("\t\tnode_{0}.label = \"{1}\"\n".format(replaceInvalidCharacters(node.name), node.label))

        # handle values
        node_file.write("\t\t# set default input values\n")
        for node in nodes:
            for i in range(0, len(node.inputs)):
                inp = node.inputs[0]
                if "default_value" in dir(inp):
                    # print(type(inp.default_value))
                    if type(inp.default_value) is bpy.types.bpy_prop_array:
                        # print("Array")
                        for x in range(0, len(inp.default_value)):
                            # so string arrays even exist in blender nodes?
                            if type(inp.default_value[x]) is str:
                                node_file.write("\t\tnode_{0}.inputs.[{1}].default_value[{2}] = \"{3}\"\n".format(replaceInvalidCharacters(node.name), i, x, inp.default_value[x]))
                            else:
                                node_file.write("\t\tnode_{0}.inputs[{1}].default_value[{2}] = {3}\n".format(replaceInvalidCharacters(node.name), i, x, inp.default_value[x]))
                    else:
                        if type(inp.default_value) is str:
                            node_file.write("\t\tnode_{0}.inputs[{1}].default_value = \"{2}\"\n".format(replaceInvalidCharacters(node.name), i, inp.default_value))
                        else:
                            node_file.write("\t\tnode_{0}.inputs[{1}].default_value = {2}\n".format(replaceInvalidCharacters(node.name), i, inp.default_value))
                            # node_file.write("\t\tnode_{0}.label = \"{1}\"\n".format(replaceInvalidCharacters(node.name), node.label))

        # handle properties
        node_file.write("\t\t# set node properties like add/subtract on math node\n")
        for node in nodes:
            # print(dir(node))
            # print(node.__dir__)
            for attrib in dir(node):
                if attrib.startswith("property"):
                    # print(attrib)
                    # print(type(getattr(node, attrib)).__name__)
                    # print(callable(getattr(node, attrib)))
                    # print(node.__dict__)
                    # print(node.bl_idname)
                    # print(dir(node))
                    # print(attrib)
                    node_file.write("\t\ttry:\n")
                    if type(getattr(node, attrib)).__name__ == "str":
                        node_file.write("\t\t\tnode_{0}.{1} = \"{2}\"\n".format(replaceInvalidCharacters(node.name), attrib, getattr(node, attrib)))
                    else:
                        node_file.write("\t\t\tnode_{0}.{1} = {2}\n".format(replaceInvalidCharacters(node.name), attrib, getattr(node, attrib)))
                    node_file.write("\t\texcept:\n")
                    # this notifies a user of properties which failed to apply, not needed, only helpful for debugging
                    # node_file.write("\t\t\tprint(\"could not set {0} to {1} on node_{2}, this is most likely not problematic\")\n".format(attrib, getattr(node, attrib), node.name.replace(".", "_").replace(" ", "_")))
                    node_file.write("\t\t\tpass\n")

        # link nodes
        node_file.write("\t\t# create node links\n")
        for link in links:
            if link.from_node in nodes and link.to_node in nodes:
                # use path_from_id() to get somthing like nodes["Float"].outputs[0], then reverse with [::-1]
                # then use split to get only the part containing the index, reverse again, so the number is right and split again to remove the last bracket
                # somewhat like to cut | rev | cut ... in bash
                # print(link.from_socket.path_from_id()[::-1].split("[")[0][::-1].split("]")[0])
                node_file.write("\t\tlinkNodes(links, node_{0}, node_{1}, {2}, {3})\n".format(replaceInvalidCharacters(link.from_node.name), replaceInvalidCharacters(link.to_node.name), link.from_socket.path_from_id()[::-1].split("[")[0][::-1].split("]")[0], link.to_socket.path_from_id()[::-1].split("[")[0][::-1].split("]")[0]))

        # remove meta node
        node_file.write("\t\tnode_tree_nodes.remove(self)\n")
        # add node to armory
        node_file.write("add_node({0}, category='{1}')".format(node_name+"_"+str(index), self.category))

        return {'FINISHED'}
    
    @classmethod
    def poll(cls, context):
        return context.space_data != None and context.space_data.type == 'NODE_EDITOR'

bpy.utils.register_class(SaveSelectedNodesOperator)
