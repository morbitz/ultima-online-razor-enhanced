bandaging = False
bandage_counter = 0
Items.UseItemByID(0x0E21)
Misc.Pause(200)
Journal.Clear()
Target.TargetExecute(Player.Serial)
Misc.Pause(200)

if not Journal.Search('begin applying'):
    Player.HeadMessage(66, 'No bandages or not damaged')
    STOP

bandaging = True
while bandaging:
    if Journal.Search('finish applying'):
        bandaging = False
        break
        
    Player.HeadMessage(69, str(bandage_counter))
    Misc.Pause(1000)
    bandage_counter += 1