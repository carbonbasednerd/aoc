import unittest
import json


def load_puzzle(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data


def load_puzzle_as_string(file):
    text_file = open("data.json", "r")
    data = text_file.read()
    text_file.close()
    return data

# Need to iterate through the json. Recursively? Flatten it out?
def parse_json(data):
    sum = 0
    num = ""
    for key in data:
        if key.isnumeric() or key == '-':
            num += key
        else:
            if num != "":
                sum += int(num)
                num = ""
    return sum

def parse_json_part_2(data):
    sum = {0: Brace(0, False)}
    num = ""
    trigger = ""
    counter = 0
    last_group = []
    for key in data:
        if key in ['r', 'e', 'd']:
            if num != "":
                sum[counter].add_value(int(num))
                num = ""
            if key == 'r' and trigger == "":
                trigger += "r"
            if key == 'e' and trigger == "r":
                trigger += "e"
            if key == 'd' and trigger == "re":
                trigger += "d"
        else:
            if trigger == "red":
                if last_group[-1] == '{':
                    sum[counter].ignore = True
            trigger = ""

            if key.isnumeric() or key == '-':
                num += key
            elif key == '[':
                if num != "":
                    sum[counter].add_value(int(num))
                    num = ""
                last_group.append(key)
            elif key == ']':
                if num != "":
                    sum[counter].add_value(int(num))
                    num = ""
                last_group.pop()
            elif key == '{':
                if num != "":
                    sum[counter].add_value(int(num))
                    num = ""
                last_group.append(key)
                counter += 1
                if counter not in sum.keys():
                    sum[counter] = Brace(0, False)
            elif key == '}':
                if num != "":
                    sum[counter].add_value(int(num))
                last_group.pop()
                if not sum[counter].ignore:
                    sum[counter - 1].add_value(sum[counter].count)
                sum[counter] = Brace(0, False)
                num = ""
                counter -= 1
            else:
                if num != "":
                    sum[counter].add_value(int(num))
                    num = ""
    total = 0
    for entry in sum:
        total += sum[entry].count
    print(total)
    return total


class Brace:
    def __init__(self, count, ignore):
        self.count = count
        self.ignore = ignore

    def add_value(self, val):
        self.count += val

class TestSolution(unittest.TestCase):
    def test_parse_json(self):
        data = "{'c': 'violet', 'a': 'yellow', 'b': 'violet'}:25,'test'"
        self.assertTrue(parse_json(data) == 25)
        data = "{'c': 'violet', 'a': 'yellow', 'b': 'violet'}:-25,'test'"
        self.assertTrue(parse_json(data) == -25)
        data = "[1,2,3]"
        self.assertTrue(parse_json(data) == 6)
        data = "{'a':2,'b':4}"
        self.assertTrue(parse_json(data) == 6)

    # 45058 - still too low
    def test_parse_json_part_2(self):
        data = "[1,2,3]"
        self.assertTrue(parse_json_part_2(data) == 6)
        data = "[1,{'c':'red','b':2},3]"
        self.assertTrue(parse_json_part_2(data) == 4)
        data = "{'d':'red','e':[1,2,3,4],'f':5}"
        self.assertTrue(parse_json_part_2(data) == 0)
        data = "[1,'red',5]"
        self.assertTrue(parse_json_part_2(data) == 6)
        data = "[{'a':1, {'b':1, {'c':1, 'd':'red'}}}]"
        self.assertTrue(parse_json_part_2(data) == 2)
        data = "[{'a':1, {'b':1, 'e':'red', {'c':1}}}]"
        self.assertTrue(parse_json_part_2(data) == 1)
        data = "[{'a':1, 'g':'red',{'b':1,{'c':1}}}]"
        self.assertTrue(parse_json_part_2(data) == 0)
        data = "['red', {'a':1,{'b':1,{'c':1}}}]"
        self.assertTrue(parse_json_part_2(data) == 3)
        data = "['red', {'a':1,{'b':1, 'c':'red',{'c':1}}}]"
        self.assertTrue(parse_json_part_2(data) == 1)
        data = "['red', 1,1,1,1,1,{'a':1,{'b':1, 'c':'red',{'c':1}}}]"
        self.assertTrue(parse_json_part_2(data) == 6)


if __name__ == '__main__':
    json_data = load_puzzle_as_string("data.json")
    print(json_data)
    print(parse_json(json_data))

    print(parse_json_part_2(json_data))
