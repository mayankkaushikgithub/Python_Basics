# Find Unique

# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.

# Note: Unique element is always present in the array/list according to the given condition.

# Input format :
        # The first line contains an Integer 't' which denotes the number of test cases or queries
        # to be run. Then the test cases follow.
        # First line of each test case or query contains an integer 'N' representing the size
        # of the array/list.
        # Second line contains 'N' single space separated integers representing the elements
        # in the array/list.
# Output Format :
        # For each test case, print the unique element present in the array.

# Output for every test case will be printed in a separate line.
# Constraints : # 1 <= t <= 10^2    # 0 <= N <= 10^3
# Time Limit: 1 sec

# Sample Input 1:   # 1                         # Sample Output 1: 1
                    # 7
                    # 2 3 1 6 3 6 2

# Sample Input 2:   # 2                         # Sample Output 2: 4
                    # 5                                            10
                    # 2 4 7 2 7
                    # 9
                    # 1 3 1 3 6 6 7 10 7



import sys

def findUnique(arr, n) :

    # pick all elements one by one and compare them with elements of second loop individually
    # this will give us nos. which are same/identical if any.
    for i in range(n):
        j = 0
        for j in range(0, n, 1):    # loop for checking the elements which are not repeated
                                    # check the condition if any number is same

            # i!=j to avoid duplicacy && arr[i]==arr[j] to check for two repeating elements
            if (i != j and arr[i] == arr[j]):
                break               # if the no. doesn't match we break the loop
            j += 1
        # as we get out of j-loop means some no.(in i) is not equal to any other no.(in j)
        # then j value will be last(i.e size of array) then this'll be our unique element.
        if (j == n):
            return arr[i]

    return -1


#Taking Input Using Fast I/O
def takeInput() :
    print("\nEnter the Size:")
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    print("\nEnter the Elements")
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
print("Enter the no. of Test Cases you want to perform")
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1










