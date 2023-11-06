# much of this was solved just by looking at the puzzle data and manually figuring out the goals. could also
# had loaded the data and just ran time updates until a match of, for example, 4,3,2,1,0 with current locations was found


def rotate_disc(d):
    if d[0] == d[1]:
        d[1] = 0
    else:
        d[1] = d[1] + 1


if __name__ == "__main__":
    disc_1 = [16, 1]
    disc_2 = [6, 0]
    disc_3 = [18, 2]
    disc_4 = [4, 0]
    disc_5 = [2, 0]
    disc_6 = [12, 5]
    disc_7 = [10, 0]

    goal = [16, 5, 16, 1, 1, 7, 4]
    time = 0
    processing = True
    while processing:
        if disc_1[1] == goal[0] and disc_2[1] == goal[1] and disc_3[1] == goal[2] and disc_4[1] == goal[3] and disc_5[1] == goal[4] and disc_6[1] == goal[5] and disc_7[1] == goal[6]:
            processing = False
        else:
            time += 1
            rotate_disc(disc_1)
            rotate_disc(disc_2)
            rotate_disc(disc_3)
            rotate_disc(disc_4)
            rotate_disc(disc_5)
            rotate_disc(disc_6)
            rotate_disc(disc_7)

    print(f"drop the ball at time index {time}")
