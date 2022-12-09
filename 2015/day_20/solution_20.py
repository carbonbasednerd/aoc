puzzle_input = 34000000


def solve(target, val, house_limit):
    answer = target
    offset = 2
    not_done = True
    buckets = [val for i in range(0, target)]
    while not_done:
        if offset > target / 10:
            not_done = False
            break
        count = 0
        for i in range(offset-1, target, offset):
            if house_limit:
                count += 1
                if count > 50:
                    break

            buckets[i] += (offset * val)
            if buckets[i] >= puzzle_input:
                answer = min(i+1, answer)
                break
        offset += 1
    return answer


if __name__ == "__main__":
    print(f"answer part 1 = {solve(puzzle_input, 10, False)}")
    print(f"answer part 2 = {solve(puzzle_input, 11, True)}")

# 31953469 - still too high
# 2259441 - not the right answer - no clue given
# 2259440 - also not the right answer
# 17450495 not it
# 17450497 - nope
# 17450496 - no what the hell am i doing wrong?
# 786240 - answer! It was because I was looking for == and not >=
#solved part 2 with no help.
