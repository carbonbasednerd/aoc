def load_data(file, part_2, max_size):
    output = []
    data = open(file, 'r')
    min_col = 1000
    max_col = 0
    min_row = 1000
    max_row = 0
    for line in data:
        split = line.strip().split(" ")
        sensor_col = int(split[2].replace("x=", "").replace(",", ""))
        sensor_row = int(split[3].replace("y=", "").replace(":", ""))
        beacon_col = int(split[8].replace("x=", "").replace(",", ""))
        beacon_row = int(split[9].replace("y=", ""))

        if part_2:
            if sensor_col < 0:
                sensor_col = 0
            elif sensor_col > max_size:
                sensor_col = max_size

            if sensor_row < 0:
                sensor_row = 0
            elif sensor_row > max_size:
                sensor_row = max_size

            if beacon_col < 0:
                beacon_col = 0
            elif beacon_col > max_size:
                beacon_col = max_size

            if beacon_row < 0:
                beacon_row = 0
            elif beacon_row > max_size:
                beacon_row = max_size

        min_col = min(sensor_col, beacon_col, min_col)
        min_row = min(sensor_row, beacon_row, min_row)
        max_col = max(sensor_col, beacon_col, max_col)
        max_row = max(sensor_row, beacon_row, max_row)
        output.append(Sensor([sensor_row, sensor_col], [beacon_row, beacon_col]))

    data.close()
    return [output, min_col, max_col, min_row, max_row]


class Sensor:
    def __init__(self, sensor_loc, beacon_loc):
        self.sensor_loc = sensor_loc
        self.beacon_loc = beacon_loc

    def print(self):
        print(f"sensor : {self.sensor_loc} nearest beacon : {self.beacon_loc}")


def print_space(s):
    for x in s:
        temp = ""
        for y in x:
            if y:
                temp += "#"
            else:
                temp += "."
        print(temp)


def mark_no_beacons(s, check_row, obj):
    check_row_count = set()
    for sensor in s:
        # print(f"tackling sensor {sensor.print()}")
        r = abs(sensor.sensor_loc[0] - sensor.beacon_loc[0])
        c = abs(sensor.sensor_loc[1] - sensor.beacon_loc[1])
        distance = r + c

        max_row = distance + sensor.sensor_loc[0]
        min_row = distance - sensor.sensor_loc[0]
        if check_row in range(sensor.sensor_loc[0], max_row + 1):
            # calc hits
            check_row_dist = check_row - sensor.sensor_loc[0]
            if [check_row, sensor.sensor_loc[1]] not in obj:
                check_row_count.add(f"{check_row}, {sensor.sensor_loc[1]}")
            for a in range(1, (distance - check_row_dist) + 1):
                if [check_row, sensor.sensor_loc[1] + a] not in obj:
                    check_row_count.add(f"{check_row}, {sensor.sensor_loc[1] + a}")
                if [check_row, sensor.sensor_loc[1] - a] not in obj:
                    check_row_count.add(f"{check_row}, {sensor.sensor_loc[1] - a}")

        elif check_row in range(sensor.sensor_loc[0], min_row - 1, -1):
            # calc hits
            check_row_dist = sensor.sensor_loc[0] - check_row
            if [check_row, sensor.sensor_loc[1]] not in obj:
                check_row_count.add(f"{check_row}, {sensor.sensor_loc[1]}")
            for a in range(1, (distance - check_row_dist) + 1):
                if [check_row, sensor.sensor_loc[1] + a] not in obj:
                    check_row_count.add(f"{check_row}, {sensor.sensor_loc[1] + a}")
                if [check_row, sensor.sensor_loc[1] - a] not in obj:
                    check_row_count.add(f"{check_row}, {sensor.sensor_loc[1] - a}")

    return len(check_row_count)


def sensor_ranges(s_list, limit):
    sensor_coverage_dict = {i: set() for i in range(0, limit + 1)}
    for sen in s_list:
        print("trying next sensor...")
        r = abs(sen.sensor_loc[0] - sen.beacon_loc[0])
        c = abs(sen.sensor_loc[1] - sen.beacon_loc[1])
        sensor_range = r + c
        # structure created below is [row, [col, col]]
        for i in range(0, sensor_range + 1):
            left_col = sen.sensor_loc[1] - (sensor_range - i)
            right_col = sen.sensor_loc[1] + (sensor_range - i)
            if left_col < 0:
                left_col = 0
            elif left_col > limit:
                left_col = limit

            if right_col < 0:
                right_col = 0
            elif right_col > limit:
                right_col = limit

            if sen.sensor_loc[0] - i >= 0:
                sensor_coverage_dict[sen.sensor_loc[0] - i].add(f"{left_col},{right_col}")
            if sen.sensor_loc[0] + i < limit:
                sensor_coverage_dict[sen.sensor_loc[0] + i].add(f"{left_col},{right_col}")

    return sensor_coverage_dict


