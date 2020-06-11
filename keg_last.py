while True:
    if Journal.Search('tool'):
        Items.UseItemByID(0x0E9B)
        Misc.Pause(300)
    
    Gumps.SendAction(949095101, 21)
    Misc.Pause(660)