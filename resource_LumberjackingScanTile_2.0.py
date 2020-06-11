#********************
beetle = 0x000697BF
autoFightMacroName = 'AttackGrey.py'
logsToBoards = False
# Trees where there is no longer enough wood to be harvested will not be revisited until this much time has passed
treeCooldown = 1200000 # 1,200,000 ms is 20 minutes
#********************

# Parameters
scanRadius = 15
treeStaticIDs = [ 0x0C95, 0x0C96, 0x0C99, 0x0C9B, 0x0C9C, 0x0C9D, 0x0C8A, 0x0CA6,
    0x0CA8, 0x0CAA, 0x0CAB, 0x0CC3, 0x0CC4, 0x0CC8, 0x0CC9, 0x0CCA, 0x0CCB,
    0x0CCC, 0x0CCD, 0x0CD0, 0x0CD3, 0x0CD6, 0x0CD8, 0x0CDA, 0x0CDD, 0x0CE0,
    0x0CE3, 0x0CE6, 0x0CF8, 0x0CFB, 0x0CFE, 0x0D01, 0x0D25, 0x0D27, 0x0D35,
    0x0D37, 0x0D38, 0x0D42, 0x0D43, 0x0D59, 0x0D70, 0x0D85, 0x0D94, 0x0D96,
    0x0D98, 0x0D9A, 0x0D9C, 0x0D9E, 0x0DA0, 0x0DA2, 0x0DA4, 0x0DA8, ]
    
if Misc.ShardName() == 'Ultima Forever':
    treeStaticIDsToRemove = [ 0x0C99, 0x0C9A, 0x0C9B, 0x0C9C, 0x0C9D, 0x0CA6, 0x0CC4, ]
    for treeStaticIDToRemove in treeStaticIDsToRemove:
        if treeStaticIDToRemove in treeStaticIDs:
            treeStaticIDs.remove( treeStaticIDToRemove )
    
#axeSerial = None
EquipAxeDelay = 1000
TimeoutOnWaitAction = 4000
ChopDelay = 1000
runebookBank = 0x41EA8DEE # Runebook for bank
runebookTrees = 0x41EA8DEE # Runebook for tree spots
recallPause = 3000
dragDelay = 600
logID = 0x1BDD
boardID = 0x1BD7
otherResourceID = [ 0x318F, 0x3199, 0x2F5F, 0x3190, 0x3191, ]
logBag = 0x401FA597 # Serial of log bag in bank
otherResourceBag = 0x40191C19 # Serial of other resource in bank
weightLimit = Player.MaxWeight - 10
bankX = 2051
bankY = 1343
axeList = [ 0x0F49, 0x13FB, 0x0F47, 0x1443, 0x0F45, 0x0F4B, 0x0F43 ]
rightHand = Player.CheckLayer( 'RightHand' )
leftHand = Player.CheckLayer( 'LeftHand' )


# System Variables
from System.Collections.Generic import List
from math import sqrt
tileinfo = List[Statics.TileInfo]
trees = []
treeCoords = None
blockCount = 0
lastRune = 5
onLoop = True

class Tree:
    x = None
    y = None
    z = None
    id = None
    
    def __init__ ( self, x, y, z, id ):
        self.x = x
        self.y = y
        self.z = z
        self.id = id


def RecallNextSpot():
    global lastRune

    Gumps.ResetGump()

    Misc.SendMessage('--> Recall to Spot', 77)

    Items.UseItem( runebookTrees )
    Gumps.WaitForGump( 1431013363, TimeoutOnWaitAction )
    Gumps.SendAction( 1431013363, lastRune )

    Misc.Pause( recallPause )

    lastRune = lastRune + 6
    if lastRune > 95:
        lastRune = 5

    EquipAxe()


def RecallBack():
    global lastRune

    Items.UseItem( runebookTrees )
    Gumps.WaitForGump( 1431013363, TimeoutOnWaitAction )
    Gumps.SendAction( 1431013363, lastRune )

    Misc.Pause( recallPause )

    EquipAxe()


