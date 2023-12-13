def load_data(file):
    data = open(file, 'r')
    count = 0
    seeds = []
    seed_ranges = []
    mapping = {}
    for line in data:
        if line == "\n":
            count += 1
            mapping[count] = []
            continue

        if count == 0:
            seeds = list(map(lambda x: int(x), line.strip().split(": ")[1].strip().split(" ")))
            # calculate seed ranges here
        else:
            if line.__contains__(":"):
                continue
            else:
                numbers = list(map(lambda x: int(x), line.strip().split(" ")))
                mapping[count].append([numbers[0], numbers[0] + numbers[2]-1, numbers[1], numbers[1]+numbers[2]-1])

    data.close()
    return seeds, mapping

def calculate_location(a_seed):
    temp = a_seed
    for key in results[1].keys():
        for range_map in results[1][key]:
            if temp in range(range_map[2], range_map[3]+1):
                print("calculate map")
                offset = temp - range_map[2]
                temp = range_map[0] + offset
                break
    return temp


if __name__ == "__main__":
    results = load_data("data")
    print(f"seeds {results[0]}")
    print(f"mapping {results[1]}")
    solution_1 = []
    for seed in results[0]:
        solution_1.append([seed, calculate_location(seed)])
    print(f"final locations 1 {solution_1}")
    minimum_location = 100000000000000
    for x in solution_1:
        minimum_location = min(minimum_location, x[1])
    print(f"solution 1 {minimum_location}")

    solution_2 = []
    # build new range of seeds for solution 2 - go through the algorithm as normal
   
