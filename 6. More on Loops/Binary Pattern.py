# Input format : N (Total no. of rows)
# Output format : Pattern in N lines
#
# Sample Input :      5
# Sample Output :     11111
#                     0000
#                     111
#                     00
#                     1

n = int(input())

for row in range(n):

    if row%2 == 0:
        for column in range(n-row):
            print("1", end="")

    else:
        for column in range(n-row):
            print("0", end="")

    print()