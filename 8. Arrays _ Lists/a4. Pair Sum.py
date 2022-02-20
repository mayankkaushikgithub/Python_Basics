# Pair Sum
#
# You have been given an integer array/list(ARR) and a number X.
# Find and return the total number of pairs in the array/list which sum to X.
# Note: Given array/list can contain duplicate elements.
#
# Input format :
#         The first line contains an Integer 't' which denotes the number of test cases or
#         queries to be run. Then the test cases follow.
#         First line of each test case or query contains an integer 'N' representing the size
#         of the first array/list.
#         Second line contains 'N' single space separated integers representing the elements in the
#         array/list.
#         Third line contains an integer 'X'.
# Output format :
#         For each test case, print the total number of pairs present in the array/list.
#
# Output for every test case will be printed in a separate line.
#
# Constraints :   1 <= t <= 10^2
#                 0 <= N <= 10^3
#                 0 <= X <= 10^9
# Time Limit:     1 sec
#
# Sample Input 1:     1                                   Sample Output 1:    7
#                     9
#                     1 3 6 2 5 4 3 2 4
#                     7
#
# Sample Input 2:     2                                   Sample Output 2:    0
#                     9                                                       2
#                     1 3 6 2 5 4 3 2 4
#                     12
#                     6
#                     2 8 10 5 -2 5
#                     10
#
# Explanation for Input 2:
# Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.
# For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).

from sys import stdin


def pairSum(arr, n, x):
    k = 0
    for i in range(0, n):
        for j in range(i+1, n):     # ith se agla dekhna hai
            l = arr[i]+arr[j]
            if l == x:
                k = k + 1
    # print(k, end=" ")

    return k
# Your code goes here


# Taking Input Using Fast I/O
def takeInput():
    print("\nEnter Size of Array:")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter Elements in the List:")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
print("\nEnter the no. of Test Cases/Queries you want to perform:")
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print("\nWhat should be sum ?")
    x = int(stdin.readline().strip())

    print("\nTotal Pairs: ", pairSum(arr, n, x))

    t -= 1