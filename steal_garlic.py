# Big item thief Script by MatsaMilla

escapeRunebook = 0x414D8007

import winsound
sound = "Sounds\woohoo.wav"

asylumKey = 0x410B #0x0113 #0x410B
green = 1372
yellow = 1174

relic = 0x2AA4

#relic = 0x0F84
eventFrag = 0x35DA
portalFrag = 0x0F21
blazeHue = 1161
powerScroll = 0x14F0
skillScroll = 0x2260
head = 0x1CE1
journalEntryDelay = 200
smallPause = 20
dragTime = 600
trapColors = [ 0x0489 , 0x0026 ]
containers = [ 0xe76 , 0xe75 , 0xe74 , 0xe78 , 0xe7d , 0xe77 ]
bags = [ 0xe76, 0xe75 , 0xe74 , 0xe78 , 0xe77 , 0x0E79 ]
# 0x0E7D trap box
# 0x0E79 pouch 
# 0x0E75 backpack
# 0x0E76 bag


def stealSkill(target):
    Player.UseSkill('Stealing')
    Misc.Pause(journalEntryDelay)
    if Journal.SearchByType('You must wait a few moments to use another skill.', 'Regular'):
        Player.HeadMessage( 44 , 'Skill Timer' )
        #Target.SetLast(target)
    else:
        Target.WaitForTarget(1500)
        Target.TargetExecute(target)
        #Target.SetLast(target)
    
    stealCheck()
        
def stealCheck():
    Misc.Pause(journalEntryDelay)
    if Journal.SearchByType( 'You fail to steal the item.' , 'Regular' ):
        Player.HeadMessage(33, 'FAILED')
        #stop()
    elif Journal.SearchByType( 'You successfully steal the item.' , 'Regular' ):
        Player.HeadMessage(66, 'GOT IT GTFO!')
        Player.ChatSay(52, "[organizeme")
        winsound.PlaySound(sound, winsound.SND_FILENAME)
        #escape()
        #stop()
        
def escape():
    runebook = Items.FindByID( 0x22C5 , -1 , Player.Backpack.Serial )
    Spells.CastMagery('Recall')
    Target.WaitForTarget(1500)
    Target.TargetExecute( runebook )
    
def stop():
    Stop
def steal_asylum(bag):
    if asylumKey in bag.Contains:
        stealSkill(item)
        stealCheck()
    else:
        for s in bag.Contains:
            if s.ItemID in bags and s.Hue not in trapColors:
                Misc.Pause(50)
                Items.UseItem(s)
                steal_asylum(s)

def stealBigItem(bag):
    # level 1 big items
    for s in bag.Contains:
        if s.ItemID == asylumKey and (s.Hue == green or s.Hue == yellow):
            Player.HeadMessage(66, 'Asylum Key')
            stealSkill(s)
            stealCheck()
        elif s.ItemID == relic:
            Player.HeadMessage(66, 'RELIC')
            stealSkill(s)
            stealCheck()
        elif s.ItemID == eventFrag:
            Player.HeadMessage(66, 'Event Frag!')
            stealSkill(s)
            stealCheck()
    
    # check other bags lvl 2
    for s in bag.Contains:
        for s in bag.Contains:
            if s.ItemID in bags and s.Hue not in trapColors:
                Misc.Pause(50)
                Items.UseItem(s)
                stealBigItem2(s)
                
def stealBigItem2(bag):
    # level 1 big items
    for s in bag.Contains:
        if s.ItemID == asylumKey and (s.Hue == green or s.Hue == yellow):
            Player.HeadMessage(66, 'Asylum Key')
            stealSkill(s)
            stealCheck()
        elif s.ItemID == relic:
            Player.HeadMessage(66, 'RELIC')
            stealSkill(s)
            stealCheck()
        elif s.ItemID == eventFrag:
            Player.HeadMessage(66, 'Event Frag!')
            stealSkill(s)
            stealCheck()
    
    # check other bags lvl 2
    for s in bag.Contains:
        for s in bag.Contains:
            if s.ItemID in bags and s.Hue not in trapColors:
                Misc.Pause(50)
                Items.UseItem(s)
                stealBigItem3(s)

def stealBigItem3(bag):
    # level 1 big items
    for s in bag.Contains:
        if s.ItemID == asylumKey and (s.Hue == green or s.Hue == yellow):
            Player.HeadMessage(66, 'Asylum Key')
            stealSkill(s)
            stealCheck()
        if s.ItemID == relic:
            Player.HeadMessage(66, 'RELIC')
            stealSkill(s)
            stealCheck()
        elif s.ItemID == eventFrag:
            Player.HeadMessage(66, 'Event Frag!')
            stealSkill(s)
            stealCheck()
    
        

def secondLayer(bag):
    Misc.Pause(dragTime)
    for s in bag.Contains:
        if s.ItemID in bags and s.Hue not in trapColors:
            Items.UseItem(s)
            stealBigItem(s)
        else:
            Misc.NoOperation()
            
def thirdLayer(bag):
    Misc.Pause(dragTime)
    for a in bag.Contains:
        if a.ItemID in bags:
            for b in a.Contains:
                if b.ItemID in bags:
                    Items.UseItem(b)
                    stealBigItem(b)
                    
def fourthLayer(bag):
    Misc.Pause(dragTime)
    for a in bag.Contains:
        if a.ItemID in bags:
            for b in a.Contains:
                if b.ItemID in bags:
                    for c in b.Contains:
                        if c.ItemID in bags:
                            Items.UseItem(c)
                            stealBigItem(c)
                            
def fifthLayer(bag):
    Misc.Pause(dragTime)
    for a in bag.Contains:
        if a.ItemID in bags:
            for b in a.Contains:
                if b.ItemID in bags:
                    for c in b.Contains:
                        if c.ItemID in bags:
                            for d in c.Contains:
                                if d.ItemID in bags:
                                    Items.UseItem(d)
                                    stealBigItem(d)


Journal.Clear()

while not Player.IsGhost:
    Misc.SendMessage('starting stelabig')
    stealTarget = Target.GetTargetFromList("stealtarget")
    if stealTarget:
        stealTargetBackpack = stealTarget.Backpack
        Items.UseItem(stealTargetBackpack)
        Misc.Pause(50)
        steal_asylum(stealTargetBackpack)