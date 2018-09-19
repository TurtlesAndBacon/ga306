import maya.cmds as cmds
import maya.mel as mel

def create_imagePlanes():
    front_ip = cmds.imagePlane(
        name="front_IP",
        fileName="front_ref.jpg",
        lookThrough="front",
        showInAllViews=False)
    cmds.move(0,0,-950)
    front_ref_L = cmds.createDisplayLayer(name="front_ref_L")
    cmds.setAttr("{}.displayType".format(front_ref_L), 2)
    cmds.imagePlane(
        name="side_IP",
        fileName="side_ref.jpg",
        lookThrough="side",
        showInAllViews=False)
    cmds.move(-950,0,0)
    cmds.rotate(0,90,0)
    side_ref_L = cmds.createDisplayLayer(name="side_ref_L")
    cmds.setAttr("{}.displayType".format(side_ref_L), 2)
    cmds.imagePlane(
        name="back_IP",
        fileName="back_ref.jpg",
        lookThrough="back",
        showInAllViews=False)
    cmds.move(0,0,950)
    cmds.rotate(0,180,0)
    back_ref_L = cmds.createDisplayLayer(name="back_ref_L")
    cmds.setAttr("{}.displayType".format(back_ref_L), 2)

def create_backCam():
    backCam=cmds.camera(name="back", hc="cmds.viewSet(b=True)")
    mel.eval('lookThroughModelPanel '+ backCam[0]+' modelPanel1;')
    mel.eval('viewSet -b `modelEditor -q -camera modelPanel1`;')
    if backCam[0]!="back":
        cmds.rename(backCam[0], 'back')
        getShapeNode=mel.eval('pickWalk -d down')[0]

create_backCam()
create_imagePlanes()
