import maya.cmds as cmds

def rename_obj(new_name):
    my_selection= cmds.ls(selection=True)
    cmds.rename(my_selection, new_name)

rename_obj('disco_ball')
