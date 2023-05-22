def load_data(file):
    output = []
    data = open(file, 'r')
    for line in data:
        output.append(line.strip())

    data.close()
    return output


class Screen:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [["." for i in range(width)] for j in range(height)]

    def print_screen(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                print(self.grid[y][x], end="")
            print("")
        print("")

    def count_lit_pixels(self):
        counter = 0
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] == "#":
                    counter += 1
        return counter

    def add_rectangle(self, rect_x, rect_y):
        for y in range(0, rect_y):
            for x in range(0, rect_x):
                self.grid[y][x] = "#"

    def rotate_x(self, col, shift):
        mod_shift = shift % self.height
        col_buffer = ["." for j in range(self.height)]
        # build buffer
        for y in range(0, self.height):
            col_buffer[(y + mod_shift) % self.height] = self.grid[y][col]

        # write buffer
        for y in range(0, self.height):
            self.grid[y][col] = col_buffer[y]

    def rotate_y(self, row, shift):
        mod_shift = shift % self.width
        row_buffer = ["." for j in range(self.width)]
        # build buffer
        for x in range(0, self.width):
            row_buffer[(x + mod_shift) % self.width] = self.grid[row][x]

        # write buffer
        for x in range(0, self.width):
            self.grid[row][x] = row_buffer[x]


if __name__ == "__main__":
    instructions = load_data("data_8")
    print(instructions)

    grid_height = 6
    grid_width = 50

    screen = Screen(grid_height, grid_width)

    for command in instructions:
        parsed = command.split(" ")
        if parsed[0] == "rect":
            split_coord = parsed[1].split("x")
            screen.add_rectangle(int(split_coord[0]), int(split_coord[1]))
        else:
            if parsed[1] == "row":
                screen.rotate_y(int(parsed[2].strip("y=")), int(parsed[4]))
            else:
                screen.rotate_x(int(parsed[2].strip("x=")), int(parsed[4]))

    screen.print_screen()
    print(f"Lit pixels = {screen.count_lit_pixels()}")
