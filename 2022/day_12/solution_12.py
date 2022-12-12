from dijkstar import Graph, find_path

def load_data(file):
    output = []
    start_index = []
    end_index = []
    data = open(file, 'r')
    all_a = []
    for row, line in enumerate(data):
        temp = []
        for col, c in enumerate(line.strip()):
            if c == "S":
                start_index = [row, col]
                temp.append(ord("a"))
                all_a.append((row, col))
            elif c == "E":
                end_index = [row, col]
                temp.append(ord("z"))
            else:
                if c == "a":
                    all_a.append((row, col))
                temp.append(ord(c))
        output.append(temp)

    data.close()
    return [output, start_index, end_index, all_a]


def build_graph(space):
    col_size = len(space[0])-1
    row_size = len(space)-1
    graph = Graph()
    count = 0
    for i in range(0, row_size+1):
        for j in range(0, col_size+1):
            # check top
            if i != 0 and (space[i][j] >= space[i-1][j] or space[i-1][j] - space[i][j] <= 1):
                graph.add_edge((i, j), (i-1, j), 1)
            # check bottom
            if i < row_size and (space[i][j] >= space[i+1][j] or space[i+1][j] - space[i][j] <= 1):
                graph.add_edge((i, j), (i+1, j), 1)
            # check left
            if j != 0 and (space[i][j] >= space[i][j-1] or space[i][j-1] - space[i][j] <= 1):
                graph.add_edge((i, j), (i, j-1), 1)
            # check right
            if j < col_size and (space[i][j] >= space[i][j+1] or space[i][j+1] - space[i][j] <= 1):
                graph.add_edge((i, j), (i, j + 1), 1)
            count += 1
    return graph


if __name__ == "__main__":
    result = load_data("data_12")
    g = build_graph(result[0])
    alg = find_path(g, (result[1][0], result[1][1]), (result[2][0], result[2][1]))
    print(f"shortest path = {alg.total_cost}")

    costs = []
    count_failed = 0
    for possible in result[3]:
        try:
            a = find_path(g, possible, (result[2][0], result[2][1]))
            costs.append(a.total_cost)
        except Exception:
            count_failed += 1

    costs.sort()
    print(f"Shortest Part 2 =  {costs[0]}")
