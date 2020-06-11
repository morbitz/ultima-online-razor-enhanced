bandaging = False
bandage_counter = 0
Player.HeadMessage(66, 'Target bandage')
bandage_target = Target.PromptTarget('Target bandage')
Items.UseItemByID(0x0E21)
Journal.Clear()
Target.TargetExecute(bandage_target)
Misc.Pause(200)

if not Journal.Search('begin applying'):
    Player.HeadMessage('Invalid target or no bandages')

bandaging = True
while bandaging:
    if Journal.Search('finish applying'):
        bandaging = False
        break
        
    Player.HeadMessage(69, str(bandage_counter))
    Misc.Pause(1000)
    bandage_counter += 1