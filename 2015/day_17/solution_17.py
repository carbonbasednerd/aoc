def load_containers(file):
    containers = []
    data = open(file, 'r')
    for line in data:
        containers.append(int(line.strip()))

    data.close()
    return containers


def fill_buckets(buckets, volume, tracker, counter):
    buckets_filled = 0
    fill_tracker = tracker
    fill_counter = counter
    for count, bucket in enumerate(buckets):
        temp_volume = volume - bucket
        if temp_volume == 0:
            buckets_filled += 1
            fill_counter += 1
            if fill_counter in fill_tracker.keys():
                fill_tracker[fill_counter] += 1
            else:
                fill_tracker[fill_counter] = 1
            fill_counter -= 1
        elif temp_volume > 0:
            fill_counter += 1
            result = fill_buckets(buckets[count+1:], temp_volume, fill_tracker, fill_counter)
            fill_counter -= 1
            buckets_filled += result[0]
            fill_tracker = result[1]

    return [buckets_filled, fill_tracker]


if __name__ == "__main__":
    containers = load_containers("data_17")
    number_of_containers = len(containers)
    filled = 0
    result = fill_buckets(containers, 150, {}, 0)
    print(result[0])

    print(f"container combinations = {result[0]}")
    keys = list(result[1].keys())
    keys.sort()
    print(f"fill tracker {result[1][keys[0]]}")
