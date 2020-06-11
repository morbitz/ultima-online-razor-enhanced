# Auto Scavenger by athL33T
# May 6, 2020
from System.Collections.Generic import List

class Scavenger(object):
    def __init__(self):
        self.loot = List[int]([
            0x705D, # bigass ettin statue
            0x20E9, # troll statue
            0x20DF, # ogre statue
            0x212E, # titan statue
            0x212D, # cyclops statue
            0x25CD, # other titan statue
            0x20CD, # male statue
            0x20CE, # female statue
            0x20D8, # ettin statue
            0x14F0, # power scroll
            0x2260, # skill scroll
            0x0F21, # portal frag
            0x35DA, # rda frag
            0x1CE1, # head
            0x47E6, # dragon egg
            0x410B, # asylum key
            0x2831, # title scroll
            0x2AA4, # relic
            0x14F0, # bank cheque
            0x707E, # giant cyclops
            0x7004, # ancient troll
            0x1BFB,
            0x0F3F
        ])
        self.to_scav = List[int]([])
        
    def get_proximate_ground_items(self):
        proximate_ore_piles = []
        ground_items_filter = Items.Filter()
        ground_items_filter.Movable = True
        ground_items_filter.OnGround = 1
        ground_items_filter.RangeMax = 0
        ground_items_filter.RangeMax = 2
        ground_items_filter.Graphics = List[int]( self.loot )
        
        self.ground_items = Items.ApplyFilter(ground_items_filter)
    
    def grab(self):
        self.to_scav = Items.Select(self.ground_items, 'Nearest')
        if self.to_scav:
            Items.Move(self.to_scav, Player.Backpack.Serial, -1)
            Misc.Pause(600)
        
Player.HeadMessage(66, 'Starting Scavenger')
scavenger = Scavenger()

while Player.Hits > 0:
    scavenger.get_proximate_ground_items()
    scavenger.grab()
    Misc.Pause(50)
