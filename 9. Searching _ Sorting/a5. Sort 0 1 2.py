# Sort 0 1 2
#
# You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s.
# Write a solution to sort this array/list in a 'single scan'.
# 'Single Scan' refers to iterating over the array/list just once or to put it in other words,
# you will be visiting each element in the array/list just once.
#
# Note: You need to change in the given array/list itself. Hence, no need to return or print anything.
#
# Input format :
#     The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
#     Then the test cases follow.
#     First line of each test case or query contains an integer 'N' representing the size of the array/list.
#     Second line contains 'N' single space separated integers(all 0s, 1s and 2s) representing the elements in the array/list.
# Output Format :
#     For each test case, print the sorted array/list elements in a row separated by a single space.
#
# Output for every test case will be printed in a separate line.
# Constraints :       1 <= t <= 10^2      0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1:     1                           Sample Output 1:    0 0 0 1 1 2 2
#                     7
#                     0 1 2 0 2 0 1
# Sample Input 2:     2                           Sample Output 2:    0 1 1 2 2
#                     5                                               0 0 0 1 1 2 2
#                     2 2 0 1 1
#                     7
#                     0 1 2 0 1 2 0



# Algorithm:
# 1.Keep three counter c0 to count 0s, c1 to count 1s and c2 to count 2s
# 2.Traverse through the array and increase the count of c0 is the element is 0,
#   increase the count of c1 is the element is 1 and increase the count of c2 is the element is 2
# 3.Now again traverse the array and replace first c0 elements with 0, next c1 elements with 1 and
#   next c2 elements with 2.

from sys import stdin


def sort012(arr, n):
    # Variables to maintain the count of 0's, 1's and 2's in the array
    count0 = 0
    count1 = 1
    count2 = 2

    for i in range(n):
        if arr[i] == 0:
            count0 +=1
        elif arr[i] == 1:
            count1 += 1
        elif arr[i] == 2:
            count2 += 1

    for i in range(0, count0):                          # Putting the 0's in the array in starting.
        arr[i] = 0
    for i in range(count0, (count0+count1)):              # Putting the 1's in the array after the 0's.
        arr[i] = 1
    for i in range((count0+count1), n):                 # Putting the 2's in the array after the 1's
        arr[i] = 2

    return


# Taking Input Using Fast I/O
def takeInput():
    print("\nEnter the Size of Array:")
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements:")
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    print("\nArray after sorting 0 1 2:")
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
print("Enter the Number of Queries you want to perform")
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)

    t -= 1



