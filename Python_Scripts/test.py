#import maya.cmds
#cmds.polySphere(sx=8, sy=8, r=10)
#cmds.polySphere(sx=8, sy=8, r=10)
#cmds.polySphere(sx=8, sy=8, r=10)
#cmds.polyCube(w=25, h=25, d=25);
#mult = maya.cmds.createNode('multiplyDivide');
#maya.cmds.connectAttr(pCube1+'.r', mult+'.input1X');
#maya.cmds.setAttr(mult+'.input2X', 1.0/90.0);
#maya.cmds.connectAttr(mult+'.outputX', pSphere1+'.ty');
#maya.cmds.select(pCube1);



#cmds.connectAttr('pCube1.rotate', 'pSphere1.ty', 'pSphere2.tx', 'pSphere3.tz')
