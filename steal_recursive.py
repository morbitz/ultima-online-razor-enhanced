# Recursive, fast steal script by ATHL33T

escapeRunebook = 0x414D8007

import winsound
sound = "Sounds\woohoo.wav"

asylum_key = 0x410B
green = 1372
yellow = 1174
short_delay = 20
journal_delay = 120
snoop_delay = 570


trap_hues = [0x0489, 0x0026]
containers = [0xe76, 0xe75, 0xe74, 0xe78, 0xe7d, 0xe77]
bags = [0x0E76, 0xE75, 0xE74, 0xE78, 0xE77, 0x0E79]

relic = 0x2AA4
eventFrag = 0x35DA
portalFrag = 0x0F21
blazeHue = 1161
powerScroll = 0x14F0
skillScroll = 0x2260
head = 0x1CE1
garlic = 0x0F84
root = 0x0F86
bandages = 0x0E21
cure_pots = 0x0F07
arrows = 0x0F3F
bags = []

#steal_priorities = [asylum_key, eventFrag, skillScroll]
#steal_priorities = [garlic, root, bandages, cure_pots]
steal_priorities = [asylum_key]
#steal_priorities = [relic, powerScroll, eventFrag]

# 0x0E7D trap box
# 0x0E79 pouch 
# 0x0E75 backpack
# 0x0E76 bag

        
def is_steal_success():
    Misc.Pause(journal_delay)
    if Journal.Search('You fail to steal the item.'):
        Player.HeadMessage(33, 'FAILED')
    elif Journal.Search('You successfully steal the item.'):
        Player.HeadMessage(66, '└[∵┌]└[ ∵ ]┘[┐∵]┘')
        Player.HeadMessage(66, 'GOT EM')
        Player.ChatSay(52, "[organizeme")
        winsound.PlaySound(sound, winsound.SND_FILENAME)
    else:
        Player.HeadMessage(66, 'third thing')
        
def escape():
    runebook = Items.FindByID( 0x22C5 , -1 , Player.Backpack.Serial )
    Spells.CastMagery('Recall')
    Target.WaitForTarget(1500)
    Target.TargetExecute( runebook )
    
def stop():
    Stop

def steal(item, mark):
    Journal.Clear()
    attempted = False
    
    while not attempted:
        Player.UseSkill('Stealing')
        Misc.Pause(journal_delay)
        if Journal.SearchByType('You must wait a few moments to use another skill.', 'Regular'):
            Player.HeadMessage(66 , 'Skill Timer')
            Misc.Pause(journal_delay)
        else:
            Target.WaitForTarget(1500)
            while Player.DistanceTo > 1:
                Misc.Pause(short_delay)
            Target.TargetExecute(item)
            attempted = True

    is_steal_success()

def snoop_recursive(container, mark):
    Items.UseItem(container)
    contents = container.Contains

    steal_target_bags = [item for item in contents if item.IsContainer and item.Hue not in trap_hues]
    items_to_steal = [item.Serial for item in contents if item.ItemID in steal_priorities]
    
    if len(items_to_steal) > 0:
        return steal(items_to_steal[0], mark)
    
    if len(steal_target_bags) == 0:
        return True
    else:
        for bag in steal_target_bags:
            Misc.Pause(snoop_delay)
            snoop_recursive(bag, mark)
    return True

def run_continuously():
    while Player.Hits > 0:
        mark = Target.GetTargetFromList("mark")
        if mark != None and Player.DistanceTo(mark) < 2:
            snoop_recursive(mark.Backpack, mark)
            Misc.Pause(short_delay)
        Misc.Pause(600)

def run_once():
    mark = Target.GetTargetFromList("mark")
    
    if mark != None and Player.DistanceTo(mark) < 2:
        snoop_recursive(mark.Backpack, mark)
        Misc.Pause(short_delay)
    Misc.Pause(600)

Player.HeadMessage(66, 'sticky fingers time')
run_continuously()