import unittest


def load_data(file, ts):
    data = open(file, 'r')
    rope_space = RopeSpace(ts)
    for line in data:
        parsed_line = line.strip().split(" ")
        rope_space.move_head(parsed_line[0], int(parsed_line[1]))

    data.close()
    return len(rope_space.tail_count)


class RopeSpace:
    def __init__(self, train_size):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.train_size = train_size
        self.train = [[0, 0] for i in range(train_size)]
        self.tail_count = {"0,0"}
        self.train_tail_count = {"0,0"}

    def move_head(self, v, d):
        for x in range(1, d+1):
            if v == "R":
                self.train[0][1] += 1
            elif v == "L":
                self.train[0][1] -= 1
            elif v == "U":
                self.train[0][0] += 1
            else:
                self.train[0][0] -= 1
            self.process_tail([self.train[0][0], self.train[0][1]])

    def process_tail(self, h):
        for t in range(1, self.train_size):
            x = abs(h[0] - self.train[t][0])
            y = abs(h[1] - self.train[t][1])
            if x > 1 or y > 1:  # adjust tail position
                # +x
                if abs((h[0] + 1) - self.train[t][0]) <= 1 and abs((h[1]) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0] + 1
                    self.train[t][1] = h[1]
            # -x
                elif abs((h[0] - 1) - self.train[t][0]) <= 1 and abs((h[1]) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0] - 1
                    self.train[t][1] = h[1]
            # +y
                elif abs((h[0]) - self.train[t][0]) <= 1 and abs((h[1] + 1) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0]
                    self.train[t][1] = h[1] + 1
            # -y
                elif abs((h[0]) - self.train[t][0]) <= 1 and abs((h[1] - 1) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0]
                    self.train[t][1] = h[1] - 1
            # +x -y
                elif abs((h[0] + 1) - self.train[t][0]) <= 1 and abs((h[1] - 1) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0] + 1
                    self.train[t][1] = h[1] - 1
            # +x +y
                elif abs((h[0] + 1) - self.train[t][0]) <= 1 and abs((h[1] + 1) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0] + 1
                    self.train[t][1] = h[1] + 1
            # -x -y
                elif abs((h[0] - 1) - self.train[t][0]) <= 1 and abs((h[1] - 1) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0] - 1
                    self.train[t][1] = h[1] - 1
            # -x +y
                elif abs((h[0] - 1) - self.train[t][0]) <= 1 and abs((h[1] + 1) - self.train[t][1]) <= 1:
                    self.train[t][0] = h[0] - 1
                    self.train[t][1] = h[1] + 1

                if t == self.train_size - 1:
                    self.tail_count.add(f"{self.train[t][0]},{self.train[t][1]}")

            h = self.train[t]


class TestRopeSpace(unittest.TestCase):

    def test_right_head_movement(self):
        r_space = RopeSpace(2)
        self.assertTrue(r_space.train[0] == [0, 0])
        r_space.move_head("R", 2)
        self.assertTrue(r_space.train[0] == [0, 2])
        self.assertTrue(r_space.train[1] == [0, 1])
        self.assertTrue(len(r_space.tail_count) == 2)

    def test_left_head_movement(self):
        r_space = RopeSpace(2)
        self.assertTrue(r_space.train[0] == [0, 0])
        r_space.move_head("L", 2)
        self.assertTrue(r_space.train[0] == [0, -2])
        self.assertTrue(r_space.train[1] == [0, -1])
        self.assertTrue(len(r_space.tail_count) == 2)

    def test_up_head_movement(self):
        r_space = RopeSpace(2)
        self.assertTrue(r_space.train[0] == [0, 0])
        r_space.move_head("U", 2)
        self.assertTrue(r_space.train[0] == [2, 0])
        self.assertTrue(r_space.train[1] == [1, 0])
        self.assertTrue(len(r_space.tail_count) == 2)

    def test_down_head_movement(self):
        r_space = RopeSpace(2)
        self.assertTrue(r_space.train[0] == [0, 0])
        r_space.move_head("D", 2)
        self.assertTrue(r_space.train[0] == [-2, 0])
        self.assertTrue(r_space.train[1] == [-1, 0])
        self.assertTrue(len(r_space.tail_count) == 2)


if __name__ == "__main__":
    result = load_data("data_9", 2)
    print(f"Tail counter {result}")

    result = load_data("data_9", 10)
    print(f"Tail counter part 2 {result}")
