import copy


def load_data(file):
    data = open(file, 'r')
    sections = {}
    moves = []
    setting_state = 0
    for line in data:
        stripped_line = line.strip('\n')
        if stripped_line == "" or stripped_line[1] == "1":
            setting_state = 1
        elif "move" in stripped_line:
            setting_state = 2

        if setting_state == 0:
            section_count = 0
            past_char = ""
            for i, c in enumerate(stripped_line):
                # read in character by character
                if (i % 4) == 0:
                    if past_char != "":
                        if section_count not in list(sections.keys()):
                            sections[section_count] = [past_char]
                        else:
                            sections[section_count].insert(0, past_char)
                        past_char = ""

                    section_count += 1
                if c.isalnum():
                    past_char = c

            if section_count not in list(sections.keys()):
                sections[section_count] = [past_char]
            else:
                sections[section_count].insert(0, past_char)
        elif setting_state == 1:
            print("skipping")
        else:
            temp_moves = []
            split_string = stripped_line.split(" ")
            for e in split_string:
                if e.isnumeric():
                    temp_moves.append(int(e))
            moves.append(temp_moves)
    data.close()
    return [sections, moves]


def cratemover_logic(section_to_map, count, from_section, to_section, is_9000):
    split_index = len(section_to_map[from_section]) - count
    sub_list = section_to_map[from_section][split_index:]

    if is_9000:
        sub_list.reverse()

    section_to_map[from_section] = section_to_map[from_section][:split_index]
    section_to_map[to_section].extend(sub_list)

    return section_to_map


def cratemover_top_boxes(section_to_map):
    sorted_keys = list(section_to_map.keys())
    sorted_keys.sort()
    top_box_string = ""
    for key in sorted_keys:
        top_box_string += section_to_map[key][-1]

    return top_box_string


if __name__ == "__main__":
    result = load_data("data_5")
    section_map_9000 = copy.deepcopy(result[0])
    section_map_9001 = copy.deepcopy(result[0])
    moves = result[1]

    for move in moves:
        count = move[0]
        from_section = move[1]
        to_section = move[2]
        section_map_9000 = cratemover_logic(section_map_9000, count, from_section, to_section, True)
        section_map_9001 = cratemover_logic(section_map_9001, count, from_section, to_section, False)

    top_box_string_9000 = cratemover_top_boxes(section_map_9000)
    top_box_string_9001 = cratemover_top_boxes(section_map_9001)

    print(f"Top boxes from 9000 {top_box_string_9000}")
    print(f"Top boxes from 9001 {top_box_string_9001}")
