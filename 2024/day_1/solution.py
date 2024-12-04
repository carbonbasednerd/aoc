def load_data(file):
    data = open(file, 'r')
    left = []
    right = []
    count= {}
    for line in data:
        stripped_line = line.strip()
        split_data = stripped_line.split("   ")
        left.append(int(split_data[0]))
        right.append(int(split_data[1]))
        count.setdefault(split_data[1], 0)
        count[split_data[1]] += 1

    data.close()
    return [left, right, count]

def get_difference(entry1, entry2):
    return [abs(x - y) for x, y in zip(left, right)]

if __name__ == "__main__":
    left, right, count = load_data('/Users/jasonraffi/git/aoc/2024/day_1/data')
    left.sort()
    right.sort()
    print(sum(get_difference(left, right)))
    score = 0
    for x in left:
        score += x * count.get(str(x), 0)
    print(score)

