import math

row = 2978
column = 3083

# row = 3
# column = 4

if __name__ == "__main__":
    # first calculate the number of operations that need to be made
    row_col = row * column
    x = row - 2
    y = column - 1

    row_tri = math.floor((x*(x + 1)) / 2)   # triangle numbers
    col_tri = math.floor((y*(y + 1)) / 2)

    operations = row_col + row_tri + col_tri
    print(f"Number of operations to perform: {operations}")

    # then perform those operations (brute force?)
    result = 20151125
    for x in range(1, operations):
        result = result * 252533
        result = result % 33554393

    print(f"the key is {result}")  # love these puzzles where you just have to see the pattern in the numbers

