# Question 12: Butterfly Pattern

# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

rows = 5

for row in range(1, rows + 1):
    for star in range(row):
        print("*", end=" ")
    spaces = 2 * (rows - row)
    for space in range(spaces):
        print("  ", end="")
    for star in range(row):
        print("*", end=" ")
    print()

for row in range(rows, 0, -1):
    for star in range(row):
        print("*", end=" ")
    spaces = 2 * (rows - row)
    for space in range(spaces):
        print("  ", end="")
    for star in range(row):
        print("*", end=" ")
    print()