import copy

def load_data(file):
    data = open(file, 'r')
    data_set = []
    row_count = 0
    start_point = [0,0]
    for line in data:
        stripped_line = line.strip()
        row = []
        for index, x in enumerate(stripped_line):
            if x == "^":
                start_point = [row_count, index]
                row.append(".")
            else:
                row.append(x)
        data_set.append(row)
        row_count += 1
    data.close()
    return data_set, start_point

def print_board(board):
    for row in board:
        print(row)
    print("------------------")

def get_path(board):
    path = []
    for row_dex, row in enumerate(board):
        for col_dex, col in enumerate(row):
            if col == "X":
                path.append([row_dex,col_dex])
    return path

def score_board(board):
    counter = 0
    for row in board:
        for col in row:
            if col == "X":
                counter += 1
    return counter

def move(location, facing, board):
    x = location[0]
    y = location[1]
    if facing == 0: # north
        if board[x-1][y]  == "#" or board[x-1][y] == "O":
            return [x,y], facing + 1, True
        else:
            board[x][y] = "X"
            return [x-1, y], facing, False
    elif facing == 1: # east
        if board[x][y+1]  == "#" or board[x][y+1] == "O":
            return [x,y], facing + 1, True
        else:
            board[x][y] = "X"
            return [x, y+1], facing, False
    elif facing == 2: # south
        if board[x+1][y]  == "#" or board[x+1][y] == "O":
            return [x,y], facing + 1, True
        else:
            board[x][y] = "X"
            return [x+1, y], facing, False
    elif facing == 3: # west
        if board[x][y-1]  == "#" or board[x][y-1] == "O":
            return [x,y], 0, True
        else:
            board[x][y] = "X"
            return [x, y-1], facing, False

if __name__ == "__main__":
    board, start_point = load_data("/Users/jasonraffi/git/aoc/2024/day_6/data")
    
    facing = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    still_on_board = True
    current_point = start_point
    game_board = board
    while still_on_board:
        current_point, facing, collision = move(current_point, facing, game_board)
        if facing == 0: # north
            if current_point[0] == 0:
                board[current_point[0]][current_point[1]] = "X"
                still_on_board = False
        elif facing == 1: # east
            if current_point[1] == len(board[0])-1:
                board[current_point[0]][current_point[1]] = "X"
                still_on_board = False
        elif facing == 2: # south
            if current_point[0] == len(board)-1:
                board[current_point[0]][current_point[1]] = "X"
                still_on_board = False
        elif facing == 3: # west
            if current_point[1] == 0:
                board[current_point[0]][current_point[1]] = "X"
                still_on_board = False
    
    print(f"Part 1 Score: {score_board(board)} start point: {start_point}")

    the_path = get_path(board)
    # Part 2
    loops = 0
    past_point = []
    new_board = board
    for point in the_path:
        facing = 0 # 0 = up, 1 = right, 2 = down, 3 = left
        still_on_board = True
        current_point = start_point
        collisions = {}
        loop_counter = 0
        if point != start_point:
            new_board[point[0]][point[1]] = "O"
            if past_point != []:
                new_board[past_point[0]][past_point[1]] = "X"
            past_point = point
        else:
            continue
        while still_on_board:
            current_point, facing, collision = move(current_point, facing, new_board)
            if collision:
                old_facing = facing - 1
                if old_facing < 0:
                    old_facing = 3

                collisions.setdefault((old_facing, current_point[0], current_point[1]), 0)
                collisions[(old_facing, current_point[0], current_point[1])] += 1
                if collisions[(old_facing, current_point[0], current_point[1])] == 2:
                    still_on_board = False
                    loops += 1
                    continue    
            

            if facing == 0: # north
                if current_point[0] == 0:
                    new_board[current_point[0]][current_point[1]] = "X"
                    still_on_board = False
            elif facing == 1: # east
                if current_point[1] == len(board[0])-1:
                    new_board[current_point[0]][current_point[1]] = "X"
                    still_on_board = False
            elif facing == 2: # south
                if current_point[0] == len(board)-1:
                    new_board[current_point[0]][current_point[1]] = "X"
                    still_on_board = False
            elif facing == 3: # west
                if current_point[1] == 0:
                    new_board[current_point[0]][current_point[1]] = "X"
                    still_on_board = False
    
    print(f"Part 2 Score: loops: {loops}")


# 139 too low - I think it needs to track when it hits the same point twice but in the same direction