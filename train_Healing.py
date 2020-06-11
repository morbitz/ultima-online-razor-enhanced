target = Target.PromptTarget('Select target to train on')
#target = 0x001348D0
Player.HeadMessage(66,'hi')
while Player.Hits > 0:
    Items.UseItemByID(0x0E21)
    Misc.Pause(200)
    Target.TargetExecute(target)
    Misc.Pause(5000)
    Misc.Pause(100)