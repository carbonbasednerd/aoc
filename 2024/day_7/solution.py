import numbers

def load_data(file):
    data = open(file, 'r')
    data_set = []
    for line in data:
        stripped_line = line.strip()
        test_value = stripped_line.split(": ")
        numbers = test_value[1].strip().split(" ")
        data_set.append([int(test_value[0])]+list(map(int, numbers)))

    data.close()
    return data_set

def calc_solution(current_total, numbers):
    if len(numbers) > 0:
        total_1 = current_total + numbers[0]
        total_2 = current_total * numbers[0]
        total_3 = int(str(current_total) + str(numbers[0]))
        result_1 = (calc_solution(total_1, numbers[1:]))
        result_2 = (calc_solution(total_2, numbers[1:]))
        result_3 = (calc_solution(total_3, numbers[1:]))
        return [result_1, result_2, result_3]

    return [current_total]

def flatten_list(nested):
    flattened = []
    for item in nested:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))  # Recursively flatten
        else:
            flattened.append(item)
    return flattened


if __name__ == "__main__":
    data_set = load_data("/Users/jasonraffi/git/aoc/2024/day_7/data")
    solution_counter = 0
    not_solved = 0
    for row in data_set:
        key = row[0]
        data_list = row[1:]
        first_pass_1 = data_list[0] + data_list[1]
        first_pass_2 = data_list[0] * data_list[1]
        first_pass_3 = int(str(data_list[0]) + str(data_list[1]))
        t1 = calc_solution(first_pass_1, data_list[2:])
        t2 = calc_solution(first_pass_2, data_list[2:])
        t3 = calc_solution(first_pass_3, data_list[2:])
        result = flatten_list(t1) + flatten_list(t2) + flatten_list(t3)
        solved = False
        for x in result:
            if x == key:
                solution_counter += x
                solved = True
                break
    print(f"Solution counter: {solution_counter} not solved: {not_solved}")

    # 285 is too low
    # 5030892083587 is too low
    # 5030892084481