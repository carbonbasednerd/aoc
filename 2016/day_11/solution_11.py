import itertools
import copy


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
        floors_to_check.append(parent_state[0] - 1)
        floors_to_check.append(parent_state[0] + 1)

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

            if not check_for_prior_state(new_state, old_states) and check_if_safe_simplified(new_state[1][floor]):
                next_states.append(new_state)

    return next_states, False


def check_for_goal(potential_goal):
    return potential_goal[0] == 3 and len(potential_goal[1][0]) == 0 and len(potential_goal[1][1]) == 0 and len(potential_goal[1][2]) == 0


def state_not_previously_done(new_state, old_states):
    for old in old_states:
        if old[1][0] == new_state[1][0] and old[1][1] == new_state[1][1] and old[1][2] == new_state[1][2] and old[1][3] == new_state[1][3]:
            return False
    return True


def check_for_prior_state(new_state, old_states):
    hashed = hash_a_state(new_state)
    for old_state in old_states:
        if hashed[0] == old_state[0] and hashed[1] == old_state[1] and hashed[2] == old_state[2] and hashed[3] == old_state[3]:
            return True
    return False


def hash_a_state(state_to_hash):
    hashed_state = []
    for i in range(0, 4):
        flattened = list(itertools.chain.from_iterable(state_to_hash[1][i]))
        stringed = ''.join(flattened).replace(" ", "")
        hashed_state.append(hash(stringed))
    return hashed_state


def check_if_safe_simplified(floor):
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


if __name__ == "__main__":
    initial_state = load_data("data_11")
    solving = True
    prior_state = copy.deepcopy(initial_state)
    states = [[0, initial_state]]
    prior_states = []
    moves = 0
    while solving:
        print(f"moves: {moves}")
        new_states = []
        rejected_states = []
        checked_states = []
        for state in states:
            queued_states, solved = generate_states(state, prior_states)
            if solved:
                solving = False
                break
            checked_states.append(hash_a_state(state))
            new_states.extend(queued_states)

        prior_states = copy.deepcopy(checked_states)
        states = copy.deepcopy(new_states)
        moves += 1
        print(f"new states {len(new_states)}")
        if not solving:
            print(f"Found solution after {moves} moves")


# todo: hash the prior states and keep them in a list for quicker look up. from itertools import chain, list(chain.from_iterable(y)), hash(), .join()
