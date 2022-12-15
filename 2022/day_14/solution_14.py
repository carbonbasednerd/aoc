def load_data(file):
    segments = []
    data = open(file, 'r')
    min_col = 1000
    max_col = 0
    max_row = 0
    segment = []
    for line in data:
        points = line.strip().split(" -> ")
        for point in points:
            split = point.split(",")
            col = int(split[0])
            row = int(split[1])

            min_col = min(col, min_col)
            max_col = max(col, max_col)

            max_row = max(row, max_row)

            segment.append([col, row])

        segments.append(segment)
        segment = []

    data.close()
    return [segments, min_col, max_col, max_row]


def build_rock_paths(paths, off_set, space):
    for path in paths:
        seg_length = len(path)
        for i in range(0, seg_length - 1):
            if path[i] == path[i+1]:
                space[path[i][1]][path[i][0]-off_set] = 1
            else:
                if path[i][0] == path[i+1][0]:
                    # vertical path
                    if path[i][1] > path[i+1][1]:
                        for x in range(path[i+1][1], path[i][1]+1):
                            space[x][path[i][0]-off_set] = 1
                    else:
                        for x in range(path[i][1], path[i+1][1]+1):
                            space[x][path[i][0]-off_set] = 1
                else:
                    # horizontal path
                    if path[i][0] > path[i+1][0]:
                        for x in range(path[i+1][0], path[i][0]+1):
                            space[path[i][1]][x-off_set] = 1
                    else:
                        for x in range(path[i][0], path[i+1][0]+1):
                            space[path[i][1]][x-off_set] = 1
    return paths


def print_puzzle_space(space):
    for i in space:
        t = ""
        for j in i:
            if j == 0:
                t += "."
            elif j == 1:
                t += "#"
            else:
                t += "o"
        print(t)


def drip(space, off_set, s, r_max, c_max):
    flag = True
    count = 0
    while flag:
        count += 1
        dropping = True
        current_loc = [0, s]
        while dropping:
            # if the start is blocked - stop
            if current_loc == [0, s] and space[current_loc[0]][current_loc[1]]:
                dropping = False
                flag = False
                break

            # check next row directly below
            if current_loc[0] + 1 > r_max:  # Check for Abyss
                dropping = False
                flag = False
                break

            if space[current_loc[0] + 1][current_loc[1]]:
                # straight down is blocked Check, left
                if current_loc[1]-1 < 0:
                    # Hit the Abyss
                    dropping = False
                    flag = False
                    break
                else:
                    if space[current_loc[0]+1][current_loc[1]-1]:
                        if current_loc[1] + 1 > c_max:
                            # hit the abyss
                            dropping = False
                            flag = False
                            break
                        else:
                            if space[current_loc[0]+1][current_loc[1]+1]:
                                dropping = False
                            else:
                                current_loc = [current_loc[0] + 1, current_loc[1] + 1]
                    else:
                        current_loc = [current_loc[0]+1, current_loc[1]-1]
            else:
                # not blocked - update and move
                current_loc = [current_loc[0]+1, current_loc[1]]

        if flag:
            space[current_loc[0]][current_loc[1]] = 2

    return count


if __name__ == "__main__":
    results = load_data("data_14")
    col_min = 0
    rock_paths = results[0]
    offset = results[1]
    col_max = results[2] - results[1]
    row_max = results[3]

    # build default puzzle space
    puzzle_space = [[0 for i in range(col_max+1)] for j in range(results[3]+1)]
    puzzle_space_2 = [[0 for i in range(col_max+10000)] for j in range(results[3]+3)]

    # Part 1
    build_rock_paths(rock_paths, offset, puzzle_space)
    print_puzzle_space(puzzle_space)

    print(" ========== ")
    # Part 2
    build_rock_paths(rock_paths, offset-5000, puzzle_space_2)
    for z in range(0, len(puzzle_space_2[-1])):
        puzzle_space_2[-1][z] = 1
    print_puzzle_space(puzzle_space_2)

    # drip puzzle 1
    count = drip(puzzle_space, offset, 500 - offset, row_max, col_max)
    print_puzzle_space(puzzle_space)
    print(f"puzzle 1 count {count - 1}")

    # drip puzzle 2
    count = drip(puzzle_space_2, offset, 500 - (offset - 5000), row_max + 3, col_max + 10000)
    print_puzzle_space(puzzle_space_2)

    print(f"puzzle 2 count {count-1}")