def sensor_ranges_2(s_list, limit):
    sensor_coverage_dict = sensor_coverage_dict = {i: [] for i in range(0, limit + 1)}
    for sen in s_list:
        print("trying next sensor...")
        r = abs(sen.sensor_loc[0] - sen.beacon_loc[0])
        c = abs(sen.sensor_loc[1] - sen.beacon_loc[1])
        sensor_range = r + c
        # structure created below is [row, [col, col]]
        for i in range(0, sensor_range + 1):
            left_col = sen.sensor_loc[1] - (sensor_range - i)
            right_col = sen.sensor_loc[1] + (sensor_range - i)
            if left_col < 0:
                left_col = 0
            elif left_col > limit:
                left_col = limit

            if right_col < 0:
                right_col = 0
            elif right_col > limit:
                right_col = limit

            if sen.sensor_loc[0] - i >= 0:
                check_ranges(sensor_coverage_dict, [left_col, right_col], sen.sensor_loc[0] - i)

            if sen.sensor_loc[0] + i < limit:
                check_ranges(sensor_coverage_dict, [left_col, right_col], sen.sensor_loc[0] + i)

    return sensor_coverage_dict


def check_ranges(cover, r, index):
    if len(cover[index]) == 0:
        cover[index].append(r)
        return

    need_to_add = True
    for idx, x in enumerate(cover[index]):
        if x[0] <= r[0] and x[1] >= r[1]:
            need_to_add = False
            break
        elif x[0] > r[0] and x[1] >= r[1]:
            cover[index][idx] = [r[0], x[1]]
            need_to_add = False
            break
        elif x[0] <= r[0] and x[1] >= r[0] and x[1] < r[1]:
            cover[index][idx] = [x[0], r[1]]
            need_to_add = False
            break
        elif x[1] == r[0]:
            cover[index][idx] = [x[0], r[1]]
            need_to_add = False
            break
        elif x[0] == r[1]:
            cover[index][idx] = [r[0], x[1]]
            need_to_add = False
            break

    if need_to_add:
        cover[index].append(r)


if __name__ == "__main__":
    results = load_data("data_15", False, 0)
    # results = load_data("test_data_15", False, 0)
    sensors = results[0]

    obj_list = []
    for sensor in sensors:
        obj_list.append(sensor.sensor_loc)
        obj_list.append(sensor.beacon_loc)

    print("Start part 1")
    count = mark_no_beacons(sensors, 2000000, obj_list)
    # count = mark_no_beacons(sensors, 10, obj_list)
    print(f"Part 1 result {count}")

    print("trying part 2")
    part_2_limit = 4000000
    # part_2_limit = 20
    # coverage = sensor_ranges(sensors, part_2_limit)
    coverage = sensor_ranges_2(sensors, part_2_limit)
    print("completed coverage")

    for c in coverage:
        coverage[c].sort()

    # try merging ranges
    kill = False
    final_row = 0
    final_col = 0
    for c in coverage:
        if len(coverage[c]) == 1:  # dangerous assumption, maybe?
            # full range continue on
            continue
        else:
            temp_range = coverage[c][0]
            index = 0
            while index + 1 < len(coverage[c]):
                if coverage[c][index + 1][0] in range(temp_range[0], temp_range[1]):
                    if coverage[c][index + 1][1] in range(temp_range[0], temp_range[1]):
                        temp_range = temp_range
                    elif coverage[c][index + 1][1] > temp_range[1]:
                        temp_range = [temp_range[0], coverage[c][index + 1][1]]
                elif coverage[c][index + 1][0] == temp_range[1] + 1 or coverage[c][index + 1][0] == temp_range[1]:
                    temp_range = [temp_range[0], coverage[c][index + 1][1]]
                else:
                    # chain is broken return
                    kill = True
                    print(f"found broken link at {c} {temp_range[1]}, {coverage[c][index + 1][0]}")
                    final_row = c
                    final_col = temp_range[1] + 1
                    break
                index += 1

        if kill:
            break

    print(f"Part 2 answer = {(final_col * part_2_limit) + final_row}")
