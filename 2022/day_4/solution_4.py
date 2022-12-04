def load_data(file):
    data = open(file, 'r')
    sections = []
    for line in data:
        stripped_line = line.strip().split(",")
        temp_section = []
        for section in stripped_line:
            range = section.split("-")
            temp_section.append(int(range[0]))
            temp_section.append(int(range[1]))
        sections.append(temp_section)

    data.close()
    return sections


if __name__ == "__main__":
    result = load_data("data_4")

    full_overlapping_count = 0
    partial_overlapping_count = 0
    for entry in result:
        if all(e in range(entry[0], entry[1]+1) for e in range(entry[2], entry[3]+1)): # not ranges are not inclusive at max
            full_overlapping_count += 1
        elif all(e in range(entry[2], entry[3]+1) for e in range(entry[0], entry[1]+1)):
            full_overlapping_count += 1

        if entry[0] in range(entry[2], entry[3]+1):
            partial_overlapping_count += 1
        elif entry[1] in range(entry[2], entry[3]+1):
            partial_overlapping_count += 1
        elif entry[2] in range(entry[0], entry[1]+1):
            partial_overlapping_count += 1
        elif entry[3] in range(entry[0], entry[1]+1):
            partial_overlapping_count += 1

    print(f"full overlapping = {full_overlapping_count} partial overlapping = {partial_overlapping_count}")
