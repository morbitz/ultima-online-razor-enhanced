# UBER Treasure Mapper
# ITS RICKY BITCH


Misc.SendMessage('Starting UBER Treasure Mapper')


msgColor = 68
self = Mobiles.FindBySerial( Player.Serial )

from Scripts import config
from Scripts.glossary.items.armor import armor
from Scripts.glossary.items.clothing import clothingInTreasureChests
from Scripts.glossary.items.gems import gems
from Scripts.glossary.items.reagents import reagents
from Scripts.glossary.items.shields import shields
from Scripts.glossary.items.spellScrolls import spellScrolls
from Scripts.glossary.items.weapons import weapons
from Scripts.utilities.items import FindItem, MoveItem
from Scripts.glossary.colors import colors

def GetBag ( sharedValue, promptString ):

    bag = Target.PromptTarget( promptString )
    Misc.SetSharedValue( sharedValue, bag )
    return bag

# Check for reg bag
Target.ClearQueue()
keepBag = GetBag( 'keepBag', 'Select Bag for stuff to keep' )
trashCan = GetBag( 'trashCan', 'Select Corpse to dump on' )

chest = Target.PromptTarget( 'Select Treasure Chest' )


mapChest = Items.FindBySerial( chest )
if mapChest == None or not mapChest.IsContainer:
    Misc.SendMessage( 'Invalid treasure chest! Try running again', colors[ 'red' ] )
    Stop

#loot includes gate, recall & lvl 8 summoning scrolls
loot = [ 0x2260, 0x1f4c, 0x1f60, 0x1f66, 0x1f68, 0x1f69, 0x1f6a, 0x1f6b, 0x1f6c ]

gold = [ 0x0EED ]
wands = [ 0xdf5, 0xdf3, 0xdf4, 0xdf2 ]

armorIDs = [ armor[ item ].itemID for item in armor ]
gemIDs = [ gems[ gem ].itemID for gem in gems ]
reagentIDs = [ reagents[ reagent ].itemID for reagent in reagents ]
shieldIDs = [ shields[ shield ].itemID for shield in shields ]
trashIDs = [ clothingInTreasureChests[ item ].itemID for item in clothingInTreasureChests ]
weaponIDs = [ weapons[ weapon ].itemID for weapon in weapons ]
scrollIDs = [ spellScrolls[ scroll ].itemID for scroll in spellScrolls ]


Items.UseItem( mapChest )
Misc.Pause( config.dragDelayMilliseconds )

def checkDistance():
    if not Player.InRangeItem( mapChest, 2 ):
        Timer.Create( 'Distance', 1 )
        while not Player.InRangeItem( mapChest, 2 ):
            if not Timer.Check( 'Distance' ):
                Player.HeadMessage( msgColor, 'Too Far Away' )
                Timer.Create( 'Distance', 2500 )
        Items.UseItem( mapChest )
        Misc.Pause( 800 )


def checkWeight():
    if Player.Weight >= Player.MaxWeight:
        Player.ChatSay(msgColor, 'I am Overweight, stopping')
        Stop

rdaFrag = Items.FindByID( 0x0F21, 0x0489, mapChest.Serial )
if rdaFrag != None:
    MoveItem( Items, Misc, rdaFrag, Player.Backpack )
    Misc.SendMessage('RDA FRAG FOUND')
    Player.ChatGuild('RDA FRAG FOUND')
    
# Move the trash into the trash can
for item in mapChest.Contains:
    checkDistance()
    #checkWeight()
    if item.ItemID in trashIDs:
        MoveItem( Items, Misc, item, trashCan )
        Misc.Pause(800)


for item in mapChest.Contains:
    checkDistance()
    #checkWeight()
    if item.ItemID in scrollIDs:
        MoveItem( Items, Misc, item, trashCan )
        Misc.Pause(800)

        
for item in mapChest.Contains:
    checkDistance()
    #checkWeight()
    MoveItem( Items, Misc, item, keepBag )
    Misc.Pause(800)


Player.ChatSay( msgColor, 'Got it all, let''s bounce!' )