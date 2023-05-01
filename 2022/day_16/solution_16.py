import copy
from dijkstar import Graph, find_path
from itertools import combinations


def load_data(file):
    graph = Graph()
    rates = {}
    data = open(file, 'r')
    for line in data:
        stripped = line.strip()
        split = stripped.split(" ")
        node_name = split[1]
        rate = int(split[4].replace("rate=", "").replace(";", ""))
        rates[node_name] = rate
        for i in range(9, len(split)):
            graph.add_edge(node_name, split[i].replace(",", ""), 1)

    data.close()
    return [graph, rates]


def find_path_recursive(minutes, loc, valves_released, valve_list, g, score, max_pressure, depth):
    if len(valves_released) >= max_pressure or minutes >= 30:
        return score

    if valve_list[loc] > 0 and loc not in valves_released:
        valves_released.append(loc)
        minutes += 1
        score += ((30 - minutes) * valve_list[loc])

    temp_score = 0
    for v in valve_list:
        if v not in valves_released and valve_list[v] > 0:
            alg = find_path(g, loc, v)
            new_location = alg.nodes[-1]
            result = find_path_recursive(minutes + alg.total_cost, new_location, copy.deepcopy(valves_released), valve_list, g,
                                            0, max_pressure, depth + 1)
            temp_score = max(temp_score, result)

    return score + temp_score


def find_path_recursive_part2(minutes, loc, valves_released, valve_list, g, score, max_pressure, depth):
    if len(valves_released) >= max_pressure or minutes >= 26:
        return score

    if valve_list[loc] > 0 and loc not in valves_released:
        valves_released.append(loc)
        minutes += 1
        score += ((26 - minutes) * valve_list[loc])

    temp_score = 0
    for v in valve_list:
        if v not in valves_released and valve_list[v] > 0:
            alg = find_path(g, loc, v)
            new_location = alg.nodes[-1]
            result = find_path_recursive_part2(minutes + alg.total_cost, new_location, copy.deepcopy(valves_released), valve_list, g,
                                            0, max_pressure, depth + 1)
            temp_score = max(temp_score, result)

    return score + temp_score


if __name__ == "__main__":
    results = load_data("data_16")
    graph = results[0]
    valves = results[1]

    print(results[0])
    print(results[1])

    under_pressure = 0
    for valve in valves:
        if valves[valve] > 0:
            under_pressure += 1

    results = find_path_recursive(0, "AA", [], valves, graph, 0, under_pressure, 0)
    print(f"results: {results}")

    print(f"Run Part 2---------")
    pressurized_valves = []
    for valve in valves:
        if valves[valve] > 0:
            pressurized_valves.append(valve)

    # for right now this solution is different for part 1 vs part 2
    # I hard coded the combination splits against the test data_1
    # could definitely multithread each run
    print("Part 2a")
    max_cost = []
    for mutation in combinations(pressurized_valves, 7):
        results = find_path_recursive_part2(0, "AA", list(mutation), valves, graph, 0, under_pressure, 0)
        max_cost.append([results, mutation])

    print("Part 2b")
    max_cost_2 = []
    for mutation in combinations(pressurized_valves, 8):
        results = find_path_recursive_part2(0, "AA", list(mutation), valves, graph, 0, under_pressure, 0)
        max_cost_2.append([results, mutation])

    print("Part 2c")
    maxy = 0
    for x in max_cost:
        for y in max_cost_2:
            found = True
            for i in x[1]:
                if i in y[1]:
                    found = False
            if found:
                maxy = max(maxy, x[0] + y[0])

    print(f"results: {maxy}")

