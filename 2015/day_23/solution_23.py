
def load_data(file):
    data = open(file, 'r')
    result = []
    for line in data:
        stripped = line.strip()
        split_data = stripped.split(" ")
        split_data[1] = split_data[1].replace(",", "")
        result.append(split_data)

    data.close()
    return result

if __name__ == "__main__":
    instruction_set = load_data("data_23")
    print(instruction_set)
    processing = True
    set_length = len(instruction_set)
    counter = 0
    a_register = 1
    b_register = 0

    while processing:
        if counter not in range(0, set_length):
            processing = False
        else:
            line = instruction_set[counter]
            instruction = line[0]
            if instruction == "hlf":
                print("hlf")
                if line[1] == "a":
                    a_register = a_register / 2
                else:
                    b_register = b_register / 2
                counter += 1

            elif instruction == "tpl":
                print("tpl")
                if line[1] == "a":
                    a_register = a_register * 3
                else:
                    b_register = b_register * 3
                counter += 1

            elif instruction == "inc":
                print("inc")
                if line[1] == "a":
                    a_register += 1
                else:
                    b_register += 1
                counter += 1

            elif instruction == "jmp":
                print("jmp")
                if line[1].find("+") == 0:
                    value = line[1].replace("+", "")
                    counter += int(value)
                else:
                    value = line[1].replace("-", "")
                    counter -= int(value)

            elif instruction == "jie":
                print("jie")
                if line[1] == "a":
                    if a_register % 2 == 0:
                        if line[2].find("+") == 0:
                            value = line[2].replace("+", "")
                            counter += int(value)
                        else:
                            value = line[2].replace("-", "")
                            counter -= int(value)
                    else:
                        counter += 1
                else:
                    if b_register % 2 == 0:
                        if line[2].find("+") == 0:
                            value = line[2].replace("+", "")
                            counter += int(value)
                        else:
                            value = line[2].replace("-", "")
                            counter -= int(value)
                    else:
                        counter += 1

            elif instruction == "jio":
                print("jio")
                if line[1] == "a":
                    if a_register == 1:
                        if line[2].find("+") == 0:
                            value = line[2].replace("+", "")
                            counter += int(value)
                        else:
                            value = line[2].replace("-", "")
                            counter -= int(value)
                    else:
                        counter += 1
                else:
                    if b_register == 1:
                        if line[2].find("+") == 0:
                            value = line[2].replace("+", "")
                            counter += int(value)
                        else:
                            value = line[2].replace("-", "")
                            counter -= int(value)
                    else:
                        counter += 1
            else:
                processing = False

    print(f"a register: {a_register}")
    print(f"b register: {b_register}")
