def load_rules(file):
    rules = {}
    data = open(file, 'r')
    for line in data:
        parsed_line = line.strip().strip('.').split(" ")
        name = parsed_line[0]
        speed = int(parsed_line[3])
        time = int(parsed_line[6])
        rest = int(parsed_line[-2])

        rules[name] = {"speed": speed, "time": time, "rest": rest, "resting": False, "count": 0, "traveled": 0, "points": 0}

    data.close()
    return rules


if __name__ == '__main__':
    rules = load_rules("data_14")

    for x in range(0, 2503):
        lead = []
        distance = 0
        for reindeer in rules:
            rules[reindeer]["count"] = rules[reindeer]["count"] + 1
            if rules[reindeer]["resting"]:
                if rules[reindeer]["count"] == rules[reindeer]["rest"]:
                    rules[reindeer]["count"] = 0
                    rules[reindeer]["resting"] = False
            else:
                if rules[reindeer]["count"] == rules[reindeer]["time"]:
                    rules[reindeer]["count"] = 0
                    rules[reindeer]["resting"] = True
                rules[reindeer]["traveled"] = rules[reindeer]["traveled"] + rules[reindeer]["speed"]
            if rules[reindeer]["traveled"] >= distance:
                if rules[reindeer]["traveled"] == distance:
                    lead.append(reindeer)
                else:
                    lead.clear()
                    lead.append(reindeer)
                    distance = rules[reindeer]["traveled"]

        for r in lead:
            rules[r]["points"] = rules[r]["points"] + 1

    print(rules)
    total = 0
    name = ""
    total_points = 0
    point_name = ""
    for reindeer in rules:
        if rules[reindeer]["traveled"] > total:
            total = rules[reindeer]["traveled"]
            name = reindeer
        if rules[reindeer]["points"] > total_points:
            total_points = rules[reindeer]["points"]
            point_name = reindeer

    print(f"part 1 winnner is {name} with a distance of {total}")
    print(f"part 2 winnner is {point_name} with a point total of {total_points}")
