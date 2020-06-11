# invis me
BICKY = 0x001626CE
Journal.Clear()
while Player.Hits > 0:
    if Journal.Search('heal me'):
        Journal.Clear()
        Spells.CastMagery('Greater Heal')
        Target.WaitForTarget(2300, True)
        Target.TargetExecute(BICKY)
    Misc.Pause(500)