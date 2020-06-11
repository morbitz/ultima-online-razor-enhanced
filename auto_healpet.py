BUD = 0x002E3F8F

BANDAGES = Items.FindByID( 0x0E21, -1, -1 )

def toggle_mount():
    if Player.Mount:
        Mobiles.UseMobile(Player.Serial)
    else:
        Mobiles.UseMobile(BUD)
        
def horsepuncher():
    BUD_MOBILE = Mobiles.FindBySerial(BUD)
    
    while Player.Hits < 55:
        if Player.Mount == None:
            toggle_mount()
            Misc.Pause(600)
        if BANDAGES != None:
            Items.UseItem( BANDAGES )
            Misc.Pause(600)
            Target.TargetExecute( Player.Serial )
            Misc.SendMessage('bandaging self')
        else:
            Misc.SendMessage('Out of bandages!', 83)
        Misc.Pause(600)
        Misc.Pause(13000)
        
    if Player.Mount:
        toggle_mount()
        Misc.Pause(600)
        Player.Attack( BUD )
        
    
    if BUD_MOBILE:
        BANDAGE_MSG =  'Bandage started: ' + Player.Name + ' -> ' + BUD_MOBILE.Name
        
        if BUD_MOBILE.Hits < 25:
            if BANDAGES != None:
                Items.UseItem( BANDAGES )
                Misc.Pause(600)
                Target.TargetExecute( BUD )
                Misc.SendMessage(BANDAGE_MSG)
            else:
                Misc.SendMessage('Out of bandages!', 83)
            Misc.Pause(4300)
    

Misc.SendMessage('Pet-Heal initializing')

while not Journal.Search('cancel'):
    horsepuncher()
    


