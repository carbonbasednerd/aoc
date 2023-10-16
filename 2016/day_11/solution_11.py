import itertools
import copy
from collections import Counter


def load_data(file):
    output = []
    data = open(file, 'r')
    for line in data:
        parsed = list(map(lambda x: replace_chars(x), filter(lambda x: x not in ("a", "and"), line.strip().split(" "))))
        if parsed[4] == "nothing":
            output.append([])
        else:
            counter = 4
            floor_list = []
            while counter < len(parsed):
                floor_list.append([parsed[counter], parsed[counter + 1]])
                counter += 2
            output.append(floor_list)

    data.close()
    return output


def replace_chars(x):
    z = x.replace(".", "")
    z = z.replace(",", "")
    return z


def generate_states(parent_state):
    floors_to_check = []
    if parent_state[0] == 0:
        floors_to_check.append(1)
    elif parent_state[0] == 3:
        floors_to_check.append(2)
    else:
        floors_to_check.append(parent_state[0] + 1)
        floors_to_check.append(parent_state[0] - 1)

    next_states = []
    current_floor = parent_state[0]
    for floor in floors_to_check:
        combos = list(itertools.chain.from_iterable(itertools.combinations(parent_state[1][current_floor], i) for i in range(1, 3)))
        for components in combos:
            new_state = copy.deepcopy(parent_state)
            new_state[0] = floor
            for component in components:
                new_state[1][floor].append(component)
                new_state[1][floor].sort()
                new_state[1][current_floor].remove(component)

            if check_for_goal(new_state):
                return [], True

            if check_if_safe_simplified(new_state[1]):
                next_states.append(new_state)

    return next_states, False


def check_for_goal(potential_goal):
    return potential_goal[0] == 3 and len(potential_goal[1][0]) == 0 and len(potential_goal[1][1]) == 0 and len(potential_goal[1][2]) == 0


def check_if_safe_simplified(check_state):
    for floor in check_state:
        generators = []
        chips = []
        for component in floor:
            if component[1] == "generator":
                generators.append(component)
            else:
                chips.append(component)

        if generators and chips:
            for chip in chips:
                chip_type = chip[0].split("-")[0]
                if chip_type not in (map(lambda x: x[0], generators)):
                    return False
    return True


def count_floor_objects(state):
    return state[0], tuple(tuple(Counter(type for _, type in floor).most_common()) for floor in state[1])


def main(start_state):
    solving = True
    states = [[0, initial_state]]
    moves = 0
    seen = set()

    while solving:
        new_states = []
        for state in states:
            queued_states, solved = generate_states(state)
            if solved:
                solving = False
                break

            for queue in queued_states:
                if (key := count_floor_objects(queue)) not in seen:
                    seen.add(key)
                    new_states.append(queue)

        states = new_states
        moves += 1

    return moves


if __name__ == "__main__":
    initial_state = load_data("data_11")
    print(f"part 1 optimal solution is {main(initial_state)}")

    initial_state = load_data("data_2_11")
    print(f"part 2 optimal solution is {main(initial_state)}")

