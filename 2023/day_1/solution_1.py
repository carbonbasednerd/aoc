import re

def load_data(file):
    data = open(file, 'r')
    total = 0
    count = 1
    for line in data:
        print(f"line {count}")
        count += 1
        number = ""
        stripped_line = line.strip()
        for x in range(0, len(stripped_line)):
            if stripped_line[x].isnumeric():
                number += stripped_line[x]
                break

        for y in range(len(stripped_line)-1, -1, -1):
            if stripped_line[y].isnumeric():
                number += stripped_line[y]
                break

        total += int(number)
    data.close()
    return total

def load_data_2(file):
    number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    data = open(file, 'r')
    total = 0
    for line in data:
        number = ""
        stripped_line = line.strip()
        left_line = ""
        right_line = ""
        for x in range(0, len(stripped_line)):
            if stripped_line[x].isnumeric():
                left_line = stripped_line[0:x+1]
                break

        for y in range(len(stripped_line)-1, -1, -1):
            if stripped_line[y].isnumeric():
                right_line = stripped_line[y:len(stripped_line)]
                break

        if len(left_line) > 0 and len(left_line) < 3:
            number += left_line[-1]
        else:
            if len(left_line) == 0:
                left_line = stripped_line
            found_number = [10000000, "zero"]
            for entry in number_text:
                location = 10000000
                for match in re.finditer(entry, left_line):
                    location = min(location, match.start())
                if location < 10000000:
                    if location < found_number[0]:
                        found_number[0] = location
                        found_number[1] = entry
            if found_number[0] != 10000000:
                number += convert_to_number(found_number[1])
            else:
                number += left_line[-1]


        if len(right_line) > 0 and len(right_line) < 3:
            number += right_line[0]
        else:
            if len(right_line) == 0:
                right_line = stripped_line
            found_number = [-1, "zero"]
            for entry in number_text:
                location = -1
                for match in re.finditer(entry, right_line):
                    location = max(location, match.start())
                if location > -1:
                    if location > found_number[0]:
                        found_number[0] = location
                        found_number[1] = entry
            if found_number[0] != -1:
                number += convert_to_number(found_number[1])
            else:
                number += right_line[0]

            if len(number) > 2:
                print("problem?")

        total += int(number)
    data.close()
    return total


def convert_to_number(num_string):
    if num_string == "one":
        return "1"
    elif num_string == "two":
        return "2"
    elif num_string == "three":
        return "3"
    elif num_string == "four":
        return "4"
    elif num_string == "five":
        return "5"
    elif num_string == "six":
        return "6"
    elif num_string == "seven":
        return "7"
    elif num_string == "eight":
        return "8"
    else:
        return "9"

if __name__ == "__main__":
    print(f"total count part one {load_data('data_1')}")
    print(f"total count {load_data_2('data_1')}")

#52837 too low