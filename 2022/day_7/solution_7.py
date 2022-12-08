def load_data(file):
    data = open(file, 'r')
    current_directory = "/"
    directories = {}
    directories[current_directory] = {"children": [], "size": 0, "parent": current_directory}
    for line in data:
        stripped_line = line.strip()
        if stripped_line[0] == '$':
            command_array = stripped_line.split(" ")
            if command_array[1] == "cd":
                if command_array[2] == "..":
                    current_directory = directories[current_directory]["parent"]
                elif command_array[2] == "/":
                    current_directory = "/"
                else:
                    temp = current_directory+"/"+command_array[2]
                    if temp not in list(directories.keys()):
                        directories[temp] = {"children": [], "size": 0, "parent": current_directory}
                    current_directory = temp
        else:  # read output
            output_array = stripped_line.split(" ")
            if output_array[0] == "dir":
                if output_array[1] not in list(directories.keys()):
                    directories[output_array[1]] = {"children": [], "size": 0, "parent": current_directory}
                directories[current_directory]["children"].append(output_array[1])
            else:
                if current_directory == "/":
                    directories[current_directory]["size"] += int(output_array[0])
                else:
                    directories[current_directory]["size"] += int(output_array[0])
                    temp_dir = directories[current_directory]["parent"]
                    flag = True
                    while flag:
                        directories[temp_dir]["size"] += int(output_array[0])
                        if temp_dir == "/":
                            flag = False
                        else:
                            temp_dir = directories[temp_dir]["parent"]

    data.close()
    return directories


if __name__ == "__main__":
    directory_structure = load_data("data_7")
    print(directory_structure)
    total_space = directory_structure["/"]["size"]
    free_space = 70000000 - total_space
    needed_space = 30000000 - free_space
    total = 0
    to_delete = free_space
    difference = 30000000
    print(f"total {total_space} free {free_space} needed {needed_space}")
    for k in directory_structure.keys():
        s = directory_structure[k]["size"]
        if s <= 100000:
            total += s
        if s >= needed_space:
            if abs(s - needed_space) < abs(to_delete - needed_space):
                to_delete = s

    print(f"Puzzle solution part 1 {total}")
    print(f"Puzzle solution part 2 {to_delete}")
