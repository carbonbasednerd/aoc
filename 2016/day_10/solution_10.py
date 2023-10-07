from collections import defaultdict


def load_data(file):
    bots = defaultdict(Bot)
    outputs = defaultdict(lambda: [])
    data = open(file, 'r')
    for line in data:
        scrubbed = line.strip().split(" ")
        if scrubbed[0] == "bot":
            bid = int(scrubbed[1])
            low_pass = [scrubbed[5], int(scrubbed[6])]
            high_pass = [scrubbed[10], int(scrubbed[11])]
            bots[bid].set_low_and_high_pass(low_pass, high_pass)
        else:
            bid = int(scrubbed[5])
            chip_value = int(scrubbed[1])
            bots[bid].chip_container.append(chip_value)

    data.close()
    return bots, outputs


class Bot:
    def __init__(self, low_pass=-1, high_pass=-1):
        self.low_pass = low_pass
        self.high_pass = high_pass
        self.chip_container = []

    def set_low_and_high_pass(self, low_pass, high_pass):
        self.low_pass = low_pass
        self.high_pass = high_pass
        if len(self.chip_container) == 2:
            self.chip_container.sort()

    def receive_chip(self, chip_value):
        self.chip_container.append(chip_value)
        self.chip_container.sort()

    def distribute_chips(self):
        distribution = [(self.low_pass, self.chip_container[0]), (self.high_pass, self.chip_container[1])]
        self.chip_container.clear()
        return distribution


if __name__ == "__main__":
    bot_list, output_bins = load_data("data_10")
    process_list = set(bot_list.keys())
    # this makes an assumption that every bot distributes a chip once - which works for this case.
    while len(process_list):
        for bot_id, bot in bot_list.items():
            if bot_id in process_list and len(bot.chip_container) == 2:
                if bot.chip_container.__contains__(61) and bot.chip_container.__contains__(17):
                    print(f"Solution 1 : {bot_id}")
                result = bot.distribute_chips()
                for to_process in result:
                    if to_process[0][0] == "bot":
                        bot_list[to_process[0][1]].receive_chip(to_process[1])
                    else:
                        output_bins[to_process[0][1]].append(to_process[1])
                process_list.remove(int(bot_id))

    print(f"Solution 2 : {output_bins[2][0] * output_bins[1][0] * output_bins[0][0]}")
