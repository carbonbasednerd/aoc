from functools import reduce

def load_data(file, apply_dampener=False):
    data = open(file, 'r')
    safe_count = 0
    for line in data:
        stripped_line = line.strip()
        split_data = list(map(int, stripped_line.split()))
        result = calculate_distances(split_data)
        fail_count = 0
        decreasing = result[0] < 0
        for index, x in enumerate(result):
            if not check_if_secure(x, decreasing):
                fail_count += 1
        
        # no joy try removing them all I suppose
        if apply_dampener:
            if fail_count == 0:
                safe_count += 1
            else:
                #retry all
                for index, x in enumerate(split_data):
                    new_list = split_data[:index] + split_data[index+1:]
                    distance = calculate_distances(new_list)
                    fc = 0
                    d = distance[0] < 0
                    for x in distance:
                        if not check_if_secure(x, d):
                            fc += 1
                            break
                    if fc == 0:
                        safe_count += 1
                        break
        else:
            if fail_count == 0:
                safe_count += 1
                
    data.close()
    return safe_count

def check_if_secure(level, decreasing):
    if level == 0:
        return False
    if decreasing:
        if level > 0:
            return False
    else:
        if level < 0:
            return False

    if abs(level) not in range(1, 4):
        return False
    
    return True


def calculate_distances(numbers):
    return [b-a for a, b in zip(numbers, numbers[1:])]

if __name__ == "__main__":
    result = load_data('/Users/jasonraffi/git/aoc/2024/day_2/data')
    print(f"result part 1 {result}")
    result = load_data('/Users/jasonraffi/git/aoc/2024/day_2/data', True)
    print(f"result part 2 {result}")


# 566