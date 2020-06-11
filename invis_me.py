# invis me
BICKY = 0x001626CE
Journal.Clear()
while Player.Hits > 0:
    if Journal.Search('invis me'):
        Journal.Clear()
        Spells.CastMagery('Invisibility')
        Target.WaitForTarget(2300, True)
        Target.TargetExecute(BICKY)
    Misc.Pause(500)