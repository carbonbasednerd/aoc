from collections import deque
import time
# 6 11 33023 4134 564 0 8922422 688775
# 125 17

def find_sequence(arr, sequence):
    sequence_len = len(sequence)
    for i in range(len(arr) - sequence_len + 1):
        if arr[i:i + sequence_len] == sequence:
            return i  # Return starting index
    return -1

if __name__ == "__main__":
    # data_set = [125, 17]
    data_set = [6, 11, 33023, 4134, 564, 0, 8922422, 688775]
    # intial_data_set = [125, 17]
    intial_data_set = [6, 11, 33023, 4134, 564, 0, 8922422, 688775]
    print(find_sequence(data_set, intial_data_set))
    prior_change = 0
    for i in range(0, 35):
        buffer = []
        timestamp = time.time()
        for x in data_set:
            if x == 0:
                buffer.append(1)
            elif len(str(x)) % 2 == 0:
                mid = len(str(x)) // 2
                buffer.append(int(str(x)[mid:]))
                buffer.append(int(str(x)[0:mid]))
            else:
                buffer.append(x*2024)
        prior_len = len(buffer) - len(data_set)
        index_sequence = find_sequence(buffer, intial_data_set)
        if index_sequence != -1:
            print(f"iteration {i} index sequence {index_sequence}")

        data_set = buffer
        print(f"iteration {i} prior len {prior_len} prior change {prior_len - prior_change} time {time.time() - timestamp}")
        prior_change = prior_len
    print(f"number of stones in data set part 1: {len(data_set)}")
