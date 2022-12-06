def load_data(file):
    output = ""
    data = open(file, 'r')
    for line in data:
        output = line.strip()

    data.close()
    return output


def find_substring(offset):
    index = 0
    for idx, x in enumerate(signal):
        temp = set()
        for y in signal[idx: idx + offset]:
            temp.add(y)

        if len(temp) == offset:
            index = idx + offset
            break
        else:
            temp.clear()
    return index


if __name__ == "__main__":
    signal = load_data("data_6")
    print(f"found at {find_substring(4)}")
    print(f"found at {find_substring(14)}")
