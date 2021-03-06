# Second Largest in array
#
# You have been given a random integer array/list(ARR) of size N. You are required to find and
# return the second largest element present in the array/list.
# If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31
# (It is the smallest value for the range of Integer)
#
# Input format :
#     The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
#     Then the test cases follow.
#     The first line of each test case or query contains an integer 'N' representing the size
#     of the array/list.
#     The second line contains 'N' single space separated integers representing the elements
#     in the array/list.
# Output Format :
#     For each test case, print the second largest in the array/list if exists, -2147483648 otherwise.
#
# Output for every test case will be printed in a separate line.
# Constraints :   1 <= t <= 10^2      0 <= N <= 10^5
# Time Limit: 1 sec

# Sample Input 1:     1                                   Sample Output 1:    13
#                     7
#                     2 13 4 1 3 6 28

# Sample Input 2:     1                                   Sample Output 2:    6
#                     5
#                     9 3 6 2 9

# Sample Input 3:     2                                   Sample Output 3:    -2147483648
#                     2                                                        8
#                     6 6
#                     4
#                     90 8 90 5


from sys import stdin


def secondLargestElement(arr, n):

    if n <= 1:
        return -2147483648

    max = -1
    sec_max = -1
    for i in range(n):
        if arr[i] > max :
            sec_max = max       # first empty the 'max' by moving its value in 'sec_max'
            max = arr[i]        # assign max value encountered in array to 'max'

        elif arr[i] < max and arr[i] > sec_max:
            sec_max = arr[i]

        elif arr[i] == max:
            sec_max = max


    return sec_max
    # pass


# Your code goes here


# Taking Input Using Fast I/O
def takeInput():
    print("\nEnter the Size of Array:")
    n = int(stdin.readline().rstrip())
    if n != 0:
        print("\nEnter the Elements of Array:")
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# main
print("Enter the Number of Test Cases you want to perform:")
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print("\nThe Second Largest Element of Array:",secondLargestElement(arr, n))

    t -= 1