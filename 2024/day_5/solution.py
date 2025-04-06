def load_data(file):
    data = open(file, 'r')
    rule_set = {}
    reading_rules = True
    data_set = []
    for line in data:
        stripped_line = line.strip()
        if stripped_line == "":
            reading_rules = False
            continue
        if reading_rules:
            rule = stripped_line.split("|")
            rule_set.setdefault(int(rule[0]), [])
            rule_set[int(rule[0])].append(int(rule[1]))
        else:
            data_set.append(list(map(int, stripped_line.split(","))))
               
    data.close()
    return data_set, rule_set

# make sure to pass the enumerated set of instructions
def fix_instruction_set(broken_instruction):
    instruction_set = {}
    new_instruction = broken_instruction
    for index, x in enumerate(broken_instruction):
        instruction_set[x] = index
    for index, x in enumerate(broken_instruction):
        constraints = rules.get(x)
        if constraints == None:
            continue
        for constraint in constraints:
            if instruction_set.get(constraint) != None and instruction_set.get(constraint) < index:
                # swap the two constraints locations and recheck
                new_instruction[instruction_set.get(constraint)] = x
                new_instruction[index] = constraint
                return fix_instruction_set(new_instruction)
    return new_instruction


if __name__ == "__main__":
    data, rules = load_data("/Users/jasonraffi/git/aoc/2024/day_5/data")
    print(rules)
    total_middle_pages = 0
    failed_instructions = []
    for instruction in data:
        #build dictionary of instructions
        instruction_set = {}
        for index, x in enumerate(instruction):
            instruction_set[x] = index
        failed_instruction = False
        for index, x in enumerate(instruction):
            constraints = rules.get(x)
            valid_instruction = True
            if constraints == None:
                continue
            for constraint in constraints:
                if instruction_set.get(constraint) != None and instruction_set.get(constraint) < index:
                    valid_instruction = False
                    failed_instructions.append(instruction)
                    break
            if not valid_instruction:
                failed_instruction = True
                break
        if not failed_instruction:
            # find the middle page and add to total
            middle_index = int((len(instruction) - 1)/2)
            total_middle_pages += instruction[middle_index]
    print(f"Total of middle page values{total_middle_pages}")

    print(f"Failed instructions: {failed_instructions}")
    for failed_instruction in failed_instructions:
        fail_count = 0
        instruction_set = {}
        for index, x in enumerate(failed_instruction):
            instruction_set[x] = index

        for index, x in enumerate(failed_instruction):
            constraints = rules.get(x)
            if constraints == None:
                continue
            for constraint in constraints:
                if instruction_set.get(constraint) != None and instruction_set.get(constraint) < index:
                    print(f"x {x} constraint {constraint}")
                    fail_count += 1
        
        print(f"Failed instruction: {failed_instruction} failed count: {fail_count}")

    total_middle_pages_2 = 0
    for failed_instruction in failed_instructions:
        fixed_instruction = fix_instruction_set(failed_instruction)
        print(f"fixed {fixed_instruction}")
        middle_index = int((len(fixed_instruction) - 1)/2)
        total_middle_pages_2 += fixed_instruction[middle_index]
    print(f"Total of middle page values part 2 {total_middle_pages_2}")
            
        
        

