def load_data(file):
    output = []
    data = open(file, 'r')
    count = 0
    for line in data:
        temp = []
        for x in line.strip():
            temp.append(int(x))
            count += 1
        output.append(temp)

    data.close()
    return output


def check_visibility(index, grid, max_row, max_col):
    test_value = grid[index[0]][index[1]]
    # check rows
    top_half_hidden = False
    for r in range(0, index[0]):
        if grid[r][index[1]] >= test_value:
            top_half_hidden = True
            break
    bottom_half_hidden = False
    for r in range(max_row-1, index[0], -1):
        if grid[r][index[1]] >= test_value:
            bottom_half_hidden = True
    # check cols
    left_half_hidden = False
    for r in range(0, index[1]):
        if grid[index[0]][r] >= test_value:
            left_half_hidden = True
    right_half_hidden = False
    for r in range(max_col-1, index[1], -1):
        if grid[index[0]][r] >= test_value:
            right_half_hidden = True

    return top_half_hidden and bottom_half_hidden and right_half_hidden and left_half_hidden


def calc_score(index, grid, max_row, max_col):
    test_value = grid[index[0]][index[1]]
    # check rows
    top_half_score = 0
    for r in range(index[0]-1, -1, -1):
        if grid[r][index[1]] < test_value:
            top_half_score += 1
        else:
            top_half_score += 1
            break
    bottom_half_score = 0
    for r in range(index[0]+1, max_row):
        if grid[r][index[1]] < test_value:
            bottom_half_score += 1
        else:
            bottom_half_score += 1
            break
    # check cols
    left_half_score = 0
    for r in range(index[1]-1, -1, -1):
        if grid[index[0]][r] < test_value:
            left_half_score += 1
        else:
            left_half_score += 1
            break
    right_half_score = 0
    for r in range(index[1] + 1, max_col):
        if grid[index[0]][r] < test_value:
            right_half_score += 1
        else:
            right_half_score += 1
            break

    return top_half_score * bottom_half_score * right_half_score * left_half_score


if __name__ == "__main__":
    tree_grid = load_data("data_8")
    y = len(tree_grid[0])
    x = len(tree_grid)
    total_trees = y*x
    count = 0
    for i in range(1,x - 1):
        for j in range(1, y-1):
            if check_visibility([i,j], tree_grid, x, y):
                count += 1

    highest_score = 0
    for i in range(1,x - 1):
        for j in range(1, y-1):
            score = calc_score([i,j], tree_grid, x, y)
            if score > highest_score:
                highest_score = score

    print(f"Number of trees hidden {total_trees - count}")
    print(f"Highest tree visibility score {highest_score}")


