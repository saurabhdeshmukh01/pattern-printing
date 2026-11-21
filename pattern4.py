# Question 4: Increasing Number Triangle

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5

for row in range(1, rows + 1):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()