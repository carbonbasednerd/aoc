from itertools import permutations

def load_rules(file):
    rules = {}
    data = open(file, 'r')
    for line in data:
        parsed_line = line.strip().strip('.').split(" ")
        value = int(parsed_line[3])
        if parsed_line[2] == "lose":
            value *= -1

        if parsed_line[0] not in rules.keys():
            rules[parsed_line[0]] = {parsed_line[-1]: value}
        else:
            rules[parsed_line[0]][parsed_line[-1]] = value

    data.close()
    return rules


def calculate_score(seating, number_of_guests, rules):
    seating_score = 0
    for seat in range(0, number_of_guests):
        person = seating[seat]

        if seat == 0:
            left_person = seating[-1]
        else:
            left_person = seating[seat-1]

        if seat == number_of_guests-1:
            right_person = seating[0]
        else:
            right_person = seating[seat+1]

        if person == "Me":
            left_value = 0
            right_value = 0
        else:
            if left_person == "Me":
                left_value = 0
            else:
                left_value = rules[person][left_person]

            if right_person == "Me":
                right_value = 0
            else:
                right_value = rules[person][right_person]

        seating_score += (left_value + right_value)

    return seating_score

class PointValue:
    def __init__(self, name, value):
        self.name = name
        self.value = value


if __name__ == '__main__':
    rules = load_rules("data_13")
    guests = rules.keys()
    number_of_guests = len(rules.keys())
    seating_permutations = permutations(guests, number_of_guests)

    highest_score = 0
    for e in seating_permutations:
        seating_score = calculate_score(list(e), number_of_guests, rules)
        if seating_score > highest_score:
            highest_score = seating_score

    print(highest_score)

    # for part 2
    rules["Me"] = {}
    guests = rules.keys()
    number_of_guests = len(guests)
    seating_permutations = permutations(guests, number_of_guests)

    highest_score = 0
    for e in seating_permutations:
        seating_score = calculate_score(list(e), number_of_guests, rules)
        if seating_score > highest_score:
            highest_score = seating_score

    print(highest_score)


