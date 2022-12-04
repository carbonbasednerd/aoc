def load_data(file):
    data = open(file, 'r')
    bags = []
    for line in data:
        bags.append(line.strip())

    data.close()
    return bags


if __name__ == "__main__":
    result = load_data("data_3")
    print(result)
    priority_points = 0
    badge_points = 0
    group = []
    for r in result:
        midpoint = int(len(r) / 2)
        first_pocket = r[0:midpoint]
        second_pocket = r[midpoint:]

        for c in first_pocket:
            if c in second_pocket:
                if c.islower():
                    priority_points += (ord(c) - 96)
                else:
                    priority_points += (ord(c) - 38)
                break

        if len(group) < 2:
            group.append(r)
        else:
            group.append(r)
            matches = set()
            for e in group[0]:
                if e in group[1] and e in group[2]:
                    matches.add(e)

            for m in matches:
                if m.islower():
                    badge_points += (ord(m) - 96)
                else:
                    badge_points += (ord(m) - 38)

            group.clear()

    print(f"Total priority points {priority_points} total badge points {badge_points}")