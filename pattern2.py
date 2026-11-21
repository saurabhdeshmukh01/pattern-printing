# Question 2: Right-Angled Triangle

# *
# * *
# * * *
# * * * *
# * * * * *

rows = 5

for row in range(1, rows + 1):
    for col in range(row):
        print("*", end=" ")
    print()