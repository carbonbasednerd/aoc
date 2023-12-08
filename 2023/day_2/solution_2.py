def load_data(file):
    data = open(file, 'r')
    goal = {"red": 12, "green": 13, "blue": 14}
    solution_1 = 0
    solution_2 = 0
    for line in data:
        stripped_line = line.strip()
        game_split = stripped_line.split(":")
        id_split = game_split[0].split(" ")
        id = int(id_split[1])

        run_split = game_split[1].strip().split(";")
        no_match = False
        gem_count = {"red": 0, "green": 0, "blue": 0}
        for run in run_split:
            gems = run.strip().split(", ")

            for gem in gems:
                num_color = gem.split(" ")
                number = int(num_color[0])
                color = num_color[1]
                gem_count[color] = max(gem_count[color], number)
                if number > goal[color]:
                    no_match = True

        if not no_match:
            solution_1 += id

        solution_2 += gem_count["red"] * gem_count["green"] * gem_count["blue"]

    data.close()
    return solution_1, solution_2

if __name__ == "__main__":
    s1, s2 = load_data('data')
    print(f"solution 1: {s1} \n solution 2 {s2}")