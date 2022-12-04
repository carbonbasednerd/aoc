
moves = [0, 1, 2]


def modify_input(value):
    if value == 'A' or value == 'X':
        return 0   # rock
    if value == 'B' or value == 'Y':
        return 1   # paper
    if value == 'C' or value == 'Z':
        return 2   # scissors


def score_input(value):
    if value == 0:
        return 1  # rock
    elif value == 1:
        return 2  # paper
    elif value == 2:
        return 3  # scissors


def score_turn(player_1, player_2):
    if player_2 == player_1:
        return 3  # draw
    elif player_2 == 0 and player_1 == 2:
        return 6
    elif player_2 == 1 and player_1 == 0:
        return 6
    elif player_2 == 2 and player_1 == 1:
        return 6
    return 0


def get_move(value, win):
    move = 0
    if win:
        move = value + 1
    else:
        move = value - 1

    if move < 0:
        return 2
    if move > 2:
        return 0

    return move


def choose_move(player_1, player_2):
    if player_2 == 0:
        return get_move(player_1, False)

    elif player_2 == 1:
        return player_1
    else:
        return get_move(player_1, True)


def load_data(file):
    data = open(file, 'r')
    score = 0
    score_part_2 = 0
    for line in data:
        input = list(map(lambda x: modify_input(x), line.strip().split(" ")))
        # choose win, lose or draw:
        part_2_choice = choose_move(input[0], input[1])

        # choice score
        score += score_input(input[1])
        score_part_2 += score_input(part_2_choice)

        # win, lose or draw
        score += score_turn(input[0], input[1])
        score_part_2 += score_turn(input[0], part_2_choice)

    data.close()
    return [score, score_part_2]


if __name__ == "__main__":
    scores = load_data('data_2')
    print(f"score is {scores[0]} and part 2 scores are {scores[1]}")
