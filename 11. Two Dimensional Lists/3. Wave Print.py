'''
Wave Print

For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, i.e,
print the first column top to bottom, next column bottom to top and so on.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
        Then the test cases follow.
        First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space.
        They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
        Second line onwards, the next 'N' lines or rows represent the ith row values.
        Each of the ith row constitutes 'M' column values separated by a single space.
Output format :
        For each test case, print the elements of the two-dimensional array/list in the sine wave order in a single line, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :       1 <= t <= 10^2      0 <= N <= 10^3      0 <= M <= 10^3
Time Limit: 1sec

Sample Input 1:     1                   Sample Output 1:    1 5 9 10 6 2 3 7 11 12 8 4
                    3 4
                    1  2  3  4
                    5  6  7  8
                    9 10 11 12

Sample Input 2:     2                   Sample Output 2:    1 4 7 10 13 14 11 8 5 2 3 6 9 12 15
                    5 3                                     10 40 70 80 50 20 30 60 90
                    1 2 3
                    4 5 6
                    7 8 9
                    10 11 12
                    13 14 15
                    3 3
                    10 20 30
                    40 50 60
                    70 80 90
'''

from sys import stdin


def wavePrint(mat, nRows, mCols):


    for i in range(mCols):                      # loop to iterate over all the columns

        if i % 2 == 0:                          # for even column: 'Go from Top to Bottom'
            for j in range(nRows):
                print(mat[j][i], end=" ")
        else:                                   # for odd column: 'Go from Bottom to Top'
            for j in range(nRows-1, -1, -1):
                print(mat[j][i], end=" ")



# Your code goes here


# Taking Iput Using Fast I/O
def take2DInput():
    print("\nEnter the Number of Rows & Columns:")
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    print("\nEnter the Elements:")
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
print("Enter the Number of Test Cases you want to perform:")
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1