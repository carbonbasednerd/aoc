from multiprocessing import Process, Queue
import datetime

global_min = []
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
            for s in range(0, len(seeds), 2):
                seed_ranges.append([seeds[s], seeds[s] + seeds[s+1]-1])
        else:
            if line.__contains__(":"):
                continue
            else:
                numbers = list(map(lambda x: int(x), line.strip().split(" ")))
                mapping[count].append([numbers[0], numbers[0] + numbers[2]-1, numbers[1], numbers[1]+numbers[2]-1])

    data.close()
    return seeds, mapping, seed_ranges

def calculate_location(a_seed, res):
    temp = a_seed
    for key in res.keys():
        for range_map in res[key]:
            if temp in range(range_map[2], range_map[3]+1):
                offset = temp - range_map[2]
                temp = range_map[0] + offset
                break
    return temp


def calculate_location_reverse(a_seed, res):
    temp = a_seed
    for key in range(7, 0, -1):
        for range_map in res[key]:
            if temp in range(range_map[0], range_map[1]+1):
                offset = temp - range_map[0]
                temp = range_map[2] + offset
                break
    return temp


def threaded_solution(seed_range, r, return_queue):
    min_loc = 100000000000
    for s in range(seed_range[0], seed_range[1]+1):
        min_loc = min(min_loc, calculate_location(s, r))
    return_queue.put(min_loc)


if __name__ == "__main__":
    results = load_data("data")
    print(f"seeds {results[0]}")
    print(f"mapping {results[1]}")


    solution_1 = []
    for seed in results[0]:
        solution_1.append([seed, calculate_location(seed, results[1])])
    minimum_location = 100000000000000
    for x in solution_1:
        minimum_location = min(minimum_location, x[1])
    print(f"solution 1 {minimum_location}")

    start_time = datetime.datetime.now()

    solution_2 = []
    searching_for_min = True
    potential_min = 0
    # do the whole thing backward. Starting from 1 do the map backward until it maps to a seed in the provided ranges
    while searching_for_min:
        potential_min += 1
        seed = calculate_location_reverse(potential_min, results[1])
        for x in results[2]:
            if seed in range(x[0], x[1]+1):
                searching_for_min = False
                break

    print(f"solution 2 = {potential_min}")



    # Threaded solution - brute
    # q = Queue()
    # threads = []
    # for seed_map in results[2]:
    #     threads.append(Process(target=threaded_solution, args=(seed_map, results[1], q)))
    #
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    #
    # mins = []
    # while not q.empty():
    #     mins.append(q.get())

    end_time = datetime.datetime.now()

    # print(f"solution 2 {min(mins)}")
    print(f"total time: {end_time - start_time}")


# Takes too long - is there a way to shortcut the mapping? buffer the keys?
# Brute force took 7:09:39.470275
# Threaded : 1:58:47.937964 - 5 hours quicker but still slow. These should be done in minutes.
# going backwards: 0:06:49.405371
# Can we just do this backwards? https://www.reddit.com/r/adventofcode/comments/18b4b0r/2023_day_5_solutions/
# got the idea while looking there but didn't really see anything that suggested this course of action, specifically
