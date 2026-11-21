# Question 8: Inverted Star Pyramid

#   * * * * * * *
#     * * * * *
#       * * *
#         *

rows = 5

for row in range(rows, 0, -1):
    for space in range(rows - row):
        print("  ", end="")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()