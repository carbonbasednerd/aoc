import copy
import unittest


def load_data(file):
    output = []
    data = open(file, 'r')
    for line in data:
        output.append(line.strip())

    data.close()
    return output


class TestBlock(unittest.TestCase):

    def test_shift_left(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4], [0, 1, 1, 1, 2])
        test_block.shift_left()
        self.assertTrue(test_block.block_grid == [[2, 3], [1, 4], [2, 4], [3, 4], [2, 5]])

    def test_shift_right(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4], [0, 1, 1, 1, 2])
        test_block.shift_right()
        self.assertTrue(test_block.block_grid == [[4, 3], [3, 4], [4, 4], [5, 4], [4, 5]])

    def test_shift_down(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4], [0, 1, 1, 1, 2])
        test_block.shift_down()
        self.assertTrue(test_block.block_grid == [[3, 2], [2, 3], [3, 3], [4, 3], [3, 4]])

    def test_check_linked_positions(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4], [0, 1, 1, 1, 2])
        self.assertTrue(test_block.get_top() == [3, 5])
        self.assertTrue(test_block.get_down() == [[3, 3], [2, 4], [4, 4]])
        self.assertTrue(test_block.get_left() == [[3, 3], [2, 4], [3, 5]])
        self.assertTrue(test_block.get_right() == [[3, 3], [4, 4], [3, 5]])

        test_block.shift_down()
        test_block.shift_right()

        self.assertTrue(test_block.get_top() == [4, 4])
        self.assertTrue(test_block.get_down() == [[4, 2], [3, 3], [5, 3]])
        self.assertTrue(test_block.get_left() == [[4, 2], [3, 3], [4, 4]])
        self.assertTrue(test_block.get_right() == [[4, 2], [5, 3], [4, 4]])

    def test_set_start_position(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4],
                           [0, 1, 1, 1, 2])
        test_block.set_starting_position(10)
        self.assertTrue(test_block.block_grid == [[3, 10], [2, 11], [3, 11], [4, 11], [3, 12]])

    def test_check_move_down(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4],
                           [0, 1, 1, 1, 2])

        space = [[False for i in range(0, 4)] for j in range(0, 7)]
        self.assertTrue(test_block.check_move_down(space))

        space[3][2] = True
        self.assertFalse(test_block.check_move_down(space))

        space[3][2] = False
        test_block.shift_down()
        self.assertTrue(test_block.check_move_down(space))
        test_block.shift_down()
        self.assertTrue(test_block.check_move_down(space))
        test_block.shift_down()
        self.assertFalse(test_block.check_move_down(space))

    def test_check_move_right(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4],
                           [0, 1, 1, 1, 2])

        space = [[False for i in range(0, 4)] for j in range(0, 7)]
        self.assertTrue(test_block.check_move_right(space))

        space[4][3] = True
        self.assertFalse(test_block.check_move_right(space))

        space[4][3] = False
        test_block.shift_right()
        self.assertTrue(test_block.check_move_right(space))
        test_block.shift_right()
        self.assertFalse(test_block.check_move_right(space))


    def test_check_move_left(self):
        test_block = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4],
                           [0, 1, 1, 1, 2])

        space = [[False for i in range(0, 4)] for j in range(0, 7)]
        self.assertTrue(test_block.check_move_left(space))

        space[2][3] = True
        self.assertFalse(test_block.check_move_left(space))

        space[2][3] = False
        test_block.shift_left()
        self.assertTrue(test_block.check_move_right(space))
        test_block.shift_left()
        self.assertFalse(test_block.check_move_left(space))


