import math


if __name__ == "__main__":
    weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
    armor = [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
    rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

    player_hp = 100
    boss_hp = 100
    boss_damage = 8
    boss_armor = 2

    part_one_cost = 10000
    part_two_cost = 0
    for weapon in weapons:
        for ar in armor:
            for ring1 in rings:
                for ring2 in rings:
                    player_dpr = weapon[1] + ar[1] + ring1[1] + ring2[1] - boss_armor
                    if player_dpr < 1:
                        player_dpr = 1
                    boss_dpr = boss_damage - ar[2] - ring1[2] - ring2[2]
                    if boss_dpr < 1:
                        boss_dpr = 1

                    boss_dead_in_rounds = math.floor(boss_hp / player_dpr)
                    player_dead_in_rounds = math.floor(player_hp / boss_dpr)

                    print(f"player_dpr = {player_dpr} boss dpr = {boss_dpr} boss dead {boss_dead_in_rounds} player dead {player_dead_in_rounds}")
                    # part 1
                    if player_dead_in_rounds >= boss_dead_in_rounds:
                        part_one_cost = min(part_one_cost, weapon[0] + ar[0] + ring1[0] + ring2[0])

                    # part 2
                    if player_dead_in_rounds < boss_dead_in_rounds:
                        part_two_cost = max(part_two_cost, weapon[0] + ar[0] + ring1[0] + ring2[0])

    print(f"Smallest amount of gold to pay to win the fight : {part_one_cost}")

    print(f"Largest amount of gold to pay and loose the fight : {part_two_cost}")