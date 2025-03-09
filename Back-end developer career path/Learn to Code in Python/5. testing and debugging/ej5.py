def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp - resist
    if total_damage < 0:
        total_damage = 0
    health -= total_damage
    if health < 0:
        health = 0
    return health
