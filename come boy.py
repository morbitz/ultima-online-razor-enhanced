from System.Collections.Generic import List 

# Filters
gate = Items.Filter()
gate.Enabled = True
gate.OnGround = True
gate.Movable = False
gate.RangeMax = 2


if Journal.Search("come boy"):
    mobileFilter = Mobiles.Filter()
    mobileFilter.RangeMax = 24
    pathfindToNearestMobile(mobileFilter)
    Journal.Clear()
    moongate = Items.ApplyFilter(gate)

    for m in moongate: # Look for items in filter
        if m.ItemID == 0x0F6C: # Return true if found a moongate = 0x0F6C
            Items.UseItem(m) # Double click on the moongate found 
            Gumps.WaitForGump(3716879466, 10000)
            Gumps.SendAction(3716879466, 1)
 