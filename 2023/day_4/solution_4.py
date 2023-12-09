def load_data(file):
    data = open(file, 'r')
    solution_1 = 0
    count = 1
    multiplier = {}
    total_cards = 0
    for line in data:
        multiplier_value = 0
        if count in multiplier.keys():
            multiplier_value = multiplier[count]

        stripped_line = line.strip()
        split_card_id = stripped_line.split(":")
        numbers = split_card_id[1].split("|")
        winning_numbers = list(map(lambda x: int(x), filter(lambda x: x != '', numbers[0].strip().split(" "))))
        played_numbers = list(map(lambda x: int(x), filter(lambda x: x != '', numbers[1].strip().split(" "))))

        score = 0
        match_count = 0
        for number in played_numbers:
            if number in winning_numbers:
                match_count += 1
                if score == 0:
                    score = 1
                else:
                    score *= 2

        if match_count > 0:
            for x in range(1, match_count + 1):
                temp = count + x
                if temp in multiplier.keys():
                    multiplier[temp] += (1 + multiplier_value)
                else:
                    multiplier[temp] = 1 + multiplier_value

        solution_1 += score
        count += 1
        total_cards += (1 + multiplier_value)
    return solution_1, total_cards


if __name__ == "__main__":
    sol_1, sol_2 = load_data('data')
    print(f"Solution 1 = {sol_1} \n Solution 2 = {sol_2}")
