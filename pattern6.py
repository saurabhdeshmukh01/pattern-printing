# Question 6: Right-Aligned Triangle

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

rows = 5

for row in range(1, rows + 1):
    for space in range(rows - row):
        print("  ", end="")
    for star in range(row):
        print("*", end=" ")
    print()