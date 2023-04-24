from functools import reduce

def load_data(file):
    data = open(file, 'r')
    result = []
    count = 0
    for line in data:
        weight = int(line.strip())
        count += weight
        result.append(weight)

    data.close()
    return [result, count]


def make_buckets(remaining_weights, current_bucket, max_size, found_buckets):
    # print(f"bucket: {current_bucket} total:{sum(current_bucket)}")
    new_weight = sum(current_bucket)
    if new_weight == max_size:
        # print(f"found a match: {current_bucket}")
        found_buckets.append(current_bucket)
        return found_buckets
    elif new_weight < bucket_size:
        # should check for remaining weights using the last value
        if len(remaining_weights) == 0:
            return found_buckets

        for next_weight in range(1, len(remaining_weights)+1):
            trial_bucket = current_bucket.copy()
            trial_bucket.append(remaining_weights[next_weight-1])
            result = make_buckets(remaining_weights[next_weight:], trial_bucket, max_size, [])
            if len(result) > 0:
                # print(f"merging: found buckets: {found_buckets} with result {result}")
                found_buckets.extend(result)
                # print(f"after merge: {found_buckets}")

        return found_buckets
    else:
        # at this point it's too big and we should return an empty bucket
        # print(f"Too big: no further matches possible {current_bucket}")
        return found_buckets


if __name__ == "__main__":
    data = load_data("data_24")
    weights = data[0]
    bucket_size = sum(weights) / 4  # part 2
    # bucket_size = sum(weights) / 3  # part 1
    print(f"Starting bucket size {bucket_size}")

    filled_buckets = []
    for w in range(1, len(weights)):
        weight = weights[w-1]
        # print(f"weight:{weight}, weights:{weights[w:]}, bucket size:{bucket_size}")
        r = make_buckets(weights[w:], [weight], bucket_size, [])
        filled_buckets.extend(r)
        # print(f"output:{r}")

    # print(f"all found filled buckets: {filled_buckets}")

    # generates a list of number of packages in bucket and it's "QE" score - all weights in the list multiplies together
    mapped = list(map(lambda b: [len(b), reduce((lambda x, y: x * y), b)], filled_buckets))
    # print(f"Mapped: {mapped}")

    smallest_bucket = mapped[0]
    # now find the lowest QE score
    # print(f"Smallest bucket: {smallest_bucket}")
    for x in mapped[1:]:
        # print(f"x val:{x}")
        if x[0] < smallest_bucket[0]:
            smallest_bucket = x
        elif x[0] == smallest_bucket[0]:
            if x[1] < smallest_bucket[1]:
                smallest_bucket = x

    print(f"smallest bucket found. number of items:{smallest_bucket[0]} and QE score: {smallest_bucket[1]}")