def DepositInBank():
    global bankX
    global bankY
    while Player.Weight >= weightLimit:
        Gumps.ResetGump()
        Items.UseItem( runebookBank )
        Gumps.WaitForGump( 1431013363, 10000 )
        Gumps.SendAction( 1431013363, 71 )
        Misc.Pause( recallPause )

        Player.ChatSay( 77, 'bank' )
        Misc.Pause( 300 )

        if Items.BackpackCount( logID, -1 ) > 0:
            while Items.BackpackCount( logID, -1 ) > 0:
                Misc.SendMessage( '--> Moving Log', 77 )
                Items.Move( item, logBag, 0 )
                Misc.Pause( dragDelay )

        if Items.BackpackCount( boardID, -1 ) > 0:
            while Items.BackpackCount( boardID, -1 ) > 0:
                Misc.SendMessage( '--> Moving Log', 77 )
                Items.Move( item, logBag, 0 )
                Misc.Pause( dragDelay )

        for otherid in otherResourceID:
            if item.ItemID == otherid:
                Misc.SendMessage( '--> Moving Other', 77 )
                Items.Move( item, otherResourceBag, 0 )
                Misc.Pause( dragDelay )
            else:
                Misc.NoOperation()


def ScanStatic():
    global treenumber
    global trees
    Misc.SendMessage('--> Scan Tile Started', 77)
    minX = Player.Position.X - scanRadius
    maxX = Player.Position.X + scanRadius
    minY = Player.Position.Y - scanRadius
    maxY = Player.Position.Y + scanRadius

    x = minX
    y = minY

    while x <= maxX:
        while y <= maxY:
            staticsTileInfo = Statics.GetStaticsTileInfo( x, y, Player.Map )
            if staticsTileInfo.Count > 0:
                for tile in staticsTileInfo:
                    for staticid in treeStaticIDs:
                        if staticid == tile.StaticID and not Timer.Check( '%i,%i' % ( x, y ) ):
                            #Misc.SendMessage( '--> Tree X: %i - Y: %i - Z: %i' % ( minX, minY, tile.StaticZ ), 66 )
                            trees.Add( Tree( x, y, tile.StaticZ, tile.StaticID ) )
            y = y + 1
        y = minY
        x = x + 1

    trees = sorted( trees, key = lambda tree: sqrt( pow( ( tree.x - Player.Position.X ), 2 ) + pow( ( tree.y - Player.Position.Y ), 2 ) ) )
    Misc.SendMessage( '--> Total Trees: %i' % ( trees.Count ), 77 )


def RangeTree():
    playerX = Player.Position.X
    playerY = Player.Position.Y
    treeX = trees[ 0 ].x
    treeY = trees[ 0 ].y
    if ( ( treeX >= playerX - 1 and treeX <= playerX + 1 ) and ( treeY >= playerY - 1 and treeY <= playerY + 1 )  ):
        return True
    else:
        return False


def MoveToTree():
    global trees
    global treeCoords
    pathlock = 0
    Misc.SendMessage( '--> Moving to TreeSpot: %i, %i' % ( trees[ 0 ].x, trees[ 0 ].y ), 77 )
    Misc.Resync()
    treeCoords = PathFinding.Route()
    treeCoords.MaxRetry = 5
    treeCoords.StopIfStuck = False
    treeCoords.X = trees[ 0 ].x
    treeCoords.Y = trees[ 0 ].y + 1
    
    if PathFinding.Go( treeCoords ):
        #Misc.SendMessage('First Try')
        Misc.Pause( 1000 )
    else:
        Misc.Resync()
        treeCoords.X = trees[ 0 ].x + 1
        treeCoords.Y = trees[ 0 ].y
        if PathFinding.Go( treeCoords ):
            Misc.SendMessage( 'Second Try' )
        else:
            treeCoords.X = trees[ 0 ].x - 1
            treeCoords.Y = trees[ 0 ].y
            if PathFinding.Go( treeCoords ):
                Misc.SendMessage( 'Third Try' )
            else:
                treeCoords.X = trees[ 0 ].x
                treeCoords.Y = trees[ 0 ].y - 1
                Misc.SendMessage( 'Final Try' )
                PathFinding.Go( treeCoords )

    Misc.Resync()

    while not RangeTree():
        CheckEnemy()
        Misc.Pause( 100 )
        pathlock = pathlock + 1
        if pathlock > 350:
            Misc.Resync()
            treeCoords = PathFinding.Route()
            treeCoords.MaxRetry = 5
            treeCoords.StopIfStuck = False
            treeCoords.X = trees[ 0 ].x
            treeCoords.Y = trees[ 0 ].y + 1
            
            if PathFinding.Go( treeCoords ):
                #Misc.SendMessage('First Try')
                Misc.Pause( 1000 )
            else:
                treeCoords.X = trees[ 0 ].x + 1
                treeCoords.Y = trees[ 0 ].y
                if PathFinding.Go( treeCoords ):
                    Misc.SendMessage( 'Second Try' )
                else:
                    treeCoords.X = trees[ 0 ].x - 1
                    treeCoords.Y = trees[ 0 ].y
                    if PathFinding.Go( treeCoords ):
                        Misc.SendMessage( 'Third Try' )
                    else:
                        treeCoords.X = trees[ 0 ].x
                        treeCoords.Y = trees[ 0 ].y - 1
                        Misc.SendMessage( 'Final Try' )
                        PathFinding.Go( treeCoords )

            pathlock = 0
            return

    Misc.SendMessage( '--> Reached TreeSpot: %i, %i' % ( trees[ 0 ].x, trees[ 0 ].y ), 77 )


