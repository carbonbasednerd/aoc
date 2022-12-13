def load_data(file):
    data = open(file, 'r')
    left_side = True
    left_list = []
    right_list = []
    for line in data:
        stripped = line.strip()
        if stripped != "":
            r = make_lists(stripped, 0)
            temp_array = r[0]
            if left_side:
                left_list.append(temp_array)
                left_side = False
            else:
                right_list.append(temp_array)
                left_side = True

    data.close()
    return [left_list, right_list]


def make_lists(data, index):
    temp_list = []
    num_buff = ""
    while index < len(data):
        if data[index] == "[":
            if index > 0:
                r = make_lists(data, index + 1)
                temp_list.append(r[0])
                index = r[1]
            else:
                index += 1
        elif data[index] == "]":
            if num_buff != "":
                temp_list.append(int(num_buff))
            return [temp_list, index + 1]
        elif data[index] == ",":
            if num_buff != "":
                temp_list.append(int(num_buff))
            num_buff = ""
            index += 1
        else:
            num_buff += data[index]
            index += 1
    return [temp_list, index+1]


def check_lists(left, right):
    for idx, item in enumerate(left):
        if idx >= len(right):
            return False

        if isinstance(item, list) and isinstance(right[idx], list):
            if item == right[idx]:
                continue
            return check_lists(item, right[idx])

        elif isinstance(item, list) or isinstance(right[idx], list):
            if not isinstance(item, list):
                if [item] == right[idx]:
                    continue
                return check_lists([item], right[idx])
            else:
                if [item] == right[idx]:
                    continue
                return check_lists(item, [right[idx]])
        else:
            if item > right[idx]:
                return False
            elif item < right[idx]:
                return True
    if len(left) < len(right):
        return True
    else:
        return False


# qs implemented lifted from stack overflow
def quicksort(xs):
    """Given indexable and slicable iterable, return a sorted list"""
    if xs: # if given list (or tuple) with one ordered item or more:
        pivot = xs[0]
        # below will be less than:
        below = [i for i in xs[1:] if check_lists(i, pivot)]
        # above will be greater than or equal to:
        above = [i for i in xs[1:] if not check_lists(i, pivot)]
        return quicksort(below) + [pivot] + quicksort(above)
    else:
        return xs # empty list


if __name__ == "__main__":
    results = load_data("data_13")

    counter = 0
    for i in range(0, len(results[0])):
        if results[0][i] == results[1][i]:
            continue
        if check_lists(results[0][i], results[1][i]):
            counter += (i+1)

    print(f"Number of valid list pairs: {counter}")

    merged_list = []
    for i in range(0, len(results[0])):
        merged_list.append(results[0][i])
        merged_list.append(results[1][i])
    merged_list.append([[2]])
    merged_list.append([[6]])

    sorted_list = quicksort(merged_list)
    div_1 = sorted_list.index([[2]]) + 1
    div_2 = sorted_list.index([[6]]) + 1
    print(f"Part two answer {div_2 * div_1}")
