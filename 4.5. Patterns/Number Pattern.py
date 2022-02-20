# For eg. N = 5
#
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input())

for row in range(n+1):

    for left_column in range(row):
        print(left_column+1, end="")

    for space in range(n-row):# use this loop two times to get your pattern
        print(" ",end="")

    for space in range(n-row):
        print(" ",end="")

    for right_column in range(row, 0, -1):
        print(right_column, end="")

    print()






