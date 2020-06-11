# human xerox copy
# You must add your beetle to Agents -> Friends -> Active Friend List


def open_beetle():
    petFilter = Mobiles.Filter()
    petFilter.RangeMin = 0
    petFilter.RangeMax = 1
    petFilter.IsHuman = 0
    petFilter.IsGhost = 0
    petFilter.Friend = 1
    pets = Mobiles.ApplyFilter( petFilter )
    for p in pets:
        if p.Body == 0x0317:
            Misc.WaitForContext(pets[0], 10000)
            Misc.Pause(600)
            Misc.ContextReply(pets[0], 'Open Backpack')

            
open_beetle()
