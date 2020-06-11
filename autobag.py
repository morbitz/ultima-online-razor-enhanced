def autobag():
    Misc.SendMessage('BAG EXPLOIT ACTIVE')
    while True:
        Items.UseItem(0x42B03651)
        Misc.Pause(1100)
    Misc.SendMessage('BAG EXPLOIT DEACTIVATED')

autobag()
