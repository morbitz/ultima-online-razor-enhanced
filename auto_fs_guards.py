'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019
Description: Finds the nearest enemy to attack. Prioritizes enemies in war mode
'''

from System.Collections.Generic import List
from System import Byte

def GetEmptyMobileList( Mobiles ):
    '''
    Creates a filter that returns an empty list, and then returns the empty list
    '''
    emptyFilter = Mobiles.Filter()
    emptyFilter.Enabled = True
    emptyFilter.Name = 'there_is_no_way this_is someones_name_since_its_way_too_long'
    return Mobiles.ApplyFilter( emptyFilter )

class Notoriety:
    byte = Byte( 0 )
    color = ''
    description = ''

    def __init__ ( self, byte, color, description ):
        self.byte = byte
        self.color = color
        self.description = description

notorieties = {
    'innocent': Notoriety( Byte( 1 ), 'blue', 'innocent' ),
    'ally': Notoriety( Byte( 2 ), 'green', 'guilded/ally' ),
    'attackable': Notoriety( Byte( 3 ), 'gray', 'attackable but not criminal' ),
    'criminal': Notoriety( Byte( 4 ), 'gray', 'criminal' ),
    'enemy': Notoriety( Byte( 5 ), 'orange', 'enemy' ),
    'murderer': Notoriety( Byte( 6 ), 'red', 'murderer' ),
    'npc': Notoriety( Byte( 7 ), '', 'npc' )
}

def GetNotorietyList ( notorieties ):
    '''
    Returns a byte list of the selected notorieties
    '''
    notorietyList = []
    for notoriety in notorieties:
        notorietyList.append( notoriety.byte )

    return List[Byte]( notorietyList )

def GetEnemyNotorieties( minRange = 0, maxRange = 12 ):
    '''
    Returns a list of the common enemy notorieties
    '''
    global notorieties

    return GetNotorietyList( [
        notorieties[ 'innocent' ]
    ] )

def GetEnemies( Mobiles, minRange = 0, maxRange = 12, notorieties = GetEnemyNotorieties(), IgnorePartyMembers = False ):
    '''
    Returns a list of the nearby enemies with the specified notorieties
    '''

    if Mobiles == None:
        raise ValueError( 'Mobiles was not passed to GetEnemies' )

    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.RangeMin = minRange
    enemyFilter.RangeMax = maxRange
    enemyFilter.Notorieties = notorieties
    enemyFilter.CheckIgnoreObject = True
    enemyFilter.Friend = False
    enemies = Mobiles.ApplyFilter( enemyFilter )

    if IgnorePartyMembers:
        partyMembers = [ enemy for enemy in enemies if enemy.InParty ]
        for partyMember in partyMembers:
            enemies.Remove( partyMember )

    return enemies

def FindEnemy():
    '''
    Returns the nearest enemy
    '''
    enemies = GetEnemies( Mobiles, 0, 12, GetEnemyNotorieties() )

    if len( enemies ) == 0:
        return None
    else:
        return Mobiles.Select( enemies, 'Nearest' )

Player.ChatSay(0,'Attack')
enemy = FindEnemy()
if enemy != None:
    Player.Attack( enemy )

while True:
    enemy = FindEnemy()
    while enemy.Hits > 0:
        if Player.Mana < 20:
            Player.UseSkill('Meditation')
            Misc.Pause(24000)
        if enemy != None:
            Spells.CastMagery('Energy Bolt')
            Misc.Pause(3500)
            Target.TargetExecute(enemy)
    Misc.Pause(2500)