def for_loop(my_selection = cmds.ls(selection=True)):
    for obj in my_selection:
        print(obj)

for_loop()
