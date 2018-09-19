import maya.cmds
cmds.polySphere(sx=8, sy=8, r=10)
cmds.polyCube(w=15, h=15, d=15);
cmds.connectAttr('pSphere1.translate', 'pCube1.rotation')
