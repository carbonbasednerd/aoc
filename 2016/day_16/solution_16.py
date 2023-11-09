def dragonize(i):
    flipped_string = ""
    for x in i[::-1]:
        if x == "1":
            flipped_string += "0"
        else:
            flipped_string += "1"

    return f"{i}0{flipped_string}"


def calculate_checksum(i):
    checksum = ""
    for y in range(0, len(i), 2):
        if i[y:y+2] == "11" or i[y:y+2] == "00":
            checksum += "1"
        else:
            checksum += "0"
    return checksum


if __name__ == "__main__":
    # base_input = "10000"
    base_input = "01000100010010111"
    # disk_size = 20
    # disk_size = 272
    disk_size = 35651584
    while len(base_input) < disk_size:
        base_input = dragonize(base_input)

    if len(base_input) > disk_size:
        base_input = base_input[0:disk_size]

    base_input = calculate_checksum(base_input)
    while len(base_input) % 2 == 0:
        base_input = calculate_checksum(base_input)

    print(f"checksum: {base_input}")
