from functools import reduce
spell_cost = [53, 73, 113, 173, 229]  # Magic Missile, Drain, Shield, Poison, Recharge
effect_times = [6, 6, 5]  # shield, Poison, Recharge

class Stats:
    shield_timer = 0
    poison_timer = 0
    recharge_timer = 0
    spent_mana = 0

    def __init__(self, player_hit_points, player_mana, boss_hit_points, boss_damage):
        self.player_hit_points = player_hit_points
        self.player_mana = player_mana
        self.boss_hit_points = boss_hit_points
        self.boss_damage = boss_damage
        self.boss_base_damage = boss_damage

    def update_mana(self, value):
        self.spent_mana += value
        self.player_mana -= value

    def copy_stats(self):
        new_stats = Stats(self.player_hit_points, self.player_mana, self.boss_hit_points, self.boss_damage)
        new_stats.shield_timer = self.shield_timer
        new_stats.poison_timer = self.poison_timer
        new_stats.recharge_timer = self.recharge_timer
        new_stats.spent_mana = self.spent_mana
        new_stats.boss_base_damage = self.boss_base_damage
        return new_stats


def process_effects(game_stats):
    if game_stats.poison_timer > 0:
        game_stats.boss_hit_points -= 3
        game_stats.poison_timer -= 1

    if game_stats.shield_timer > 0:
        game_stats.shield_timer -= 1
        game_stats.boss_damage = game_stats.boss_base_damage - 7
    else:
        game_stats.boss_damage = game_stats.boss_base_damage

    if game_stats.recharge_timer > 0:
        game_stats.player_mana += 101
        game_stats.recharge_timer -= 1


def play_round(game_stats):
    boss_dies = set()

    # part 2 solution (player loses 1 hit point on each of their turns)
    game_stats.player_hit_points -= 1
    if game_stats.player_hit_points <= 0:
        return boss_dies

    process_effects(game_stats)
    if game_stats.boss_hit_points <= 0:
        boss_dies.add(game_stats.spent_mana)
        return boss_dies

    # decide which spells to cast
    # Magic Missile?
    if game_stats.player_mana >= spell_cost[0]:
        new_game_stats = game_stats.copy_stats()
        new_game_stats.update_mana(spell_cost[0])
        new_game_stats.boss_hit_points -= 4

        process_effects(new_game_stats)

        if new_game_stats.boss_hit_points <= 0:
            boss_dies.add(new_game_stats.spent_mana)
        else:
            new_game_stats.player_hit_points -= new_game_stats.boss_damage
            if new_game_stats.player_hit_points > 0:
                boss_dies.update(play_round(new_game_stats))

    # Drain
    if game_stats.player_mana >= spell_cost[1]:
        new_game_stats = game_stats.copy_stats()
        new_game_stats.update_mana(spell_cost[1])
        new_game_stats.boss_hit_points -= 2
        new_game_stats.player_hit_points += 2

        process_effects(new_game_stats)

        if new_game_stats.boss_hit_points <= 0:
            boss_dies.add(new_game_stats.spent_mana)
        else:
            new_game_stats.player_hit_points -= new_game_stats.boss_damage
            if new_game_stats.player_hit_points > 0:
                boss_dies.update(play_round(new_game_stats))

    # Shield
    if game_stats.shield_timer == 0 and game_stats.player_mana >= spell_cost[2]:
        new_game_stats = game_stats.copy_stats()
        new_game_stats.update_mana(spell_cost[2])
        new_game_stats.shield_timer = effect_times[0]
        new_game_stats.boss_damage = new_game_stats.boss_base_damage - 7

        process_effects(new_game_stats)

        if new_game_stats.boss_hit_points > 0:
            new_game_stats.player_hit_points -= new_game_stats.boss_damage
            if new_game_stats.player_hit_points > 0:
                boss_dies.update(play_round(new_game_stats))
        else:
            boss_dies.add(new_game_stats.spent_mana)

    # Poison
    if game_stats.poison_timer == 0 and game_stats.player_mana >= spell_cost[3]:
        new_game_stats = game_stats.copy_stats()
        new_game_stats.update_mana(spell_cost[3])
        new_game_stats.poison_timer = effect_times[1]

        process_effects(new_game_stats)

        if new_game_stats.boss_hit_points > 0:
            new_game_stats.player_hit_points -= new_game_stats.boss_damage
            if new_game_stats.player_hit_points > 0:
                boss_dies.update(play_round(new_game_stats))
        else:
            boss_dies.add(new_game_stats.spent_mana)

    # Recharge
    if game_stats.recharge_timer == 0 and game_stats.player_mana >= spell_cost[4]:
        new_game_stats = game_stats.copy_stats()
        new_game_stats.update_mana(spell_cost[4])
        new_game_stats.recharge_timer = effect_times[2]

        process_effects(new_game_stats)

        if new_game_stats.boss_hit_points > 0:
            new_game_stats.player_hit_points -= new_game_stats.boss_damage
            if new_game_stats.player_hit_points > 0:
                boss_dies.update(play_round(new_game_stats))
        else:
            boss_dies.add(new_game_stats.spent_mana)

    return boss_dies


if __name__ == "__main__":
    stats = Stats(50, 500, 71, 10)
    # stats = Stats(10, 250, 14, 8)  #for testing
    spent_mana = play_round(stats)
    s_sorted = sorted(spent_mana)

    print(f"lowest mana spent {s_sorted}")




