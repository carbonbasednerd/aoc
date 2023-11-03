from math import sqrt
import copy

# returns 0 if a space, 1 otherwise
def is_a_wall(p):
    # key = 10  # test key
    key = 1362
    base = (p[1] * p[1]) + (3 * p[1]) + (2 * p[1] * p[0]) + p[0] + (p[0] * p[0]) + key
    return len(list(filter(lambda x: x == '1', bin(base)))) % 2


def get_valid_paths(point, v):
    valid_paths = []
    # top
    if point[0] != 0:
        top = (point[0]-1, point[1])
        if top not in v and not is_a_wall(top):
            valid_paths.append(top)
    # Left
    if point[1] != 0:
        left = (point[0], point[1]-1)
        if left not in v and not is_a_wall(left):
            valid_paths.append(left)
    # Right
    right = (point[0], point[1]+1)
    if right not in v and not is_a_wall(right):
        valid_paths.append(right)
    # Bottom
    bottom = (point[0]+1, point[1])
    if bottom not in v and not is_a_wall(bottom):
        valid_paths.append(bottom)

    return valid_paths


if __name__ == "__main__":
    searching = True
    goal = (39, 31)
    # goal = (4, 7)
    start = (1, 1)
    visited = set()
    visited.add(start)
    count = 0
    queue = []
    queue.extend(get_valid_paths(start, visited))
    final = (-1, -1)
    while searching:
        next_queue = []
        while queue:
            node = queue.pop()
            if node == goal:
                searching = False
                final = node
                break
            else:
                visited.add(node)
                next_queue.extend(get_valid_paths(node, visited))
        count += 1
        print(f"count {count} searching {searching} queue count: {len(visited)}")
        queue.extend(next_queue)

    print(f"Goal {final} in {count} moves")

