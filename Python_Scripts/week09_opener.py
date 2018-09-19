import maya.cmds as cmds


def create_geo(size=4):
    cmds.polyCube(w=size, h=size, d=size)
    cmds.move(0,0,-10)
    cmds.polyCylinder(r=size)
    cmds.polySphere(r=size)
    cmds.move(0,0,10)

create_geo()
