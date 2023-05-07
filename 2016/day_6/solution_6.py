data_size = 8

def load_data(file):
    output = ""
    data = open(file, 'r')
    frequency_count = [{} for j in range(data_size)]
    for line in data:
        stripped = line.strip()
        for c in range(0, data_size):
            if stripped[c] in frequency_count[c].keys():
                frequency_count[c][stripped[c]] += 1
            else:
                frequency_count[c][stripped[c]] = 1

    for fc in frequency_count:
        sort = sorted(fc.items(), key=lambda x: x[1])
        # sort.reverse()
        print(sort)
        output += sort[0][0]

    data.close()
    return output


if __name__ == "__main__":
    print(load_data("data_6"))
