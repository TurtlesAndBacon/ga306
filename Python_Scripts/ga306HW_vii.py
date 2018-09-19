import maya.cmds as cmds

cmds.polySphere()
cmds.spaceLocator()
cmds.connectAttr('locator1' + '.translateY', 'pSphere1' + '.scaleX')
cmds.connectAttr('locator1' + '.translateY', 'pSphere1' + '.scaleY')
cmds.connectAttr('locator1' + '.translateY', 'pSphere1' + '.scaleZ')
