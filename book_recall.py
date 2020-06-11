if Player.Name == 'bicky pit':
    book_id = 0x42DABE5F

Items.UseItem(book_id)
Gumps.WaitForGump(1431013363, 10000)
Gumps.SendAction(1431013363, 2)

Misc.Pause(1800)
if Player.Direction != 'North':
    Player.Walk('North')
    Misc.Pause(100)
Player.Run('North')
Player.Run('North')
Player.Run('North')
