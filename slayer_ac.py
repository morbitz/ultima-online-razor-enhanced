CRYSTAL_WORKBENCH = 0x40624E9B
RUNE = {
    'a': {'gump_id': 18491, 'item_id': 0x483B},
    'b': {'gump_id': 18494, 'item_id': 0x483E},
    'ch': {'gump_id': 18497, 'item_id': 0x4841},
    'e': {'gump_id': 18503, 'item_id': 0x4847},
    'f': {'gump_id': 18506, 'item_id': 0x484A},
    'g': {'gump_id': 18509, 'item_id': 0x484D},
    'h': {'gump_id': 18512, 'item_id': 0x4850},
    'i': {'gump_id': 18515, 'item_id': 0x4853},
    'gl': {'gump_id': 18521, 'item_id': 0x4859},
    'k': {'gump_id': 18524, 'item_id': 0x485C},
    'l': {'gump_id': 18527, 'item_id': 0x485F},
    'm': {'gump_id': 18530, 'item_id': 0x4862},
    'n': {'gump_id': 18536, 'item_id': 0x4868},
    'p': {'gump_id': 18539, 'item_id': 0x486B},
    'r': {'gump_id': 18542, 'item_id': 0x486E},
    'sh': {'gump_id': 18545, 'item_id': 0x4871},
    't': {'gump_id': 18551, 'item_id': 0x4877},
    'u': {'gump_id': 18554, 'item_id': 0x487A}
}
SUPER_SLAYER_WORD = {
    'silver': ['n', 'e', 'ch', 'r', 'a'],
    'fey': ['m', 'a', 'r'],
    'exorcism': ['b', 'a', 'k', 'r'],
    'elemental': ['g', 'a', 'sh'],
    'repond': ['k', 'l', 'i', 'gl', 'e'],
    'reptilian': ['p', 'u', 'n', 't'],
    'arachnid': ['f', 'i', 'h', 'l', 'a']
}

Journal.Clear()
Misc.SendMessage('Starting Slayer AC Maker')

if Misc.ReadSharedValue('reliquary') != 0:
    reliquary = Misc.ReadSharedValue('reliquary')
else:
    Player.HeadMessage(66, 'Target Reliquary')
    reliquary = Target.PromptTarget()
    Misc.SetSharedValue('reliquary', reliquary)
    
Items.UseItem(CRYSTAL_WORKBENCH)
Misc.Pause(600)

Misc.SendMessage('Pick Slayer Type:')
Misc.SendMessage('  - silver')
Misc.SendMessage('  - fey')
Misc.SendMessage('  - exorcism')
Misc.SendMessage('  - elemental')
Misc.SendMessage('  - repond')
Misc.SendMessage('  - reptilian')
Misc.SendMessage('  - arachnid')

Player.HeadMessage(69, 'CHOOSE YOUR SET TYPE')

Journal.Clear()
Misc.Pause(4000)

Items.UseItem(reliquary)
Misc.Pause(1000)

def get_letters(slayer_type):
    for letter in SUPER_SLAYER_WORD[slayer_type]:
        Gumps.SendAction(1616378132, RUNE[letter]['gump_id'])
        Misc.Pause(900)

def move_runes_to_workbench(power_word_list):
    x = 0
    for letter in power_word_list:
        rune = Items.FindByID(RUNE[letter]['item_id'], -1, -1)
        Items.Move(rune, CRYSTAL_WORKBENCH, 1, x, 0)
        x += 30
        Misc.Pause(900)
        
def fill_workbench(slayer_type):
    get_letters(slayer_type)
    Misc.Pause(1200)
    move_runes_to_workbench(SUPER_SLAYER_WORD[slayer_type])

if Journal.Search('silver'):
    fill_workbench('silver')
elif Journal.Search('fey'):
    fill_workbench('fey')
elif Journal.Search('exorcism'):
    fill_workbench('exorcism')
elif Journal.Search('elemental'):
    fill_workbench('elemental')
elif Journal.Search('repond'):
    fill_workbench('repond')
elif Journal.Search('reptilian'):
    fill_workbench('reptilian')
elif Journal.Search('arachnid'):
    fill_workbench('arachnid')
else:
    Player.HeadMessage(69, 'NO VALID SLAYER TYPE SELECTED')