from Scripts.glossary.colors import colors
from System.Collections.Generic import List
from Scripts.glossary.enemies import GetEnemyNotorieties, GetEnemies
from Scripts.utilities.mobiles import GetEmptyMobileList

def FindEnemy():
    '''
    Returns the nearest enemy
    '''
    enemies = GetEnemies( Mobiles, 0, 12, GetEnemyNotorieties() )

    if len( enemies ) == 0:
        return None
    elif len( enemies ) == 1:
        return enemies[ 0 ]
    else:
        enemiesInWarMode = GetEmptyMobileList( Mobiles )
        enemiesInWarMode.AddRange( [ enemy for enemy in enemies if enemy.WarMode  ] )

        if len( enemiesInWarMode ) == 0:
            return Mobiles.Select( enemies, 'Nearest' )
        elif len( enemiesInWarMode ) == 1:
            return enemiesInWarMode[ 0 ]
        else:
            return Mobiles.Select( enemiesInWarMode, 'Nearest' )



if Player.Name == 'bicky pit':
    BUD = 0x00035097 # Ricky
    #BUD = 0x00010926 # vintage
    #BUD = Player.Serial
elif Player.Name == 'Ricky The Hand':
    BUD = 0x001626CE # bicky
if Player.Name == 'vintage':
    BUD = 0x001626CE # bicky
    #BUD = 0x0016218A # Thicc
    #BUD = 0x0003D75F # Richie Rich
if Player.Name == 'robin will ylems':
    BUD = 0x001626CE # bicky
    #BUD = 0x0016218A # Thicc
    #BUD = 0x0003D75F # Richie Rich
    

BANDAGES = Items.FindByID( 0x0E21, -1, -1 )
BUD_MOBILE = Mobiles.FindBySerial(BUD)
BANDAGE_MSG =  'Bandage started: ' + ' -> ' + BUD_MOBILE.Name

def heal_bud():
    if BUD_MOBILE.Hits < 25:
        if BANDAGES != None:
            Items.UseItem( BANDAGES )
            Target.WaitForTarget( 2000, False )
            Target.TargetExecute( BUD )
            Misc.SendMessage(BANDAGE_MSG, colors[ 'green' ])
        else:
            Misc.SendMessage('Out of bandages!', colors[ 'red' ])
        Misc.Pause(4500)

Misc.SendMessage('Auto-Heal initializing')
Journal.Clear()
while not Journal.Search('cancel'):
    if Player.Name != 'vintage' and Player.Name != 'robin will ylems':
        enemy = FindEnemy()
        if enemy != None:
            Player.Attack( enemy )
            Misc.Pause(900)
    heal_bud()
    Misc.Pause(900)
    
