import hashlib
import re

if __name__ == "__main__":
    # salt = "abc"
    salt = "ahsbgdzn"
    keys = 0
    threes = []
    count = 0
    index_of_last = 0
    while keys < 64:
        hash = hashlib.md5(f"{salt}{count}".encode('utf-8')).hexdigest()
        for x in range(2016):
            hash = hashlib.md5(hash.encode('utf-8')).hexdigest()
        match_three = re.search("([a-zA-Z0-9])\\1\\1", hash)
        match_five = re.search("([a-zA-Z0-9])\\1\\1\\1\\1", hash)

        if match_five:
            temp = []
            for x in threes:
                if x[0] == match_five[0] and count - x[1] <= 1000:
                    keys += 1
                    if keys == 64:
                        index_of_last = x[1]
                    temp.append(x)
            if temp:
                for y in temp:
                    threes.remove(y)

        if match_three:
            padded_match = match_three[0]+match_three[0][0:2]
            threes.append([padded_match, count])

        count += 1

    print(f"64th key generated at index {index_of_last}")
