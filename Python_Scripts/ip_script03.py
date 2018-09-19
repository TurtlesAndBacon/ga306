import maya.cmds as cmds
import maya.mel as mel

def create_imagePlanes():
    front_ip = cmds.imagePlane(
        name="front_IP",
        width=100,
        height=100,
        lookThrough="front",
        showInAllViews=False)
    cmds.imagePlane(front_ip , edit = True, showInAllViews=True)
    print(cmds.imagePlane(front_ip, query = True))
    cmds.imagePlane(front_ip , edit = True, showInAllViews=False)
    cmds.move(0,0,-950)
    cmds.imagePlane(
        name="side_IP",
        width=100,
        height=100,
        lookThrough="side",
        showInAllViews=False)
    cmds.move(-950,0,0)
    cmds.rotate(0,90,0)
    cmds.imagePlane(
        name="back_IP",
        width=100,
        height=100,
        lookThrough="back",
        showInAllViews=False)
    cmds.move(0,0,950)
    cmds.rotate(0,180,0)

def create_backCam():
    backCam=cmds.camera(name="back", hc="cmds.viewSet(b=True)")
    mel.eval('lookThroughModelPanel '+ backCam[0]+' modelPanel1;')
    mel.eval('viewSet -b `modelEditor -q -camera modelPanel1`;')
    if backCam[0]!="back":
        cmds.rename(backCam[0], 'back')
        getShapeNode=mel.eval('pickWalk -d down')[0]

create_backCam()
create_imagePlanes()
