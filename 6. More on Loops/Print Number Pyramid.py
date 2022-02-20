# Print Number Pyramid
# Print the following pattern for a given n.
# For eg. N = 6
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456

n = int(input())

for row in range(n):

    for space in range(row):
        print(" ", end="")

    for column in range(n-row):
        print(row+1, end="")
        row = row + 1

    print()

for row in range(2, n+1):

    for space in range(n-row):
        print(" ", end="")
    a = n - row + 1
    for column in range(row):
        print(a, end="")
        a = a + 1

    print()









