import numpy as np

with open("input.txt") as f:
    m = [list(line.strip()) for line in f.readlines()]


def part1():
    matrix = np.array(m)
    rows, cols = matrix.shape

    row_lines = ["".join(l) for l in m]
    col_lines = ["".join(l) for l in np.transpose(m)]
    primary_diagonals = [
        "".join(l)
        for l in [np.diagonal(matrix, offset) for offset in range(-rows + 1, cols)]
    ]
    flipped_matrix = np.fliplr(matrix)
    secondary_diagonals = [
        "".join(l)
        for l in [
            np.diagonal(flipped_matrix, offset) for offset in range(-rows + 1, cols)
        ]
    ]

    res = 0
    for line in row_lines + col_lines + primary_diagonals + secondary_diagonals:
        res += line.count("XMAS") + line.count("SAMX")

    return res


def part2():
    res = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == 0 or j == 0 or i == len(m) - 1 or j == len(m[0]) - 1:
                continue

            upper_left = m[i - 1][j - 1]
            upper_right = m[i - 1][j + 1]
            lower_left = m[i + 1][j - 1]
            lower_right = m[i + 1][j + 1]

            if m[i][j] == "A":
                if (
                    upper_left == "M"
                    and lower_right == "S"
                    and upper_right == "M"
                    and lower_left == "S"
                ):
                    res += 1

                if (
                    lower_left == "M"
                    and upper_right == "S"
                    and lower_right == "M"
                    and upper_left == "S"
                ):
                    res += 1

                if (
                    upper_left == "M"
                    and lower_left == "M"
                    and upper_right == "S"
                    and lower_right == "S"
                ):
                    res += 1

                if (
                    upper_right == "M"
                    and lower_right == "M"
                    and upper_left == "S"
                    and lower_left == "S"
                ):
                    res += 1

    return res


print(f"part1: {part1()}")
print(f"part2: {part2()}")
