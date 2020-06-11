from datetime import datetime
#import random

PLAYERS = {
    'human xerox copy': {
        'runebook_vendor_target': 0x401DD01F,
        'runebook_home_target': 0x401D2727,
        'pull_timer': 18000000
    },
    'dankmemes': {
        'runebook_vendor_target': 0x401DD7C7,
        'runebook_home_target': 0x401DE5B2,
        'pull_timer': 21600000
    },
    'wattttgg': {
        'runebook_vendor_target': 0x401DEF7D,
        'runebook_home_target': 0x401DCCBA,
        'pull_timer': 21600000
    },
    'white grl wasted': {
        'runebook_vendor_target': 0x41A45C3A,
        'runebook_home_target': 0x427FF1A3,
        'pull_timer': 21600000
    },
}
    
BOD_LOG = 'C:\\Users\\athl33t\\Documents\\uo\\bodpulls.log'

def recall(target):
    Spells.CastMagery('Recall')
    Misc.Pause(1800)
    Target.TargetExecute(target)
    Misc.Pause(900)

def goto_vendor(runebook_vendor_target):
    Journal.Clear()    
    recall(runebook_vendor_target)
    Misc.Pause(3000)
    Player.UseSkill('Hiding')
    Misc.Pause(600)

def goto_home(runebook_home_target):
    recall(runebook_home_target)
    Misc.Pause(1100)
    Player.Run('North')
    Misc.Pause(600)
    Player.Run('North')
    Player.UseSkill('Hiding')

def is_order_available():
    Journal.Clear()
    Misc.WaitForContext(0x00029397, 10000)
    Misc.Pause(600)
    Misc.ContextReply(0x00029397, 1)
    Misc.Pause(1600)
    if Journal.Search('can get an order'):
        return True
    else:
        return False

def is_order_received():
    Gumps.SendAction(2611865322, 1)
    Gumps.SendAction(3188567326, 1)
    if Journal.Search('your backpack'):
        fp = open(BOD_LOG, 'a')
        log_msg =  str(datetime.now()) + ': ' + Player.Name + '\n'
        fp.write(log_msg)
        fp.close()
        return True
    else:
        return False

def pull_bod(runebooks):
    goto_vendor(runebooks['runebook_vendor_target'])
    if not is_order_available():
        goto_home(runebooks['runebook_home_target'])
        return True

    while not is_order_received():
        Misc.WaitForContext(0x00029397, 10000)
        Misc.Pause(600)
        Misc.ContextReply(0x00029397, 3)
        Misc.Pause(600)

    goto_home(runebooks['runebook_home_target'])


def get_pull_delay():
    max_tstamp = lambda a, b: a if a and a > b else b
    str_to_tstamp = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
    elapsed = lambda l: (datetime.now() - l).total_seconds() * 1000 if l else PLAYERS[Player.Name]['pull_timer']
    pull_delay_ms = lambda l: PLAYERS[Player.Name]['pull_timer'] - elapsed(l) if PLAYERS[Player.Name]['pull_timer'] - elapsed(l) > 0 else 0
    last_pull = None

    with open(BOD_LOG, 'r') as lfp:
        pulls = lfp.readlines()
    
    for pull in pulls:
        if Player.Name in pull:
            last_pull = max_tstamp(last_pull, str_to_tstamp(pull[:26]))

    return pull_delay_ms(last_pull)


make_rand = lambda n: n
#make_rand = lambda n: n + random.randint(720000, 960000)
pull_delay_ms = get_pull_delay()
Misc.SendMessage(str(pull_delay_ms))
if pull_delay_ms > 0:
    pull_delay_ms = make_rand(pull_delay_ms)
Misc.SendMessage('Starting bodpull in: {} minutes'.format(pull_delay_ms/1000.0/60.0))
Misc.Pause(pull_delay_ms)
pull_bod(PLAYERS[Player.Name])
