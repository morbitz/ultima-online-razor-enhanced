while Player.Hits > 0:
    if Player.Hits < 90:
        Items.UseItemByID(0x0E21)
        Misc.Pause(630)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(9500)