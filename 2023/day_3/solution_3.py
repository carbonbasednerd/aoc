def load_data(file):
    data = open(file, 'r')
    data_array = []
    for line in data:
        row = []
        stripped_line = line.strip()
        for entry in stripped_line:
            if entry not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "*"):
                row.append("X")
            else:
                row.append(entry)
        data_array.append(row)

    return data_array


def get_part_number(x, y, e_map):
    part_num = e_map[x][y]
    can_check_left = True
    left_count = y-1
    while can_check_left:
        if left_count < 0 or e_map[x][left_count] in (".", "X", "*"):
            can_check_left = False
        else:
            part_num = e_map[x][left_count]+part_num
        left_count -= 1

    can_check_right = True
    right_count = y+1
    while can_check_right:
        if right_count == len(e_map[x]) or e_map[x][right_count] in (".", "X", "*"):
            can_check_right = False
        else:
            part_num += e_map[x][right_count]
        right_count += 1

    print(f"part num: {part_num} x:{x} y:{y}")
    return int(part_num)


def check_for_part(xloc, yloc, engine_map, is_gear):
    parts = []
    # check top
    if xloc != 0:
        temp_parts = set()
        if engine_map[xloc-1][yloc] not in (".", "X", "*"):
            temp_parts.add(get_part_number(xloc-1, yloc, engine_map))
        #check top left
        if yloc != 0:
            if engine_map[xloc-1][yloc-1] not in (".", "X", "*"):
                temp_parts.add(get_part_number(xloc-1, yloc-1, engine_map))
        # check top right
        if yloc != len(engine_map[xloc-1])-1:
            if engine_map[xloc-1][yloc+1] not in (".", "X", "*"):
                temp_parts.add(get_part_number(xloc-1, yloc+1, engine_map))
        parts.extend(temp_parts)

    # Check Left
    if yloc != 0:
        if engine_map[xloc][yloc-1] not in (".", "X", "*"):
            parts.append(get_part_number(xloc, yloc-1, engine_map))

    # Check Right
    if yloc != len(engine_map[xloc])-1:
        if engine_map[xloc][yloc+1] not in (".", "X", "*"):
            parts.append(get_part_number(xloc, yloc+1, engine_map))

    # Check Bottom
    if xloc != len(engine_map)-1:
        temp_parts = set()
        if engine_map[xloc+1][yloc] not in (".", "X", "*"):
            temp_parts.add(get_part_number(xloc+1, yloc, engine_map))
        #check bottom left
        if yloc != 0:
            if engine_map[xloc+1][yloc-1] not in (".", "X", "*"):
                temp_parts.add(get_part_number(xloc+1, yloc-1, engine_map))
        # check top right
        if yloc != len(engine_map[xloc+1])-1:
            if engine_map[xloc+1][yloc+1] not in (".", "X", "*"):
                temp_parts.add(get_part_number(xloc+1, yloc+1, engine_map))
        parts.extend(temp_parts)

    gear_value = 0
    if is_gear and len(parts) == 2:
        gear_value = parts[0] * parts[1]
    return parts, gear_value


if __name__ == "__main__":
    result = load_data("data")
    print(len(result))
    part_numbers_found = 0
    gear_total = 0
    for x in range(0, len(result)):
        for y in range(0, len(result[x])):
            if result[x][y] == "X" or result[x][y] == "*":
                parts, gear = check_for_part(x, y, result, result[x][y] == "*")
                part_numbers_found += sum(parts)
                gear_total += gear

    print(f"solution 1 {part_numbers_found}")
    print(f"solution 2 {gear_total}")


# 521840 too low