def EquipAxe():
    global axeSerial

    if not leftHand:
        for item in Player.Backpack.Contains:
            if item.ItemID in axeList:
                Player.EquipItem( item.Serial )
                Misc.Pause( 600 )
                axeSerial = Player.GetItemOnLayer( 'LeftHand' ).Serial
    elif Player.GetItemOnLayer( 'LeftHand' ).ItemID in axeList:
        axeSerial = Player.GetItemOnLayer( 'LeftHand' ).Serial
    else:
        Player.HeadMessage( 35, 'You must have an axe to chop trees!' )
        Misc.Pause( 1000 )


def CutTree():
    global blockCount
    global trees
    if Target.HasTarget():
        Misc.SendMessage( '--> Detected block, canceling target!', 77 )
        Target.Cancel()
        Misc.Pause( 500 )

    if Player.Weight >= weightLimit:
        MoveToBeetle()
        MoveToTree()

    CheckEnemy()

    Journal.Clear()

    Items.UseItem( Player.GetItemOnLayer( 'LeftHand' ) )
    Target.WaitForTarget( TimeoutOnWaitAction , True )
    Target.TargetExecute( trees[ 0 ].x, trees[ 0 ].y, trees[ 0 ].z, trees[ 0 ].id )
    
    while not ( Journal.SearchByType( 'You hack at the tree for a while, but fail to produce any useable wood.', 'Regular' ) or 
            Journal.SearchByType( 'You chop some', 'Regular' ) or 
            Journal.SearchByType( 'There\'s not enough wood here to harvest.', 'Regular' ) ):
        Misc.Pause( 100 )

    if Journal.SearchByType( 'There\'s not enough wood here to harvest.', 'Regular' ):
        Misc.SendMessage( '--> Tree change', 77 )
        Timer.Create( '%i,%i' % ( trees[ 0 ].x, trees[ 0 ].y ), treeCooldown )
    elif Journal.Search( 'That is too far away' ):
        blockCount = blockCount + 1
        Journal.Clear()
        if blockCount > 5:
            blockCount = 0
            Misc.SendMessage( '--> Possible block detected tree change', 77 )
            Timer.Create( '%i,%i' % ( trees[ 0 ].x, trees[ 0 ].y ), treeCooldown )
        else:
            CutTree()
    elif Journal.Search( 'bloodwood' ):
        Player.HeadMessage( 1194, 'BLOODWOOD!' )
        CutTree()
    elif Journal.Search( 'heartwood' ):
        Player.HeadMessage( 1193, 'HEARTWOOD!' )
        CutTree()
    elif Journal.Search( 'frostwood' ):
        Player.HeadMessage( 1151, 'FROSTWOOD!' )
        CutTree()
    else:
        CutTree()


