from itertools import combinations

def load_data(file):
    data = open(file, 'r')
    data_set = {}
    row_count= 0
    total = 0
    line_count = 0
    for line in data:
        stripped_line = line.strip()
        line_count = len(stripped_line)
        for index, char in enumerate(stripped_line):
            total += 1
            if char != ".":
                data_set.setdefault(char, []).append([row_count, index])
        row_count += 1

    data.close()
    return data_set, row_count, line_count

if __name__ == "__main__":
    data_set, row_count, line_count = load_data("/Users/jasonraffi/git/aoc/2024/day_8/data")
    antinodes = {}
    for antenna in data_set:
        pairs = list(combinations(data_set[antenna], 2))
        for pair in pairs:
            delta_y = pair[1][1] - pair[0][1]
            delta_x = pair[1][0] - pair[0][0]

            antinodes.setdefault((pair[0][0], pair[0][1]), 0)
            antinodes.setdefault((pair[1][0], pair[1][1]), 0)
            antinodes[(pair[0][0], pair[0][1])] += 1
            antinodes[(pair[1][0], pair[1][1])] += 1

            antinode_1 = (0,0)
            delta_x_1 = delta_x
            delta_y_1 = delta_y
            while antinode_1[0] >= 0 and antinode_1[0] < row_count and antinode_1[1] >=0 and antinode_1[1] < line_count:
                antinode_1 = (pair[1][0] + delta_x_1, pair[1][1] + delta_y_1)
                antinodes.setdefault(antinode_1, 0)
                antinodes[antinode_1] += 1
                delta_x_1 += delta_x
                delta_y_1 += delta_y

            antinode_2 = (0,0)
            delta_x_2 = delta_x
            delta_y_2 = delta_y
            while antinode_2[0] >= 0 and antinode_2[0] < row_count and antinode_2[1] >=0 and antinode_2[1] < line_count:
                antinode_2 = (pair[0][0] - delta_x_2, pair[0][1] - delta_y_2)
                antinodes.setdefault(antinode_2, 0)
                antinodes[antinode_2] += 1
                delta_x_2 += delta_x
                delta_y_2 += delta_y 
            
    count = 0
    for key in antinodes:
        if key[0] >= 0 and key[0] < row_count and key[1] >=0 and key[1] < line_count:
            count += 1
    print(count)