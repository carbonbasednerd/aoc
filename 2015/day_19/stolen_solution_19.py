from random import shuffle

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


results = load_data('data_19')

reps = results[0]
mol = results[1]

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print(part2)