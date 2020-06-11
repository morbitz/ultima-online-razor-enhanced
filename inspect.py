def inspect(var):
    if var:
        Misc.SendMessage('truthy')
    elif var == None:
        Misc.SendMessage('none-y')
    elif var == False:
        Misc.SendMessage('falsey')
    else:
        Misc.SendMessage('??: ' + str(var))