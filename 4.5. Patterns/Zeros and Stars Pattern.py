# Sample Input 1 :    3
# Sample Output 1 :   *00   *   00*
#                     0*0   *   0*0
#                     00*   *   *00

# Pattern for N =         4
# Sample Output:          *000  *   000*
#                         0*00  *   00*0
#                         00*0  *   0*00
#                         000*  *   *000

# Sample Input 2 :    5
# Sample Output 2 :   *0000     *       0000*
#                     0*000     *       000*0
#                     00*00     *       00*00
#                     000*0     *       0*000
#                     0000*     *       *0000

n = int(input())
for row in range(n):

    for left_column in range(n):    # printing left pattern with '*' diagonal

        if row == left_column:
            print("*", end="")
        else:
            print("0", end="")

    for center_column in range(1):  # printing middle star column
        print("*", end="")

    for right_column in range(n):   # printing left pattern with '*' diagonal

        if right_column == n-row-1:
            print("*", end="")
        else:
            print("0", end="")
    print()





