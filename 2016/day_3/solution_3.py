import re
def load_data(file):
    output = []
    data = open(file, 'r')
    for line in data:
        stripped = line.strip()
        split = re.split(r"[ ]* ", stripped)
        output.append(list(map(lambda x: int(x), split)))

    data.close()
    return output


def is_a_triangle(sides):
    if (sides[0] + sides[1]) <= sides[2]:
        return False
    if (sides[1] + sides[2]) <= sides[0]:
        return False
    if (sides[0] + sides[2]) <= sides[1]:
        return False
    return True


if __name__ == "__main__":
    potential_triangles = load_data("data_3")
    print(potential_triangles)
    valid_triangle_count = 0
    for measurements in potential_triangles:
        if is_a_triangle(measurements):
            valid_triangle_count += 1

    print(f"number of valid triangles:{valid_triangle_count}")

    valid_triangle_count = 0
    for x in range(2, len(potential_triangles), 3):
        triangle_1 = [potential_triangles[x - 2][0], potential_triangles[x - 1][0], potential_triangles[x][0]]
        triangle_2 = [potential_triangles[x - 2][1], potential_triangles[x - 1][1], potential_triangles[x][1]]
        triangle_3 = [potential_triangles[x - 2][2], potential_triangles[x - 1][2], potential_triangles[x][2]]

        if is_a_triangle(triangle_1):
            valid_triangle_count += 1

        if is_a_triangle(triangle_2):
            valid_triangle_count += 1

        if is_a_triangle(triangle_3):
            valid_triangle_count += 1

    print(f"number of valid triangles (part 2):{valid_triangle_count}")
