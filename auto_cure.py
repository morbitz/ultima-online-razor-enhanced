Misc.SendMessage('Auto-pot-chugger initializing')
while True:
    if Player.Poisoned:
        try:
            twoh = Player.GetItemOnLayer('LeftHand')
            Player.UnEquipItemByLayer('LeftHand')
            Misc.Pause(560)
        except:
            pass
        Items.UseItemByID(0x0F07)
        Misc.Pause(580)
        Player.EquipItem(twoh)
        Misc.Pause(1100)
    elif Player.Hits < 35:
        try:
            twoh = Player.GetItemOnLayer('LeftHand')
            Player.UnEquipItemByLayer('LeftHand')
            Misc.Pause(560)
        except:
            pass
        Items.UseItemByID(0x0F0C)
        Misc.Pause(580)
        Player.EquipItem(twoh)
        Misc.Pause(1100)