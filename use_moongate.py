from Scripts.glossary.items.moongates import FindMoongates

moongates = FindMoongates( Items )
while len( moongates ) == 0:
    Misc.Pause( 20 )
    moongates = FindMoongates( Items )

Items.UseItem( moongates[ 0 ] )
Gumps.WaitForGump( 3716879466, 2000 )
Gumps.SendAction( 3716879466, 1 )
Player.HeadMessage(13,'Using Moongate')