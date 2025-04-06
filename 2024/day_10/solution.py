def load_data(file):
    data = open(file, 'r')
    data_set = []
    trail_heads = []
    summits = []
    row_count = 0
    for line in data:
        stripped_line = line.strip()
        row_set = []
        column_count = 0
        for char in stripped_line:
            entry = int(char)
            row_set.append(entry)
            if entry == 0:
                trail_heads.append([row_count, column_count])
            if entry == 9:
                summits.append([row_count, column_count])
            column_count += 1
        data_set.append(row_set)
        row_count += 1

    data.close()
    return data_set, trail_heads, summits

def find_path(data_set, location, score, path=[]):
    loc_x = location[0]
    loc_y = location[1]
    step = data_set[loc_x][loc_y]
    path.append(location)
    if step == 9:
        score.append(path.copy())
        return score
    # Check north
    flag = False
    if loc_x > 0 and data_set[loc_x - 1][loc_y] == step + 1:
        score = find_path(data_set, [loc_x - 1, loc_y], score, path)
        path.pop()
        
    # Check south
    if loc_x < len(data_set) - 1 and data_set[loc_x + 1][loc_y] == step + 1:
        score = find_path(data_set, [loc_x + 1, loc_y], score, path)
        path.pop()
        
    # Check east
    if loc_y < len(data_set[0]) - 1 and data_set[loc_x][loc_y + 1] == step + 1:
        score = find_path(data_set, [loc_x, loc_y + 1], score, path)
        path.pop()
        
    # Check west
    if loc_y > 0 and data_set[loc_x][loc_y - 1] == step + 1:
        score = find_path(data_set, [loc_x, loc_y - 1], score, path)
        path.pop()
        
    return score
    

if __name__ == "__main__":
    data_set, trail_heads, summits = load_data("/Users/jasonraffi/git/aoc/2024/day_10/data")

    # probably a recursive function to find the path
    total_summit_score = 0
    total_modified_sumimit_score = 0
    for trail_head in trail_heads:
        result = find_path(data_set, trail_head, [])
        summit_count = set()
        total_modified_sumimit_score += len(result)
        for i in result:
            if i[-1] in summits:
                summit_count.add(f"{i[-1][0]} {i[-1][1]}")
        total_summit_score += len(summit_count)
    
    print(f"total_summit_score {total_summit_score}")
    print(f"total_summit_score part 2 {total_modified_sumimit_score}")
    