class Block:

    def __init__(self, block_grid, top, down, left, right, height_offsets):
        self.block_grid = block_grid
        self.top = top
        self.down = down
        self.left = left
        self.right = right
        self.height_offsets = height_offsets

    def set_starting_position(self, start_height):
        for i in range(0, len(self.block_grid)):
            self.block_grid[i][1] = start_height + self.height_offsets[i]

    def check_move_right(self, space):
        for i in self.get_right():
            if i[0] == 6:  # Dangerous hard coded value for puzzle space width
                return False
            elif i[1] < len(space[0]) and space[i[0]+1][i[1]]:
                return False
        return True

    def check_move_left(self, space):
        for i in self.get_left():
            if i[0] == 0:
                return False
            elif i[1] < len(space[0]) and space[i[0]-1][i[1]]:
                return False
        return True

    def check_move_down(self, space):
        for i in self.get_down():
            if i[1] == 0:
                return False
            elif i[1] < len(space[0]) and space[i[0]][i[1] - 1]:
                return False
        return True

    def shift_left(self):
        for i in self.block_grid:
            i[0] = i[0] - 1

    def shift_left_with_value(self, val):
        for i in self.block_grid:
            i[0] = i[0] - val

    def shift_right_with_val(self, val):
        for i in self.block_grid:
            i[0] = i[0] + val

    def shift_down(self):
        for i in self.block_grid:
            i[1] = i[1] - 1

    def shift_right(self):
        for i in self.block_grid:
            i[0] = i[0] + 1

    def get_top(self):
        return self.block_grid[self.top]

    def get_down(self):
        down_list = []
        for i in self.down:
            down_list.append(self.block_grid[i])
        return down_list

    def get_left(self):
        left_list = []
        for i in self.left:
            left_list.append(self.block_grid[i])
        return left_list

    def get_right(self):
        right_list = []
        for i in self.right:
            right_list.append(self.block_grid[i])
        return right_list


