# puzzle_input = 34000000
puzzle_input = 10

def get_score(num):
    score = 0
    for i in range(1, num + 1):
        if (num % i) == 0:
            score += i * 10
    else:
        return score

def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if (num % i) == 0:
            factors.append(i)
    return factors


def solver(val_min, val_max, end):
    x = int((val_min + val_max)/2)

    if x % 2 == 0:
        x += 1
    not_a_prime = True
    num_score = get_score(x)
    while not_a_prime:
        if num_score != -1:
            not_a_prime = False
        else:
            print("prime")
            x += 1
            num_score = get_score(x)

    # print(s)
    print(f"min {val_min}, max {val_max}, mid {x}")
    if num_score == end:
        return x
    elif val_max - val_min == 1:
        return -1
    elif num_score > end:
        print("too high")
        return solver(val_min, x, end)
    else:
        print("too low")
        return solver(x, val_max, end)

if __name__ == "__main__":
    solving = True
    answer = 0
    min_dex = 0

    for x in range(1, 21):
        s = get_score(x)
        print(f"{x} {s} {get_factors(x)}")
        # if 34000000 % s == 0:
        #     print("mean anything?")
        #     break
        # else:
        #     print(x)
    # while solving:
    #     answer = solver(min_dex, puzzle_input, puzzle_input)
    #     if answer != -1:
    #         solving = False
    #     else:
    #         min_dex += 1000
    #         print(f"resetting with min dex {min_dex}")
    # print(f"House {answer} is the first to equal the input")

