# Question 3: Inverted Right-Angled Triangle

# * * * * *
# * * * *
# * * *
# * *
# *

rows = 5

for row in range(rows, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()