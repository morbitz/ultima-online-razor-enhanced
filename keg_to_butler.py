POTS = {
    'REFRESH': 0x0F0B,
    'HEAL': 0x0F0C,
    'STRENGTH': 0x0F09,
    'EXPLO': 0x0F0D,
    'CURE': 0x0F07,
    'AGILITY': 0x0F08
}



REGS = {
    'HEAL': 0x0F85,
    'REFRESH': 0x0F7A,
    'STRENGTH': 0x0F86,
    'EXPLO': 0x0F8C,
    'CURE': 0x0F84,
    'AGILITY': 0x0F7B
}

to_make = 'EXPLO'
pot = POTS[to_make]
reg = REGS[to_make]


while Player.Hits > 0:
    msg = ''
    try:
        msg = list(Gumps.LastGumpGetLineList())[6]
    except:
        pass
    if Journal.Search('worn out your tool'):
        Items.UseItemByID(0x0E9B)
        Misc.Pause(600)
        Journal.Clear()
    if 'bottle' in msg:
        Items.Move(0x41E63765, 0x000F42D2, 0)
        Misc.Pause(600)
        Items.Move(Items.FindByID(pot, -1, -1), 0x41E63765, 0)
        Misc.Pause(600)
        msg = ''
    if 'You do not have enough' in msg:
        reg_reserve = Items.FindByID(reg, -1, 0x4577823A)
        Items.Move(reg_reserve, Player.Backpack, 1100)

    Gumps.SendAction(949095101, 21)
    Misc.Pause(600)
    
