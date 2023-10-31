
def load_data(file):
    data = open(file, 'r')
    output = []

    for line in data:
        output.append(line.strip().split(" "))
    return output


def main(registers, commands):
    index = 0
    while index < len(commands):
        parsed = commands[index]
        if parsed[0] == 'cpy':
            target = parsed[2]
            value = ""
            if parsed[1] in ['a', 'b', 'c', 'd']:
                value = registers[parsed[1]]
            else:
                value = int(parsed[1])
            registers[target] = value
            index += 1
        elif parsed[0] == 'inc':
            registers[parsed[1]] += 1
            index += 1
        elif parsed[0] == 'dec':
            registers[parsed[1]] -= 1
            index += 1
        else:
            if parsed[1] in ['a', 'b', 'c', 'd']:
                if registers[parsed[1]] == 0:
                    index += 1
                else:
                    index += int(parsed[2])
            else:
                if int(parsed[1]) != 0:
                    index += int(parsed[2])
                else:
                    index += 1
    return registers


if __name__ == "__main__":
    data = load_data('data_12')
    print(f"{main({'a': 0, 'b': 0, 'c': 0, 'd': 0}, data)}")
    print(f"{main({'a': 0, 'b': 0, 'c': 1, 'd': 0}, data)}")
