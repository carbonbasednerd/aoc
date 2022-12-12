import math


def load_data(file):
    data = open(file, 'r')
    count = -1
    monkeys = []
    monkey = None
    for line in data:
        count += 1
        stripped = line.strip()
        if count == 0:
            monkey = Monkey(stripped[-2])
        elif count == 1:
            split = stripped.replace(",", "").split(" ")
            monkey.add_items(list(map(lambda x: int(x), split[2:])))
        elif count == 2:
            split = stripped.split(" ")
            if split[-1] == "old":
                split[-2] = "s"
                split[-1] = "0"
            monkey.add_op([split[-2], int(split[-1])])
        elif count == 3:
            split = stripped.split(" ")
            monkey.add_test(int(split[-1]))
        elif count == 4:
            split = stripped.split(" ")
            monkey.add_resolve(int(split[-1]))
        elif count == 5:
            split = stripped.split(" ")
            monkey.add_resolve(int(split[-1]))
        else:
            monkeys.append(monkey)
            count = -1

    monkeys.append(monkey)
    data.close()
    return monkeys


class Monkey:

    def __init__(self, name):
        self.name = name
        self.items = []
        self.op = []
        self.test = 0
        self.resolve = []
        self.inspect_count = 0

    def add_items(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def get_item(self):
        return self.items.pop(0)

    def add_op(self, op):
        self.op = op

    def add_test(self, test):
        self.test = test

    def add_resolve(self, resolve):
        self.resolve.append(resolve)

    def modify_worry_level(self, val):
        self.inspect_count += 1
        if self.op[0] == "+":
            return val + self.op[1]
        elif self.op[0] == "*":
            return val * self.op[1]
        else:
            return val * val

    def throw_to(self, val):
        if val % self.test == 0:
            return self.resolve[0]
        else:
            return self.resolve[1]

    def show_stats(self):
        print(f"Monkey {self.name}")
        print(f"  Starting items: {self.items}")
        print(f"  Operation: {self.op}")
        print(f"  Test mod : {self.test}")
        print(f"     True, throw to : {self.resolve[0]}")
        print(f"     False, throw to : {self.resolve[1]}")
        print(f"")


def play_round(m_list, flag):

    for m in m_list:
        while len(m.items) != 0:
            worry = m.modify_worry_level(m.get_item())
            if flag:
                worry = math.floor(worry / 3)
            else:
                worry = worry % 9699690
                # worry = worry % 96577

            new_monkey = m.throw_to(worry)
            m_list[new_monkey].add_item(worry)


if __name__ == "__main__":
    monkey_list = load_data("data_11")

    for i in range(1, 10001):
        play_round(monkey_list, False)

    inspect_counts = []
    for mnk in monkey_list:
        inspect_counts.append(mnk.inspect_count)

    inspect_counts.sort()
    print(inspect_counts)
    print(f"Monkey inspect count answer is {inspect_counts[-1] * inspect_counts[-2]}")
