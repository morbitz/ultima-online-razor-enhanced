while Items.FindByID(0x0EF3, -1, Player.Backpack.Serial) is not None:
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 42)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x4AAFA78D)
    Misc.Pause(50)