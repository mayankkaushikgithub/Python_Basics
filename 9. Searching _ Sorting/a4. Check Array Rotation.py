# Check Array Rotation
#
# You have been given an integer array/list(ARR) of size N.
# It has been sorted(in increasing order) and then rotated by some number 'K' in the clockwise direction.
# Your task is to write a function that returns the value of 'K', that means, the index from which the
# array/list has been rotated.
#
# Input format :
#     The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
#     Then the test cases follow.
#     First line of each test case or query contains an integer 'N' representing the size of the array/list.
#     Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
#     For each test case, print the value of 'K' or the index from which which the array/list has been rotated.
#
# Output for every test case will be printed in a separate line.
# Constraints :   1 <= t <= 10^2      0 <= N <= 10^5
# Time Limit: 1 sec
#
# Sample Input 1:     1                       Sample Output 1:    2
#                     6
#                     5 6 1 2 3 4
# Sample Input 2:     2                       Sample Output 2:    0
#                     5                                           3
#                     3 6 8 9 10
#                     4
#                     10 20 30 1
#


# Solution
# If we take closer look at examples, we can notice that the number of rotations is equal to
# index of minimum element. A simple linear solution is to find minimum element and returns its index.

from sys import stdin

def arrayRotateCheck(arr, n):    # Solution 1 (using Linear Search)
# but this soln doesn't use adv. of Circularly Sorted Array, to use it do by Binary Search
    if n>0:
        min = arr[0]

        for i in range(0, n):
            if (min > arr[i]):
                min = arr[i]
                min_index = i
                return min_index

    return 0


#Taking Input Using Fast I/O
def takeInput() :
    print("\nEnter the Size of Array:")
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements:")
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
print("Enter the Number of Test Cases you want to perform:")
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print("\nArray is rotated by", arrayRotateCheck(arr, n))

    t -= 1