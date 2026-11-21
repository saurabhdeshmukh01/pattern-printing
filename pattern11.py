# Question 11: Hollow Right-Angled Triangle

# *
# * *
# *   *
# *     *
# * * * * *

rows = 5

for row in range(1, rows + 1):
    for col in range(1, row + 1):
        if col == 1 or col == row or row == rows:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()