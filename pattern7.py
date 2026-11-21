# Question 7: Star Pyramid

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

rows = 5

for row in range(1, rows + 1):
    for space in range(rows - row):
        print("  ", end="")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()