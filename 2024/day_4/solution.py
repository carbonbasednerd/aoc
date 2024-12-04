import re

#prep data to get rid of \n
def load_data(file):
    data = open(file, 'r')
    found_in_row = 0
    data_set = []
    for line in data:
        stripped_line = line.strip()
        found_in_row += len(re.findall(r'(?=(XMAS|SAMX))', stripped_line))
        row_set = list(stripped_line)
        data_set.append(row_set)
               
    data.close()
    return data_set, found_in_row

if __name__ == "__main__":
    data, xmas_count = load_data("/Users/jasonraffi/git/aoc/2024/day_4/data")
    # count columns
    for i in range(0, len(data[0])):
        col_string = "".join([row[i] for row in data[:]])
        xmas_count += len(re.findall(r'(?=(XMAS|SAMX))', col_string))

    rows, cols = len(data), len(data[0])
    # back diagonals
    back_diagonals = [[data[i + start_row][i] for i in range(min(rows - start_row, cols))] for start_row in range(rows)] + [[data[i][i + start_col] for i in range(min(rows, cols - start_col))] for start_col in range(1, cols)]
    
    # forward diagonals
    forward_diagonals = [[data[i + start_row][cols - 1 - i] for i in range(min(rows - start_row, cols))]for start_row in range(rows)] + [[data[i][cols - 1 - (i + start_col)] for i in range(min(rows, cols - start_col))]for start_col in range(1, cols)]
    
    all_diagonals = back_diagonals + forward_diagonals
    for x in all_diagonals:
        diagonal_string = "".join(x)
        xmas_count += len(re.findall(r'(?=(XMAS|SAMX))', diagonal_string))
    
    print(f'Solution one :{xmas_count}')

    # part two
    part_two_counts = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if i == 0 or i == len(data)-1 or j == 0 or j == len(data[0])-1:
                continue
            if data[i][j] == 'A':
                # check the diagonals
                # back slash
                back_slash = False
                front_slash = False
                if data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S':
                    back_slash = True
                elif data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M':
                    back_slash = True
                if data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S':
                    front_slash = True
                elif data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M':
                    front_slash = True
                if back_slash and front_slash:
                    part_two_counts += 1
                    
    print(part_two_counts)    
