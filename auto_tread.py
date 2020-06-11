while True:
    if Player.Hits < 65:
        Items.UseItemByID(0x0E21)
        Misc.Pause(900)
        Target.TargetExecute(0x001626CE)
        Misc.Pause(900)
    Player.Walk('East')
    Misc.Pause(600)
    Player.Walk('West')
    Misc.Pause(600)
    Player.Walk('West')
    Misc.Pause(600)
    Player.Walk('East')
    Misc.Pause(22000)
        