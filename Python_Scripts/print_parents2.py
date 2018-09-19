def print_parents(my_selection = cmds.ls(selection=True)):

    for object in my_selection:
       relative = cmds.listRelatives(object, parent=True)
       print('SELECTED OBJECT: %s, PARENT NODE: %s'%(object , relative))

print_parents(my_selection = cmds.ls(selection=True))  
