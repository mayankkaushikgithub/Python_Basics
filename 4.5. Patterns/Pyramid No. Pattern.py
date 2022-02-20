# Input format : N (Total no. of rows)
# Output format : Pattern in N lines
#
# Sample Input :      5
# Sample Output :         1                           1
#                        212                         21 2
#                       32123                       321 23
#                      4321234                     4321 234
#                     543212345                   54321 2345

n = int(input())

for row in range(1,n+1):

    for space in range(1,n-row+1):
        print(" ", end="")

    for column in range(row, 0, -1):
        print(column, end="")

    for sec_column in range(1,row):
        print(sec_column+1, end="")
        # row = row + 1

    print()








