spell_cost = [53, 73, 113, 173, 229] # Magic Missile, Drain, Shield, Poison, Recharge

def play_round(php, pm, bhp, bdmg, timers):
    for timer in timers:
        if timers[timer] == 0:
            if timer == "shield":
                bdmg += 7
        elif timers[timer] > 0:
            if timer == "poison":
                bhp -= 3
            elif timer == "recharge":
                pm += 101
        timers[timer] -= 1

    #player choose a spell



if __name__ == "__main__":
    player_hp = 50
    player_mana = 500
    boss_hp = 71
    bass_damage = 10

    play_round(50, 500, 71, 10, {})



