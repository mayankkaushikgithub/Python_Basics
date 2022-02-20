# Swap Alternate

# You have been given an array/list(ARR) of size N.
# You need to swap every pair of alternate elements in the array/list.
# You don't need to print or return anything, just change in the input array itself.

# Input Format :
#         The first line contains an Integer 't' which denotes the number of test cases or queries
#         to be run. Then the test cases follow.
#         First line of each test case or query contains an integer 'N' representing the size of
#         the array/list.
#         Second line contains 'N' single space separated integers representing the elements in
#         the array/list.

# Output Format :
#         For each test case, print the elements of the resulting array in a single row
#         separated by a single space.
#         Output for every test case will be printed in a separate line.

# Constraints :   1 <= t <= 10^2        # 0 <= N <= 10^5
# Time Limit:     1sec

# Sample Input 1:     1                                 # Sample Output 1 :   3 9 12 6 32 4
#                     6
#                     9 3 6 12 4 32

# Sample Input 2:     2                                 # Sample Output 2 :   3 9 12 6 32 4 11 5 19
#                     9                                                       2 1 4 3
#                     9 3 6 12 4 32 5 11 19
#                     4
#                     1 2 3 4



from sys import stdin

def swapAlternate(arr, n):
    print("\nWait for it.....")

    for i in range(0, n-1, 2):
        t = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = t
    print("\nDone.:")
    #Your code goes here


#Taking Input Using Fast I/O
def takeInput() :
    print("\nEnter the no. of elements you want to enter")
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    print("\nEnter the elements")
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

#Printing the array/list
def printList(arr, n) :
    print("\nNew Array after sorting is:")
    for i in range(n) :
        print(arr[i], end = " ")
    print()

#main
print("Enter total no. of test cases you want to perform\n")
t = int(stdin.readline().rstrip())      # It, automatically adds ‘\n’ after each sentence.

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1


