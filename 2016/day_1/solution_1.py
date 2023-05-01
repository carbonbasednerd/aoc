from sympy import Point, Segment

directions = [0, 1, 2, 3] #N, E, S, W
lines = []

def load_data(file):
    data = open(file, 'r')
    result = []
    for line in data:
        stripped = line.strip()
        result = stripped.split(", ")
    data.close()
    return result

def determine_facing(current, next):
    if next == "R":
        if current < 3:
            current += 1
        else:
            current = 0
    else:
        if current > 0:
            current -= 1
        else:
            current = 3
    return current

def check_for_intersection(new_line):
    for line in lines[0:-1]:
        l = line.intersection(new_line)
        print(f"checking line:{line} and {new_line} found:{l}")

        if len(l) > 0:
            return l

    return []


if __name__ == "__main__":
    commands = load_data("data_1")

    x = 0
    y = 0
    facing = 0   # degrees
    intersection_point = []

    for command in commands:
        to_turn = command[0]
        steps = int(command[1:])
        facing = determine_facing(facing, to_turn)
        point1 = Point(x, y)
        if facing == 0:
            y += steps
        elif facing == 1:
            x += steps
        elif facing == 2:
            y -= steps
        elif facing == 3:
            x -= steps

        point2 = Point(x, y)
        segment = Segment(point1, point2)
        print(f"Line: {segment}")
        if len(intersection_point) == 0:
            intersection_point = check_for_intersection(segment)
            lines.append(segment)
        else:
            print(f"intersection:{intersection_point}")

    intersection_x = abs(intersection_point[0].x)
    intersection_y = abs(intersection_point[0].y)

    print(f"x:{abs(x)} y:{abs(y)} total:{abs(x) + abs(y)} intersection point:{intersection_point} distance:{intersection_x + intersection_y}")
