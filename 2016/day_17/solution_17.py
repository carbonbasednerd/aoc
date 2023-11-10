import hashlib


def get_possible_moves(n):
    hashed_path = hashlib.md5(n[2].encode('utf-8')).hexdigest()
    next_moves = []
    # up
    if n[1] > 0 and hashed_path[0] in ("b", "c", "d", "e", "f"):
        next_moves.append([n[0], n[1] - 1, n[2] + "U"])
    # down
    if n[1] < 3 and hashed_path[1] in ("b", "c", "d", "e", "f"):
        next_moves.append([n[0], n[1] + 1, n[2] + "D"])
    # left
    if n[0] > 0 and hashed_path[2] in ("b", "c", "d", "e", "f"):
        next_moves.append([n[0] - 1, n[1], n[2] + "L"])
    # right
    if n[0] < 3 and hashed_path[3] in ("b", "c", "d", "e", "f"):
        next_moves.append([n[0] + 1, n[1], n[2] + "R"])

    return next_moves


if __name__ == "__main__":
    paths = []
    base = "vkjiggvb"
    paths.append([0, 0, base])  # x, y, path
    searching = True
    max_steps = 0
    found_shortest = False
    while searching:
        next_paths = []
        for path in paths:
            if path[0] == 3 and path[1] == 3:
                path = path[2][len(base):]
                if not found_shortest:
                    print(f"shortest path is {path}")
                    found_shortest = True
                max_steps = max(max_steps, len(path))
            else:
                next_paths.extend(get_possible_moves(path))
        if next_paths:
            paths = next_paths
        else:
            searching = False

    print(f"longest path is {max_steps}")