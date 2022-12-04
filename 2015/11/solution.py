import unittest

puzzle_input = "hxbxwxba"
# puzzle_input = "abcdefgh"  #test
# puzzle_input = "ghijklmn"  #test

a_char = 97
z_char = 122
i_char = 105
o_char = 111
l_char = 108


def convert_password_to_ascii(data):
    d = []
    for e in range(0, len(data)):
        d.append(ord(data[e]))
    return d


def convert_ascii_to_char(input):
    result = ""
    for e in input:
        result += chr(e)
    return result


def increment_password(input, index):
    new_password = input
    if index < 0:
        return new_password

    if input[index] == z_char:
        new_password = increment_password(input, index-1)
        new_password[index] = a_char
    else:
        next_value = new_password[index] + 1
        if next_value == i_char or next_value == o_char or next_value == l_char:
            next_value += 1
        new_password[index] = next_value
    return new_password


# length should be array length -1
def test_password(input, length):
    if (105 in input) or (111 in input) or (108 in input):
        return False

    increasing_straight_count = 0
    increasing_double_count = 0
    buffer = []
    for e in range(0, length):
        buffer.insert(0, input[e])
        if e > 1:
            if (input[e]-input[e-1]) == 1 and (input[e-1]-input[e-2]) == 1:
                increasing_straight_count += 1
        if e > 0:
            if len(buffer) == 2:
                if buffer[0] == buffer[1]:
                    increasing_double_count += 1
                    buffer.clear()
                else:
                    buffer.pop()

    return increasing_straight_count > 0 and increasing_double_count > 1


def puzzle_logic(data, length):
    checking_password = True
    temp = data
    while checking_password:
        if test_password(temp, length):
            checking_password = False
        else:
            temp = increment_password(temp, length-1)
    return temp


class TestSolution(unittest.TestCase):
    def test_password_to_ascii(self):
        data = convert_password_to_ascii("test")
        self.assertTrue(116 == data[0])
        self.assertTrue(101 == data[1])
        self.assertTrue(115 == data[2])
        self.assertTrue(116 == data[3])

    def test_ascii_to_password(self):
        self.assertTrue("test" == convert_ascii_to_char([116, 101, 115, 116]))

    def test_increment_password(self):
        self.assertTrue([97, 98, 99, 101] == increment_password([97, 98, 99, 100], 3))
        self.assertTrue([97, 98, 100, 97] == increment_password([97, 98, 99, 122], 3))
        self.assertTrue([97, 97, 97, 97] == increment_password([122, 122, 122, 122], 3))
        self.assertTrue([100, 101, 106] == increment_password([100, 101, 104], 2))
        self.assertTrue([100, 101, 109] == increment_password([100, 101, 107], 2))
        self.assertTrue([100, 101, 112] == increment_password([100, 101, 110], 2))
        self.assertTrue([97, 106, 97] == increment_password([97, 104, 122], 2))
        self.assertTrue([97, 109, 97] == increment_password([97, 107, 122], 2))
        self.assertTrue([97, 112, 97] == increment_password([97, 110, 122], 2))
        self.assertTrue([106, 97, 97] == increment_password([104, 122, 122], 2))
        self.assertTrue([109, 97, 97] == increment_password([107, 122, 122], 2))
        self.assertTrue([112, 97, 97] == increment_password([110, 122, 122], 2))
        return

    def test_check_password(self):
        self.assertTrue(test_password([97, 98, 99, 110, 110, 100, 113, 113, 100], 9))
        self.assertFalse(test_password([97, 99, 101, 110], 4))
        self.assertTrue(test_password([101, 101, 102, 103, 103], 5))
        self.assertFalse(test_password([97, 99, 99, 101, 101, 105], 6))
        self.assertTrue(test_password([97, 97, 97, 97, 97, 97, 98, 99], 8))
        self.assertFalse(test_password([97, 97, 97, 98, 99, 100], 6))
        self.assertTrue(test_password([97, 97, 97, 97, 98, 99], 6))
        self.assertTrue(test_password([97, 97, 97, 97, 98, 99, 100], 7))
        self.assertFalse(test_password([97, 97, 97, 97, 105, 98, 99, 100], 8))
        self.assertFalse(test_password([97, 97, 97, 97, 108, 98, 99, 100], 8))
        self.assertFalse(test_password([97, 97, 97, 97, 111, 98, 99, 100], 8))


if __name__ == '__main__':
    puzzle_data = convert_password_to_ascii(puzzle_input)
    puzzle_data_length = len(puzzle_data)

    puzzle_data = puzzle_logic(puzzle_data, puzzle_data_length)
    print(f"Part 1 password is: {convert_ascii_to_char(puzzle_data)}")

    #For part 2
    puzzle_data = increment_password(puzzle_data, puzzle_data_length - 1)
    puzzle_data = puzzle_logic(puzzle_data, puzzle_data_length)
    print(f"Part 2 password is: {convert_ascii_to_char(puzzle_data)}")









