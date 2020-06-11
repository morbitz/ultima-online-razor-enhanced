def recall(target):
    Spells.CastMagery('Recall')
    Target.WaitForTarget( 2000, False )
    Target.TargetExecute(target)

def turn(direction):
    if Player.Direction == direction:
        return True
    else:
        Player.Walk(direction)
        return True
