import maya.cmds as cmds

cmds.polySphere()
cmds.polyCube()

def rotate_trans():
    cmds.connectAttr('pCube1.rotate', 'pSphere1.translate')

rotate_trans()
