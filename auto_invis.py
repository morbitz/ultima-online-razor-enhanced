g = Player.Serial #keeps your character invisible

while True:
    Misc.SendMessage('AUTO INVIS RUNNING')
    if Player.Visible == True:
        Spells.CastMagery("Invisibility")
        Misc.Pause(2600)
        Target.TargetExecute(g)
    Misc.Pause(600)