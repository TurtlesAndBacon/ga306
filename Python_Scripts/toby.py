import maya.cmds as cmds

def getParentList():

   startingNode = cmds.ls(selection=True)
   tempNode = startingNode
   parentNode = cmds.listRelatives(tempNode, parent=True)

   while parentNode != None:
       startingNode.append(parentNode[0])
       tempNode=parentNode
       parentNode = cmds.listRelatives(tempNode, parent=True)
   print(startingNode[1:])
   return startingNode

def print_Parents(nodeList):
   a = nodeList[0]
   b = nodeList[1:]
   print('Selected Node: %s, Parents: %s' %(a, b))

print_Parents(getParentList())
Message Input

Message @Tobias
