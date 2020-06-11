while Player.Hits > 0:
    Player.UseSkill('Detect Hidden')
    Misc.Pause(600)
    Target.TargetExecuteRelative(Player.Serial, 0)
    Misc.Pause(2400)