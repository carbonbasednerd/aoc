keypad_2 = [["0", "0", "1", "0", "0"],
            ["0", "2", "3", "4", "0"],
            ["5", "6", "7", "8", "9"],
            ["0", "A", "B", "C", "0"],
            ["0", "0", "D", "0", "0"]]

keypad_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

def load_data(file):
    output = []
    data = open(file, 'r')
    for line in data:
        output.append(line.strip())

    data.close()
    return output


def get_digit(x_value, y_value, offset, kpad):
    x_adjusted = x_value + offset
    y_adjusted = abs(y_value - offset)
    return kpad[y_adjusted][x_adjusted]


def can_move(x_value, y_value, move, offset, kpad, max):
    x_adjusted = x_value + offset
    y_adjusted = abs(y_value - offset)
    result = [x_value, y_value]
    if move == "U":
        if y_adjusted - 1 >= 0 and kpad[y_adjusted-1][x_adjusted] != "0":
            result = [x_value, y_value + 1]
    elif move == "D":
        if y_adjusted + 1 < max and kpad[y_adjusted+1][x_adjusted] != "0":
            result = [x_value, y_value - 1]
    elif move == "L":
        if x_adjusted - 1 >= 0 and kpad[y_adjusted][x_adjusted - 1] != "0":
            result = [x_value - 1, y_value]
    elif move == "R":
        if x_adjusted + 1 < max and kpad[y_adjusted][x_adjusted + 1] != "0":
            result = [x_value + 1, y_value]

    return result


if __name__ == "__main__":
    instructions = load_data("data_2")
    x = 0
    y = 0

    password = ""
    for i in instructions:
        for command in i:
            x, y = can_move(x, y, command, 1, keypad_1, 3)
        password = f"{password}{get_digit(x, y, 1, keypad_1)}"

    print(f"part one bathroom passcode is:{password}")

    x = -2
    y = 0
    password = ""
    for i in instructions:
        for command in i:
            x, y = can_move(x, y, command, 2, keypad_2, 5)
        password = f"{password}{get_digit(x, y, 2, keypad_2)}"

    print(f"part two bathroom passcode is:{password}")

