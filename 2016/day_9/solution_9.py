def decompress(file):
    decompression = 0
    data = open(file, 'r')
    for line in data:
        stripped = line.strip()
        counter = 0
        marker = ""
        reading_compression_marker = False
        while counter < len(stripped):
            if stripped[counter] == "(":
                reading_compression_marker = True
                counter += 1
            elif stripped[counter] == ")" and reading_compression_marker:
                reading_compression_marker = False
                marker_split = marker.split("x")
                decompression += (int(marker_split[0]) * int(marker_split[1]))
                counter += int(marker_split[0]) + 1
                marker = ""
            else:
                if reading_compression_marker:
                    marker += stripped[counter]
                    counter += 1
                else:
                    if stripped[counter] != " ":
                        decompression += 1
                    counter += 1

    data.close()
    return decompression


def read_data(file):
    data = open(file, 'r')
    output = data.read().strip()
    data.close()
    return output


def decompress_nested(data):
    # print(data)
    decompression = 0
    equation = ""
    marker = ""
    reading_compression_marker = False
    skip = 0
    for count, c in enumerate(data):
        if skip > 0:
            skip -= 1
        else:
            if c == "(":
                reading_compression_marker = True
            elif c == ")":
                reading_compression_marker = False
                split = marker.split("x")
                equation += f"{decompress_nested(data[count+1:count+int(split[0])+1]) * int(split[1])}+"
                skip = int(split[0])
                marker = ""

            else:
                if reading_compression_marker:
                    marker += c
                else:
                    equation += "1+"

    # remove extraneous +
    if equation[-1] == "+":
        equation = equation[0:-1]

    # print(f"equation:{equation}")

    decompression = eval(equation)
    return decompression


if __name__ == "__main__":
    print(f"size after decompression:{decompress('data_9')}")

    print(f"size after nested decompression:{decompress_nested(read_data('data_9'))}")
