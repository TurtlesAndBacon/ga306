import maya.cmds as cmds

cmds.polySphere()

def rename_obj(new_name):
    my_selection = cmds.ls(selection=True)
    cmds.rename(my_selection, new_name)

rename_obj('Updated Name')
