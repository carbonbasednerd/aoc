import copy
import math


def load_data(file):
    output = ""
    data = open(file, 'r')
    for line in data:
        output = line.strip()

    data.close()
    return output


def increment_move_count(current, max_count):
    current += 1
    if current == max_count:
        return 0
    return current


def increment_current_block(current):
    current += 1
    if current == 5:
        return 0
    return current


if __name__ == "__main__":
    moves = load_data("data_17")
    total_moves = len(moves)

    tower_space = []
    block_one = [0b11110]
    block_one_min = [0b1111]
    block_one_max = [0b1111000]

    block_two = [0b1000, 0b11100, 0b1000]
    block_two_min = [0b10, 0b111, 0b10]
    block_two_max = [0b100000, 0b1110000, 0b100000]

    block_three = [0b11100, 0b100, 0b100]
    block_three_min = [0b111, 0b1, 0b1]
    block_three_max = [0b1110000, 0b10000, 0b10000]

    block_four = [0b10000, 0b10000, 0b10000, 0b10000]
    block_four_min = [0b1, 0b1, 0b1, 0b1]
    block_four_max = [0b1000000, 0b1000000, 0b1000000, 0b1000000]

    block_five = [0b11000, 0b11000]
    block_five_min = [0b11, 0b11]
    block_five_max = [0b1100000, 0b1100000]

    blocks = [block_one, block_two, block_three, block_four, block_five]
    mins = [block_one_min, block_two_min, block_three_min, block_four_min, block_five_min]
    maxs = [block_one_max, block_two_max, block_three_max, block_four_max, block_five_max]

    rock_count = 0
    height = 0
    falling = True
    current_block_count = 0
    move_count = 0
    current_block = copy.deepcopy(blocks[current_block_count])

    # prep first block
    for x in range(0, 4):
        if moves[move_count] == ">":
            if current_block[0] != mins[current_block_count][0]:
                for idx, i in enumerate(current_block):
                    current_block[idx] = i >> 1
        else:
            if current_block[0] != maxs[current_block_count][0]:
                for idx, i in enumerate(current_block):
                    current_block[idx] = i << 1
        move_count = increment_move_count(move_count, total_moves)
    tower_space.append(current_block[0])

    rock_count += 1
    current_block_count = increment_current_block(current_block_count)
    current_block = copy.deepcopy(blocks[current_block_count])

    # loop through the rest of the puzzle
    prior_length = len(tower_space)
    height = 0
    pattern = ""
    pattern_buffer = ""
    start_match = False
    to_match = ""
    target_height = 1000000000000
    target_rock_min = 10000
    pattern_size = 20
    # target_height = 2022
    # target_rock_min = 100
    # pattern_size = 10

    while rock_count < target_height:
        # first get the 4 moves before possible contact
        for x in range(0, 4):
            if moves[move_count] == ">":
                if current_block[0] != mins[current_block_count][0]:
                    for idx, i in enumerate(current_block):
                        current_block[idx] = i >> 1
            else:
                if current_block[0] != maxs[current_block_count][0]:
                    for idx, i in enumerate(current_block):
                        current_block[idx] = i << 1
            move_count = increment_move_count(move_count, total_moves)

        processing_collisions = True
        depth = 1
        tower_length = len(tower_space)
        current_block_length = len(current_block)
        while processing_collisions:
            # check drop
            tower_slice = tower_space[tower_length-depth:tower_length]

            for idts, ts in enumerate(tower_slice):
                if idts < current_block_length:
                    if ts & current_block[idts]:
                        # collision
                        processing_collisions = False
                        depth = depth - 1
                        break

            if processing_collisions:
                # get next jet
                last_move = copy.deepcopy(current_block)
                if moves[move_count] == ">":
                    if current_block[0] != mins[current_block_count][0]:
                        for idx, i in enumerate(current_block):
                            current_block[idx] = i >> 1
                else:
                    if current_block[0] != maxs[current_block_count][0]:
                        for idx, i in enumerate(current_block):
                            current_block[idx] = i << 1

                move_count = increment_move_count(move_count, total_moves)

                # check for side collision
                side_collision = False
                for idts, ts in enumerate(tower_slice):
                    if idts < current_block_length:
                        if ts & current_block[idts]:
                            # collision
                            side_collision = True
                            break

                if side_collision:
                    current_block = copy.deepcopy(last_move)

                depth += 1
            else:
                break

        # resolve collision
        for idx, x in enumerate(current_block):
            if depth - idx > 0:
                offset = depth - idx
                tower_space[tower_length - offset] = int(bin(x + tower_space[tower_length - offset]), 2)
            else:
                tower_space.append(x)

        # logic to try to find a pattern in the difference of height
        if rock_count > target_rock_min:
            pattern_buffer += str(len(tower_space) - prior_length)
            if not start_match:
                if len(pattern_buffer) >= pattern_size:
                    start_match = True
                    to_match = pattern_buffer[0:pattern_size]
            else:
                if to_match in pattern_buffer[pattern_size:]:
                    pattern = pattern_buffer[pattern_size:]
                    break

        rock_count += 1
        current_block_count = increment_current_block(current_block_count)
        current_block = copy.deepcopy(blocks[current_block_count])

        prior_length = len(tower_space)
        height = len(tower_space)

    pattern_array = []
    for i in pattern:
        pattern_array.append(int(i))
    height += (math.floor((target_height - rock_count) / len(pattern_array)) * sum(pattern_array))
    height += sum(pattern_array[0: (target_height - rock_count) % len(pattern_array)])

    print(f"puzzle answer {height}")
