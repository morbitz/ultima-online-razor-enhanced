def release_pets():
    petFilter = Mobiles.Filter()
    petFilter.RangeMin = 0
    petFilter.RangeMax = 1
    petFilter.IsHuman = 0
    petFilter.IsGhost = 0
    pets = Mobiles.ApplyFilter( petFilter )

    for p in pets:
        Misc.WaitForContext(p, 10000)
        Misc.Pause(600)
        Misc.ContextReply(p, 'Release')
        Misc.Pause(600)

release_pets()
while True:
    Spells.CastMagery('Summon Creature')
    Misc.Pause(8100)
    release_pets()
    
    if Player.Mana < 80:
        Player.UseSkill('Meditation')
        Misc.Pause(9000)
