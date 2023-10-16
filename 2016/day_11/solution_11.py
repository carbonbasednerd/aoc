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


def generate_states(parent_state, old_states):
    floors_to_check = []
    if parent_state[0] == 0:
        floors_to_check.append(1)
    elif parent_state[0] == 3:
        floors_to_check.append(2)
    else:
        floors_to_check.append(parent_state[0] + 1)
        floors_to_check.append(parent_state[0] - 1)
    # elif parent_state[0] == 1:
    #     floors_to_check.append(parent_state[0] + 1)
    #     if parent_state[1][0]:
    #         floors_to_check.append(parent_state[0] - 1)
    # else:
    #     floors_to_check.append(parent_state[0] + 1)
    #     if parent_state[1][0] and parent_state[1][1]:
    #         floors_to_check.append(parent_state[0] - 1)

    next_states = []
    failed_states = []
    current_floor = parent_state[0]
    for floor in floors_to_check:
        combos = list(itertools.chain.from_iterable(itertools.combinations(parent_state[1][current_floor], i) for i in range(1, 3)))
        for components in combos:
            new_state = copy.deepcopy(parent_state)
            new_state[0] = floor
            new_state[3] = copy.deepcopy(parent_state[1])
            for component in components:
                new_state[1][floor].append(component)
                new_state[1][floor].sort()
                new_state[1][current_floor].remove(component)

            if check_for_goal(new_state):
                return [], True, []

            if check_if_safe_simplified(new_state[1]):
                # if check_distance(new_state[1]) > parent_state[2] - 1 and not check_priors(new_state, old_states):
                # if not check_local_priors(new_state):
                next_states.append(new_state)
            else:
                failed_states.append(new_state)

            # if not check_local_priors(new_state):
            #     if check_if_safe_simplified(new_state[1]):
            #         if check_for_goal(new_state):
            #             return [], True, []
            #
            #         new_state[2] = check_distance(new_state[1])
            #         if new_state[2] >= parent_state[2] - 1:
            #             next_states.append(new_state)
            #         else:
            #             failed_states.append(new_state)
            #     else:
            #         failed_states.append(new_state)

    return next_states, False, failed_states


def check_distance(s):
    return (1 * len(s[0])) + (2 * len(s[1])) + (3 * len(s[2])) + (4 * len(s[3]))


def check_for_goal(potential_goal):
    return potential_goal[0] == 3 and len(potential_goal[1][0]) == 0 and len(potential_goal[1][1]) == 0 and len(potential_goal[1][2]) == 0


def check_local_priors(new_state):
    if new_state[3]:
        if new_state[3][0] == new_state[1][0] and new_state[3][1] == new_state[1][1] and new_state[3][2] == new_state[1][2] and\
                new_state[3][3] == new_state[1][3]:
            return True
    return False


def check_priors(new_state, old_states):
    if old_states[new_state[0]]:
        for old_state in old_states.get(new_state[0]):
            if old_state[1][0] == new_state[1][0] and old_state[1][1] == new_state[1][1] and old_state[1][2] == new_state[1][2] and old_state[1][3] == new_state[1][3]:
                return True
    return False


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


if __name__ == "__main__":
    initial_state = load_data("data_11")
    solving = True
    states = [[0, initial_state, check_distance(initial_state), []]]
    prior_states = {0: [], 1: [], 2: [], 3: []}
    moves = 0
    seen = set()

    while solving:
        print(f"moves: {moves}")
        new_states = []
        for state in states:
            queued_states, solved, failed = generate_states(state, prior_states)
            if solved:
                solving = False
                break

            for queue in queued_states:
                if (key := count_floor_objects(queue)) not in seen:
                    seen.add(key)
                    new_states.append(queue)

            # prior_states[state[0]].append(state)
            # for fail in failed:
            #     prior_states[fail[0]].append(fail)
            # new_states.extend(queued_states)

        states = new_states
        moves += 1
        print(f"new states {len(new_states)}")
        if not solving:
            print(f"Found solution after {moves} moves")
