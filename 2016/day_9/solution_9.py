
def read_data(file):
    data = open(file, 'r')
    output = data.read().strip()
    data.close()
    return output


def decompress_nested(data, allow_nesting):
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
                if allow_nesting:
                    equation += f"{decompress_nested(data[count+1:count+int(split[0])+1], allow_nesting) * int(split[1])}+"
                else:
                    equation += f"{int(split[0])*int(split[1])}+"
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

    return eval(equation)


if __name__ == "__main__":
    print(f"size after decompression:{decompress_nested(read_data('data_9'), False)}")

    print(f"size after nested decompression:{decompress_nested(read_data('data_9'), True)}")
