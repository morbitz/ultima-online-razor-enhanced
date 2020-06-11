pouch = Target.PromptTarget('Target your pouch')
while Player.Mana > 10:
    Spells.CastMagery('Magic Trap')
    Misc.Pause(300)
    Target.TargetExecute(pouch)
    Misc.Pause(100)
