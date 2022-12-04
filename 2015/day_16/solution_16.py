# I think the solution for this might be to find the entries that don't match. I.e. if there is a value entered
# and it doesn't match the "tape" then it can be ignored. That should be phase one.
# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1

def load_sues(file):
    sues = []
    data = open(file, 'r')
    count = 1
    for line in data:
        stripped_line = line[line.find(":")+2:].strip().replace(":", ",").split(",")
        temp_dict = dict(zip(list(map(lambda x: x.replace(" ", ""), stripped_line[::2])), list(map(lambda x: int(x), stripped_line[1::2]))))
        temp_dict["sue"] = count
        sues.append(temp_dict)
        count += 1

    data.close()
    return sues


if __name__ == "__main__":
    sue_attributes = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    sue_list = load_sues("data_16")
    temp_sues = []
    for sue in sue_list:
        match = True
        for attribute in sue:
            if attribute != "sue" and sue[attribute] != sue_attributes[attribute]:
                match = False
                break
        if match:
            temp_sues.append(sue)
    print(temp_sues)

    temp_sues = []
    for sue in sue_list:
        match = True
        for attribute in sue:
            if attribute != "sue":
                if attribute in ["cats", "trees"]:
                    if sue[attribute] <= sue_attributes[attribute]:
                        match = False
                        break
                elif attribute in ["pomeranians", "goldfish"]:
                    if sue[attribute] >= sue_attributes[attribute]:
                        match = False
                        break
                else:
                    if sue[attribute] != sue_attributes[attribute]:
                        match = False
                        break

        if match:
            temp_sues.append(sue)
    print(temp_sues)

