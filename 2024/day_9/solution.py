def load_data(file):
    data = open(file, 'r')
    data_set = []
    for line in data:
        stripped_line = line.strip()
        for char in stripped_line:
            data_set.append(int(char))

    data.close()
    return data_set

def build_checksum(check_sum, block_id, value, checksum_counter):
    for i in range(0, value):
        check_sum += int(block_id * checksum_counter)
        checksum_counter += 1
    return check_sum, checksum_counter

def get_last_block_id(right_location, right_location_buffer, data_set):
    if right_location_buffer == []:
        right_location -= 2
        data_set.pop()
        data_set.pop()
        block_id = int(right_location / 2)
        for i in range(0, data_set[right_location]):
            right_location_buffer.append(block_id)
    return right_location_buffer.pop(), right_location, right_location_buffer

if __name__ == "__main__":
    data_set = load_data("/Users/jasonraffi/git/aoc/2024/day_9/data")
    data_set_part_two = data_set.copy()
    checksum = 0
    checksum_counter = 0
    left_location = 0
    right_location = len(data_set) - 1
    right_location_buffer = []

    #prep right location
    if right_location % 2 > 0:
        right_location -= 1
    
    block_id = int(right_location / 2)
    for i in range(0, data_set[right_location]):
        right_location_buffer.append(block_id)
    

    while left_location < right_location:
        if left_location % 2 == 0:
            checksum, checksum_counter = build_checksum(checksum, int(left_location/2), data_set[left_location], checksum_counter)
            left_location += 1
        else:
            while data_set[left_location] > 0:
                last_block_id, right_location, right_location_buffer = get_last_block_id(right_location, right_location_buffer, data_set)
                checksum, checksum_counter = build_checksum(checksum, last_block_id, 1, checksum_counter)
                data_set[left_location] -= 1
            left_location += 1

    # get the rest of the buffer
    for i in right_location_buffer:
        checksum, checksum_counter = build_checksum(checksum, i, 1, checksum_counter)
    print(f"checksum, part one: {checksum}")

    # part 2
    right_location = len(data_set_part_two) - 1
        #prep right location
    if right_location % 2 > 0:
        right_location -= 1

    override_buffer = {}
    while right_location != 0:
        block_id = int(right_location / 2)
        size = data_set_part_two[right_location]

        # loop through the data set to find an empty spot starting from the right
        searching = True
        search_pointer = 1
        while searching:
            if data_set_part_two[search_pointer] >= size:
                override_buffer.setdefault(search_pointer,[])
                for i in range(0, data_set_part_two[right_location]):
                    override_buffer[search_pointer].append(block_id)
                data_set_part_two[right_location] = size * -1
                data_set_part_two[search_pointer] -= size
                searching = False
            else:
                search_pointer += 2
                if search_pointer >= right_location:
                    searching = False
        
        right_location -= 2
    
    # once we have made the pass we loop through the data set to calculate the checksum
    # ignore -1 values and for odd numbers, skip anything that is not in the override buffer
    checksum = 0
    counter = 0
    for index, x in enumerate(data_set_part_two):
        if index % 2 == 0:
            if x >= 0:
                for i in range(0, x):
                    checksum += int(counter * int(index/2))
                    counter += 1
            else:
                counter += (x * - 1)
        else:
            if index in override_buffer:
                for i in override_buffer[index]:
                    checksum += int(i * counter)
                    counter += 1
                counter += x
            else:
                counter += x
    
    print(f"checksum, part two: {checksum}")



    # 2333133121414131402