def mount_beetle():
    Player.ChatSay('mount beetle')
    petFilter = Mobiles.Filter()
    petFilter.RangeMin = 0
    petFilter.RangeMax = 1
    petFilter.IsHuman = 0
    petFilter.IsGhost = 0
    petFilter.Friend = 1
    pets = Mobiles.ApplyFilter( petFilter )
    for p in pets:
        if p.Body == 0x0317:
            p.Mount

mount_beetle()
