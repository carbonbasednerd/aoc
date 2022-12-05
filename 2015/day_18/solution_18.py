import copy


def load_containers(file):
    light_map = []
    data = open(file, 'r')
    for line in data:
        stripped = line.strip()
        temp_row = []
        for c in stripped:
            temp_row.append(c == "#")
        light_map.append(temp_row)

    data.close()
    return light_map


def print_light_map(light_map):
    for row in light_map:
        temp = ""
        for col in row:
            if col:
                temp += "#"
            else:
                temp += "."
        print(temp)


def check_light_rule(light_map, row, col, width, height):
    number_of_on_lights = nearby_on_lights(light_map, row, col, width, height)
    if light_map[row][col]:  # light is on
        if number_of_on_lights == 2 or number_of_on_lights == 3:
            return True
        else:
            return False
    else:
        if number_of_on_lights == 3:
            return True
        else:
            return False


def nearby_on_lights(light_map, row, col, width, height):
    count = 0
    # top row
    if row-1 >= 0:
        if light_map[row-1][col]:
            count += 1
        if col-1 >= 0:
            if light_map[row-1][col-1]:
                count += 1
        if col+1 < width:
            if light_map[row-1][col+1]:
                count += 1
    # middle row
    if col-1 >= 0:
        if light_map[row][col-1]:
            count += 1
    if col+1 < width:
        if light_map[row][col+1]:
            count += 1

    # bottom row
    if row+1 < height:
        if light_map[row+1][col]:
            count += 1
        if col-1 >= 0:
            if light_map[row+1][col-1]:
                count += 1
        if col+1 < width:
            if light_map[row+1][col+1]:
                count += 1

    return count


def count_lights_on(lights):
    total_lights_on = 0
    for row in lights:
        for col in row:
            if col:
                total_lights_on += 1
    return total_lights_on

if __name__ == "__main__":
    max = 100
    original_map = load_containers("data_18")
    light_map = copy.deepcopy(original_map)
    light_map_2 = copy.deepcopy(original_map)
    light_map_width = len(light_map[0])
    light_map_height = len(light_map)
    for count in range(0, max):
        new_map = []
        for i, row in enumerate(light_map):
            new_row = []
            for j, col in enumerate(row):
                new_row.append(check_light_rule(light_map, i, j, light_map_width, light_map_height))
            new_map.append(new_row)

        # print(f"map after {count+1} pass")
        # print_light_map(new_map)
        light_map = copy.deepcopy(new_map)

    print(f"light on at the end of {max} runs {count_lights_on(light_map)}")
    print("Running part two...")

    # prep bad lights
    light_map_2[0][0] = True
    light_map_2[0][light_map_width - 1] = True
    light_map_2[light_map_height - 1][light_map_width - 1] = True
    light_map_2[light_map_height - 1][0] = True

    for count in range(0, max):
        new_map = []
        for i, row in enumerate(light_map_2):
            new_row = []
            for j, col in enumerate(row):
                if (i == 0 and j == 0) or (i == 0 and j == light_map_width - 1) or (i == light_map_height - 1 and j == light_map_width - 1) or (i == light_map_height - 1 and j == 0):
                    new_row.append(True)
                else:
                    new_row.append(check_light_rule(light_map_2, i, j, light_map_width, light_map_height))
            new_map.append(new_row)

        light_map_2 = copy.deepcopy(new_map)

    print(f"light on at the end of {max} runs {count_lights_on(light_map_2)}")


