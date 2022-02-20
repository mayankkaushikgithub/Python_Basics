# Code Bubble Sort
#
# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array
# using 'Bubble Sort'.
#
# Note: Change in the input array/list itself. You don't need to return or print the elements.
#
# Input format :
#         The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
#             Then the test cases follow.
#         First line of each test case or query contains an integer 'N' representing the size of the array/list.
#         Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output format :
#         For each test case, print the elements of the array/list in sorted order separated by a single space.
#
# Output for every test case will be printed in a separate line.
# Constraints :       1 <= t <= 10^2          0 <= N <= 10^3
# Time Limit: 1 sec
#
# Sample Input 1:     1                               Sample Output 1:    1 2 3 4 6 13 28
#                     7
#                     2 13 4 1 3 6 28
#
# Sample Input 2:     2                               Sample Output 2:    0 2 3 6 9
#                     5                                                   1 2 3 4
#                     9 3 6 2 0
#                     4
#                     4 3 2 1


from sys import stdin


def bubbleSort(arr, n):

    for i in range(len(arr)):                   # traverse through all elements of array

        for j in range(0, len(arr)-i-1):          # Last i elements are already in place

            # traverse the array from 0 to n-i-1, Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# Taking Input Using Fast I/O
def takeInput():
    print("\nEnter Size of the Array/List:")
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    print("\nEnter Elements of the Array:")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
arr, n = takeInput()
print("\nSorted List:",bubbleSort(arr, n))

