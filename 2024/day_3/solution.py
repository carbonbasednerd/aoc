import re

#prep data to get rid of \n
def load_data(file):
    data = open(file, 'r')
    total_part_one = 0
    total_part_two = 0
    for line in data:
        print("oince")
        stripped_line = line.strip()
        can_multiply = True        
        for commands in re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', stripped_line):
            if commands == "do()":
                can_multiply = True
            elif commands == "don't()":
                can_multiply = False
            else:
                numbers = re.findall(r'\d{1,3},\d{1,3}', commands)[0].split(",")
                result = int(numbers[0]) * int(numbers[1])
                total_part_one += result
                if can_multiply:
                    total_part_two += result                
    data.close()
    return total_part_one, total_part_two

if __name__ == "__main__":
    result_one, result_two = load_data("/Users/jasonraffi/git/aoc/2024/day_3/data")
    print(f"Part one: {result_one} Part two: {result_two}")