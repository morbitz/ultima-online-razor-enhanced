import math
from System.Collections.Generic import List

def pause_if_is_saving():
    if Journal.SearchByType('The world is saving, please wait.', 'Regular'):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(1000)
        Misc.SendMessage('Continuing', 33)
    Journal.Clear()

# Calculates distance between player and given coords
def distance(x1,y1):
    x2 = Player.Position.X
    y2 = Player.Position.Y
    return math.floor(math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)))
    
# Tries PathFindTo on exact coords and 1 square around to find a route
def pathfindNear(x, y, z, isItem):
    startX = Player.Position.X
    startY = Player.Position.Y
   
    for dx in [0, -1, 1]:
        for dy in [0, -1, 1]:
            pause_if_is_saving()
            # If it's an item, ignores the exact given coords and search 1 square around
            if (isItem and (dx == 0 and dy == 0)): continue
            # Just a debug code to see which path is choosed, you can safely comment out...
            Misc.SendMessage(str(dx) + ' ' + str(dy))
            Player.PathFindTo(x + dx, y + dy, z)
            # This pause added to wait PathFindTo calculate its route and check moving is started
            # Because PathFindTo runs async and returns nothing
            # You need to increase wait if you see many paths on previous SendMessage line
            Misc.Pause(280)
            if(startX != Player.Position.X or startY != Player.Position.Y): break
            
        if(startX != Player.Position.X or startY != Player.Position.Y): break
    
    # You can comment out these lines if you don't want to pause script till arrive to position
    while distance(x, y) > 1: Misc.Pause(290)
            
def pathfindToNearestItem(filter):
    item = Items.Select(Items.ApplyFilter(filter), 'Nearest')
    if item is None: return False
    Items.Message(item, 53, 'Come to me!')
    pathfindNear(item.Position.X, item.Position.Y, item.Position.Z, True)

def pathfindToNearestMobile(filter):
    mobile = Mobiles.Select(Mobiles.ApplyFilter(filter), 'Nearest')
    if mobile is None: return False
    Mobiles.Message(mobile, 53, 'Come to me!')
    pathfindNear(mobile.Position.X, mobile.Position.Y, mobile.Position.Z, False)
    
def pathfindToCoords(x, y, z):
    pathfindNear(x, y, z, False)
    Misc.Pause(7000)
    
def test():
    itemFilter = Items.Filter()
    itemFilter.RangeMax = 24
    itemFilter.OnGround = True
    itemFilter.Enabled = True
    itemFilter.Movable = False
    itemFilter.Graphics = List[int]((0x0EDC, 0x0EDC))

    mobileFilter = Mobiles.Filter()
    mobileFilter.RangeMax = 24

    pathfindToNearestMobile(mobileFilter)
    Misc.Pause(1000)
    #pathfindToNearestItem(itemFilter)
    # Misc.Pause(1000)
    #pathfindToCoords(Player.Position.X - 5, Player.Position.Y - 5, 0)
    
#pathfindToCoords(5387,81,20)
#Misc.Pause(60000)
#pathfindToCoords(5387,42,20)
#Misc.Pause(60000)

pathfindToCoords(5387,36,20)
pathfindToCoords(5387,48,20)
pathfindToCoords(5387,60,20)
pathfindToCoords(5387,72,20)
pathfindToCoords(5387,82,20)
pathfindToCoords(5387,90,20)
pathfindToCoords(5393,90,20)
pathfindToCoords(5398,90,11)
pathfindToCoords(5404,90,10)
pathfindToCoords(5404,83,10)
pathfindToCoords(5404,75,10)
pathfindToCoords(5404,80,10)
pathfindToCoords(5404,85,10)
pathfindToCoords(5404,91,10)
pathfindToCoords(5404,99,10)
pathfindToCoords(5404,106,10)
pathfindToCoords(5404,99,10)
pathfindToCoords(5404,91,10)
pathfindToCoords(5409,91,10)
pathfindToCoords(5415,91,11)
pathfindToCoords(5420,91,11)
pathfindToCoords(5426,91,20)
pathfindToCoords(5433,91,20)
pathfindToCoords(5439,91,20)
pathfindToCoords(5446,94,20)
pathfindToCoords(5451,101,20)
pathfindToCoords(5454,107,20)
pathfindToCoords(5453,115,20)

pathfindToCoords(5444,116,20)
pathfindToCoords(5440,116,20)
pathfindToCoords(5435,116,0)
pathfindToCoords(5430,115,0)
pathfindToCoords(5424,115,0)
pathfindToCoords(5422,111,0)
pathfindToCoords(5424,115,0)
pathfindToCoords(5430,115,0)
pathfindToCoords(5435,116,0)
pathfindToCoords(5440,115,20)
pathfindToCoords(5453,115,20)
pathfindToCoords(5459,115,20)
pathfindToCoords(5467,115,35)
pathfindToCoords(5467,110,35)
pathfindToCoords(5467,106,35)
pathfindToCoords(5468,109,35)
pathfindToCoords(5468,115,35)
pathfindToCoords(5473,115,33)
pathfindToCoords(5478,115,33)
pathfindToCoords(5484,115,20)
pathfindToCoords(5489,109,20)
pathfindToCoords(5492,106,20)
pathfindToCoords(5491,100,35)
pathfindToCoords(5491,94,35)
pathfindToCoords(5491,89,35)
pathfindToCoords(5487,87,35)
pathfindToCoords(5487,81,35)
pathfindToCoords(5484,84,35)
pathfindToCoords(5478,81,35)
pathfindToCoords(5471,80,35)
pathfindToCoords(5468,84,29)
pathfindToCoords(5463,84,29)
pathfindToCoords(5458,86,29)
pathfindToCoords(5453,88,20)
pathfindToCoords(5449,90,20)
pathfindToCoords(5444,92,20)
pathfindToCoords(5438,91,20)
pathfindToCoords(5432,91,20)
pathfindToCoords(5428,91,20)
pathfindToCoords(5423,91,20)
pathfindToCoords(5418,91,20)
pathfindToCoords(5414,91,20)
pathfindToCoords(5408,91,20)
pathfindToCoords(5404,91,20)
pathfindToCoords(5400,91,20)
pathfindToCoords(5394,91,20)
pathfindToCoords(5390,87,20)
pathfindToCoords(5387,84,20)
pathfindToCoords(5387,90,20)
pathfindToCoords(5387,95,20)
pathfindToCoords(5387,100,20)
pathfindToCoords(5387,105,20)
pathfindToCoords(5390,108,20)
pathfindToCoords(5492,111,20)
pathfindToCoords(5387,103,20)
pathfindToCoords(5387,94,20)
pathfindToCoords(5387,92,20)
pathfindToCoords(5387,86,20)
pathfindToCoords(5387,80,20)
pathfindToCoords(5387,76,20)
pathfindToCoords(5387,69,20)
pathfindToCoords(5387,63,20)
pathfindToCoords(5387,55,20)
pathfindToCoords(5387,46,20)
pathfindToCoords(5387,36,20)