import maya.cmds as cmds

cmds.polyCube()
cmds.polySphere()
cmds.polyCylinder()
cmds.polyTorus()

# I manually parented the torus to the cylinder, cylinder to the sphere,
# and the sphere to the cube.
# I had trouble finding the correct python command to parent one object to another.
# Everything I found regarding parenting was related to rigging.

def print_parents():
    firstObj = cmds.ls(selection=True)
    temp = firstObj
    parentObj = cmds.listRelatives(temp, parent=True)

    while parentObj != None:
        firstObj.append(parentObj[0])
        temp = parentObj
        parentObj = cmds.listRelatives(temp, parent=True)
        print(firstObj[1:])
        return firstObj

def print_Parents(nodeList):
   a = nodeList[0]
   b = nodeList[1:]
   print('Selected Node: %s, Parents: %s' %(a, b))

print_Parents(getParentList())
