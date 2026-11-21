# Question 5: Repeated Row Number Triangle

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = 5

for row in range(1, rows + 1):
    for count in range(row):
        print(row, end=" ")
    print()