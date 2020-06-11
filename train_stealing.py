while Player.Hits > 0:
    Player.UseSkill("Stealing")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x4017CEA3)
    Misc.Pause(2400)
    Items.Move(0x4017CEA3, 0x400F5A53, 0)
    Misc.Pause(9000)
    