def CheckEnemy():
    enemy = Target.GetTargetFromList( 'enemy' )
    if enemy != None and enemy.WarMode:
        Misc.ScriptRun( autoFightMacroName )
        while enemy != None:
            Misc.Pause( 1000 )
            enemy = Mobiles.FindBySerial( enemy.Serial )
            if enemy:
                if Player.DistanceTo( enemy ) > 1:
                    enemyPosition = enemy.Position
                    enemyCoords = PathFinding.Route()
                    enemyCoords.MaxRetry = 5
                    enemyCoords.StopIfStuck = False
                    enemyCoords.X = enemyPosition.X
                    enemyCoords.Y = enemyPosition.Y - 1
                    PathFinding.Go( enemyCoords )

        corpseFilter = Items.Filter()
        corpseFilter.Movable = False
        corpseFilter.RangeMax = 2
        corpseFilter.Graphics = List[int]( [ 0x2006 ] )
        corpses = Items.ApplyFilter( corpseFilter )
        corpse = None

        Misc.Pause( dragDelay )

        for corpse in corpses:
            for item in corpse.Contains:
                if item.ItemID == logID:
                    Items.Move( item.Serial, Player.Backpack.Serial, 0 )
                    Misc.Pause( dragDelay )
                    
        PathFinding.Go( treeCoords )


def GetNumberOfBoardsInBeetle():
    global beetle
    global boardID
    global dragDelay

    remount = False
    if not Mobiles.FindBySerial( beetle ):
        remount = True
        Mobiles.UseMobile( Player.Serial )
        Misc.Pause( dragDelay )

    numberOfBoards = 0
    for item in Mobiles.FindBySerial( beetle ).Backpack.Contains:
        if item.ItemID == boardID:
            numberOfBoards += item.Amount

    if remount:
        Mobiles.UseItem( beetle )
        Misc.Pause( dragDelay )

    return numberOfBoards


def GetNumberOfLogsInBeetle():
    global beetle
    global logID
    global dragDelay

    remount = False
    if not Mobiles.FindBySerial( beetle ):
        remount = True
        Mobiles.UseMobile( Player.Serial )
        Misc.Pause( dragDelay )

    numberOfBoards = 0
    for item in Mobiles.FindBySerial( beetle ).Backpack.Contains:
        if item.ItemID == boardID:
            numberOfBoards += item.Amount

    if remount:
        Mobiles.UseItem( beetle )
        Misc.Pause( dragDelay )

    return numberOfBoards


def MoveToBeetle():
    # Chop logs into boards
    if logsToBoards:
        for item in Player.Backpack.Contains:
            if item.ItemID == logID:
                Items.UseItem( Player.GetItemOnLayer( 'LeftHand' ) )
                Target.WaitForTarget( 1500, False )
                Target.TargetExecute( item )
                Misc.Pause( dragDelay )

    if Player.Mount:
        Mobiles.UseMobile( Player.Serial )
        Misc.Pause( dragDelay )

    # Move boards to beetle, if they'll fit in the beetle
    for item in Player.Backpack.Contains:
        if logsToBoards and item.ItemID == boardID:
            numberOfBoardsInBeetle = GetNumberOfBoardsInBeetle()
            if numberOfBoardsInBeetle + i.Amount < 16000:
                Items.Move( i, beetle, 0 )
                Misc.Pause( dragDelay )
        elif not logsToBoards and item.ItemID == logID:
            numberOfBoardsInBeetle = GetNumberOfLogsInBeetle()
            if numberOfBoardsInBeetle + item.Amount < 16000:
                Items.Move( item, beetle, 0 )
                Misc.Pause( dragDelay )

    if not Player.Mount:
        Mobiles.UseMobile( beetle )
        Misc.Pause( dragDelay )


Misc.SendMessage('--> Start up Woods', 77)
EquipAxe()
while onLoop:
    #RecallNextSpot()
    ScanStatic()
    i = 0
    while trees.Count > 0:
        MoveToTree()
        CutTree()
        trees.pop( 0 )
        trees = sorted( trees, key = lambda tree: sqrt( pow( ( tree.x - Player.Position.X ), 2 ) + pow( ( tree.y - Player.Position.Y ), 2 ) ) )
    trees = []
    Misc.Pause( 100 )
