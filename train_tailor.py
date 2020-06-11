ITEMS = {
    'CLOAK': 0x1515,
    'OILCLOTH': 0x175D,
    'ROBES': 0x1F03,
    'SCISSORS': 0x0F9F
}

item = ITEMS['OILCLOTH']

while Player.Hits > 0:
    if Journal.Search('tool'):
        Items.UseItemByID(0x0F9D)
        Misc.Pause(600)
        Journal.Clear()
    
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 21)
    
    Misc.Pause(600)
    if Items.FindByID(item, -1, Player.Backpack.Serial) is not None:
        Items.UseItemByID(ITEMS['SCISSORS'])
        Misc.Pause(600)
        Target.TargetExecute(Items.FindByID(item, -1, Player.Backpack.Serial))
        Misc.Pause(600)
