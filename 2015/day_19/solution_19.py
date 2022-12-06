import time
import threading

def load_data(file):
    data = open(file, 'r')
    flag = True
    output_string = ""
    transforms = []
    for line in data:
        stripped = line.strip()
        if stripped == "":
            flag = False

        if flag:
            split_data = stripped.split(" ")
            transforms.append([split_data[0], split_data[2]])
        else:
            output_string = stripped
    data.close()
    return [transforms, output_string]


def find_uniques(mol, trans):
    uniques = set()
    for t in trans:
        i = 0
        search = True
        while search:
            m = mol.find(t[0], i)
            if m > -1:
                l = len(t[0])
                uniques.add(mol[0:m]+t[1]+mol[m+l:])
                i = m + 1
            else:
                search = False
    return uniques


def build_molecule(t, e, end, depth):
    terminate = False
    un = find_uniques(e, t)
    # time.sleep(1)
    for u in un:
        if u == end:
            print(f"found {u}")
            terminate = True
        if len(u) > len(end):
            # print(f"too big, {u}")
            continue
        if terminate:
            break
        # print(f"unique {u}")
        terminate = build_molecule(t, u, end, depth + 1)
    print(f"Completed a recursion {depth}")
    return terminate


if __name__ == "__main__":
    results = load_data("data_19")
    transforms = results[0]
    molecule = results[1]

    build_molecule(transforms, "e", molecule, 0)
