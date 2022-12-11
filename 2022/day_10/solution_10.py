def load_data(file):
    output = []
    data = open(file, 'r')
    for x, line in enumerate(data):
        output.append(line.strip())

    data.close()
    return output


def run_cycle(commands, max_cycle):
    x_value = 1
    pixel = [0, 1, 2]
    x_snapshot = []
    op_delay = 0
    op_add = []
    next_command = 0
    command_count = len(commands)
    crt_col = 0
    offset = 0
    grid = []
    temp_ray = ""
    for cycle in range(1, max_cycle+2):
        if next_command >= command_count:
            # end of commands
            break

        if op_delay == 0:
            if commands[next_command] != "noop":
                parsed_command = commands[next_command].split(" ")
                op_add.append(int(parsed_command[1]))
                op_delay = 2
            next_command += 1

        # pixel logic
        if (cycle -1) - offset in pixel:
            temp_ray += "#"
        else:
            temp_ray += "."

        if crt_col == 39:
            grid.append(temp_ray)
            temp_ray = ""
            crt_col = 0
            offset += 40
        else:
            crt_col += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            x_snapshot.append(x_value * cycle)

        if op_delay > 0:
            op_delay -= 1

        if op_delay == 0:
            if len(op_add) > 0:
                x_value += op_add.pop()
                pixel = [x_value - 1, x_value, x_value + 1]

    return [x_value, x_snapshot, grid]


def print_crt(v):
    for i in v:
        print(i)


if __name__ == "__main__":
    instructions = load_data("data_10")
    result = run_cycle(instructions, 10000)
    print(f"Register = {result[0]} signal value = {sum(result[1])}")
    print_crt(result[2])
