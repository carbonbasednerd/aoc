def load_data(file):
    output = 0
    data = open(file, 'r')
    for line in data:
        stripped = line.strip()
        match_checksum = False
        alphas = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0,
                  "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0,
                  "w": 0, "x": 0, "y": 0, "z": 0}
        checksum = ""
        sector = ""
        door_name = ""
        for character in stripped:
            if match_checksum:
                if character == "]":
                    break
                else:
                    checksum = f"{checksum}{character}"
            else:
                if character == "[":
                    match_checksum = True
                elif character.isalpha():
                    alphas[character] += 1
                    door_name += character
                elif character.isdigit():
                    sector = f"{sector}{character}"
                else:
                    door_name += character


        sort = sorted(alphas.items(), key=lambda x:x[1])
        sort.reverse()
        found_total = sort[0][1] + sort[1][1] + sort[2][1] + sort[3][1] + sort[4][1]
        checksum_total = alphas[checksum[0]] + alphas[checksum[1]] + alphas[checksum[2]] + alphas[checksum[3]] + alphas[checksum[4]]

        if found_total == checksum_total:
            output += int(sector)
            shift_value = int(sector) % 26
            decoded_door = ""
            for door_char in door_name:
                if door_char == "-":
                    decoded_door += " "
                else:
                    decoded_door += chr(get_shifted_alpha(ord(door_char), shift_value))
            print(f"decoded door name:{decoded_door} : sector:{sector}")

    data.close()
    return output


def get_shifted_alpha(ascii_value, shift):
    new_val = ascii_value + shift
    if (new_val > 122):
        new_val = 97 + new_val - 123
    return new_val


if __name__ == "__main__":
    print(f"Valid door:{load_data('data_4')}")
