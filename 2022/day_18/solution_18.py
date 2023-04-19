import copy

def load_data(file):
    output = []
    data = open(file, 'r')
    for line in data:
        cube = []
        split_input = line.strip().split(",")
        cube.append([int(split_input[0]), int(split_input[1]), int(split_input[2])])
        # 1 +x, y, z
        cube.append([cube[0][0] + 1, cube[0][1], cube[0][2]])
        # 2 +x, +y, z
        cube.append([cube[0][0] + 1, cube[0][1] + 1, cube[0][2]])
        # 3 x, +y, z
        cube.append([cube[0][0], cube[0][1] + 1, cube[0][2]])
        # 4 x, y, +z
        cube.append([cube[0][0], cube[0][1], cube[0][2] + 1])
        # 5 +x, y, +z
        cube.append([cube[0][0] + 1, cube[0][1], cube[0][2] + 1])
        # 6 +x, +y, +z
        cube.append([cube[0][0] + 1, cube[0][1] + 1, cube[0][2] + 1])
        # 7 x, +y, +z
        cube.append([cube[0][0], cube[0][1] + 1, cube[0][2] + 1])

        output.append(cube)
    data.close()
    return output


if __name__ == "__main__":
    cubes = load_data("test_data_18")
    # print(cubes)
    max_surface_area = len(cubes) * 6

    faces = [[0, 1, 2, 3], [1, 2, 5, 6], [0, 3, 4, 7], []]

    hidden = 0

    for idx, i in enumerate(cubes):
        for j in range(idx+1, len(cubes)):
            point_count = 0
            for point in i:
                if point in cubes[j]:
                    point_count += 1

            if point_count == 4:
                max_surface_area -= 2

            elif point_count == 0:
                temp_i = copy.deepcopy(i)


                for point in i:
                    temp_point = copy.copy(point)
                    temp_point[0] = temp_point[0] + 1
                    temp_point[1] = temp_point[1] + 1
                    temp_point[2] = temp_point[2] + 1

                    # cube.append([int(split_input[0]), int(split_input[1]), int(split_input[2])])
                    # # +x, y, z
                    # cube.append([cube[0][0] + 1, cube[0][1], cube[0][2]])
                    # # +x, +y, z
                    # cube.append([cube[0][0] + 1, cube[0][1] + 1, cube[0][2]])
                    # # x, +y, z
                    # cube.append([cube[0][0], cube[0][1] + 1, cube[0][2]])
                    # # x, y, +z
                    # cube.append([cube[0][0], cube[0][1], cube[0][2] + 1])
                    # # +x, y, +z
                    # cube.append([cube[0][0] + 1, cube[0][1], cube[0][2] + 1])
                    # # +x, +y, +z
                    # cube.append([cube[0][0] + 1, cube[0][1] + 1, cube[0][2] + 1])
                    # # x, +y, +z
                    # cube.append([cube[0][0], cube[0][1] + 1, cube[0][2] + 1])


                    if temp_point in cubes[j]:
                        point_count += 1
                if point_count == 4:
                    hidden += 6


    print(f"max surface area {max_surface_area} hidden {hidden}")
