while Player.Hits > 0:
    if Player.Mana < 40:
        Player.UseSkill('Meditation')
        Misc.Pause(12000)
    Spells.CastMagery('Mana Vampire')
    Misc.Pause(2700)
    Target.TargetExecute(0x0027AECA)
    Misc.Pause(600)