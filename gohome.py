PLAYERS = {
    'human xerox copy': {'book_serial': 0x41A6D2E0, 'type': 'mage'},
    'Belcasor': {'book_serial': 0x4013AEE6, 'type': 'mage'},
    'bicky pit': {'book_serial': 0x42DABE5F, 'type': 'dexer'},
    'vintage': {'book_serial': 0x401EC72C, 'type': 'dexer'},
    'Ricky The Hand': {'book_serial': 0x427FFF44, 'type': 'dexer'},
    'watto': {'book_serial': 0x40A1F5F0, 'type': 'dexer'},
    'new fettuccine': {'book_serial': 0x466414BA, 'type': 'mage'},
    'tEnTinQUaRaNtinO': {'book_serial': 0x41A2ECA2, 'type': 'dexer'}
}

book_serial = PLAYERS[Player.Name]['book_serial']
type = PLAYERS[Player.Name]['type']

def dexer(book_serial):
    Items.UseItem(book_serial)
    Misc.Pause(100)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 2)

def mage(book_serial):
    Spells.CastMagery("Recall")
    Misc.Pause(1700)
    Target.TargetExecute(book_serial)
    
if type == 'dexer':
    dexer(book_serial)
else:
    mage(book_serial)