if __name__ == "__main__":
    # block_one = [[2, 3], [3, 3], [4, 3], [5, 3]]
    # block_two = [[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]]
    # block_three = [[2, 3], [3, 3], [4, 3], [4, 4], [4, 5]]
    # block_four = [[2, 3], [2, 4], [2, 5], [2, 6]]
    # block_five = [[2, 3], [3, 3], [2, 4], [3, 4]]

    block_one = Block([[2, 3], [3, 3], [4, 3], [5, 3]], 3, [0, 1, 2, 3], [0], [3], [0, 0, 0, 0])

    block_two = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4], [0, 1, 1, 1, 2])

    block_three = Block([[2, 3], [3, 3], [4, 3], [4, 4], [4, 5]], 4, [0, 1, 2], [0, 3, 4], [2, 3, 4], [0, 0, 0, 1, 2])

    block_four = Block([[2, 3], [2, 4], [2, 5], [2, 6]], 3, [0], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3])

    block_five = Block([[2, 3], [3, 3], [2, 4], [3, 4]], 2, [0, 1], [0, 2], [1, 3], [0, 0, 1, 1])

    blocks = [block_one, block_two, block_three, block_four, block_five]

    tower_space = [[0 for i in range(0, 30)] for j in range(0, 7)]

    for i in tower_space:
        temp = ""
        for j in i:
            if j:
                temp += "#"
            else:
                temp += "."
        # print(temp)

    moves = load_data("test_data_17")

    current_rock = -1
    is_falling = False
    highest_point = 0
    rock_counter = 0
    move_counter = 0
    max_move = len(moves[0])
    while rock_counter < 2:
        if move_counter == 0 and current_rock == 0:
            temp_space = ""
            for i in tower_space:
                if tower_space[highest_point - 1]:
                    temp_space = "#"
                else:
                    temp_space = "."
            print(temp_space)

        # if no rock, add a new one
        if not is_falling:
            # print(f"rock counter {rock_counter} height = {highest_point}")
            is_falling = True
            current_rock += 1
            if current_rock > 4:
                current_rock = 0
            #init block - this is shitty
            if current_rock == 0:
                blocks[current_rock] = Block([[2, 3], [3, 3], [4, 3], [5, 3]], 3, [0, 1, 2, 3], [0], [3], [0, 0, 0, 0])
            elif current_rock == 1:
                blocks[current_rock] = Block([[3, 3], [2, 4], [3, 4], [4, 4], [3, 5]], 4, [0, 1, 3], [0, 1, 4], [0, 3, 4], [0, 1, 1, 1, 2])
            elif current_rock == 2:
                blocks[current_rock] = Block([[2, 3], [3, 3], [4, 3], [4, 4], [4, 5]], 4, [0, 1, 2], [0, 3, 4], [2, 3, 4], [0, 0, 0, 1, 2])
            elif current_rock == 3:
                blocks[current_rock] = Block([[2, 3], [2, 4], [2, 5], [2, 6]], 3, [0], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3])
            else:
                blocks[current_rock] = Block([[2, 3], [3, 3], [2, 4], [3, 4]], 2, [0, 1], [0, 2], [1, 3], [0, 0, 1, 1])

            blocks[current_rock].set_starting_position(highest_point)
            # get next three moves
            shift_count = 0
            for i in range(0, 3):
                if moves[0][move_counter] == ">":
                    if blocks[current_rock].check_move_right(tower_space):
                        blocks[current_rock].shift_right()
                else:
                    if blocks[current_rock].check_move_left(tower_space):
                        blocks[current_rock].shift_left()
                move_counter += 1
                if move_counter == max_move:
                    move_counter = 0




            # blocks[current_rock].set_starting_position(highest_point + 3)
            # print(f"starting {blocks[current_rock].block_grid} {highest_point}")
            temp_tower_space = copy.deepcopy(tower_space)
            blocky = blocks[current_rock].block_grid
            # for i in blocky:
            #     temp_tower_space[i[0]][i[1]] = 2
            #
            # for i in range(0, len(temp_tower_space[0])):
            #     temp_row = ""
            #     for idx, x in enumerate(temp_tower_space):
            #         if x[-(i + 1)] == 2:
            #             temp_row += "@"
            #         elif x[-(i + 1)] == 1:
            #             temp_row += "#"
            #         else:
            #             temp_row += "."
            #     print(temp_row)
            # print("======================")


        # shift rock
        # print(f"move counter = {moves[0][move_counter]}")
        if moves[0][move_counter] == ">":
            # print("move right")
            if blocks[current_rock].check_move_right(tower_space):
                blocks[current_rock].shift_right()
        else:
            # print("move _left")
            if blocks[current_rock].check_move_left(tower_space):
                blocks[current_rock].shift_left()

        temp_tower_space = copy.deepcopy(tower_space)
        blocky = blocks[current_rock].block_grid
        # for i in blocky:
        #     temp_tower_space[i[0]][i[1]] = 2
        #
        # for i in range(0, len(temp_tower_space[0])):
        #     temp_row = ""
        #     for idx, x in enumerate(temp_tower_space):
        #         if x[-(i + 1)] == 2:
        #             temp_row += "@"
        #         elif x[-(i + 1)] == 1:
        #             temp_row += "#"
        #         else:
        #             temp_row += "."
        #     print(temp_row)
        # print("======================")

        move_counter += 1
        if move_counter == max_move:
            move_counter = 0

        # drop rock
        # check for collision / handle collision
        if blocks[current_rock].check_move_down(tower_space):
            blocks[current_rock].shift_down()
            blocky = blocks[current_rock].block_grid
            # print(blocky)

            # temp_tower_space = copy.deepcopy(tower_space)
            # for i in blocky:
            #     temp_tower_space[i[0]][i[1]] = 2
            #
            # for i in range(0, len(temp_tower_space[0])):
            #     temp_row = ""
            #     for idx, x in enumerate(temp_tower_space):
            #         if x[-(i+1)] == 2:
            #             temp_row += "@"
            #         elif x[-(i+1)] == 1:
            #             temp_row += "#"
            #         else:
            #             temp_row += "."
            #     print(temp_row)
            # print("======================")
        else:  # block is stopped - mark it and start a new block, calc new top
            # print(blocks[current_rock].block_grid)
            for i in blocks[current_rock].block_grid:
                tower_space[i[0]][i[1]] = 1

            # print(f"height {highest_point}")
            # for i in range(1, len(tower_space[0])+1):
            #     temp_row = ""
            #     for x in tower_space:
            #         if x[-i]:
            #             temp_row += "#"
            #         else:
            #             temp_row += "."
            #     print(temp_row)

            is_falling = False
            rock_counter += 1
            top_block = blocks[current_rock].get_top()
            if top_block[1] >= highest_point:
                # print("change highest point")
                highest_point = top_block[1] + 1

            # increase tower space?
            # if highest_point + 3 > len(tower_space[0]):
            #     height_diff = highest_point + 3 - len(tower_space[0])
            #     # print("redo it")
            for i in range(0, 2):
                for x in tower_space:
                    x.append(0)

    print(f"Highest point: {highest_point}")
