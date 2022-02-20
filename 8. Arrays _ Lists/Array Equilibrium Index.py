'''
Array equilibrium index
Send Feedback
For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] is equal to the sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, the item at the index 'i' is not included in either part.
If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be returned. Negative one(-1) if no such index is present.
Example:
Let's consider an array/list Arr = [2, 3, 10, -10, 4, 2, 9]  of size, N = 7.

There exist two equilibrium indices, one at 2 and another at 3.

At index 2, the sum of all the elements to the left, [2 + 3] is 5, and the elements to its right, [-10 + 4 + 2 + 9] is also 5. Hence index 2 is an equilibrium index according to the condition we want to achieve. Mind it that we haven't included the item at index 2, which is 10, to either of the parts.

Similarly, we can see at index 3, the elements to its left sum up to 15 and to the right, sum up to 15 either.

Since index 2 comes early in the order, left to right, the answer would be 2.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains an integer 'N' representing the size of the first array/list.

The second line contains 'N' single space separated integers representing the elements of the array/list
Output Format :
For each test case, print the 'Equilibrium Index'.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^6

Time Limit: 1 sec
Sample Input 1 :
1
5
1 4 9 3 2
Sample Output 1 :
2
Sample Input 2 :
2
3
1 4 6
3
1 -1 4
Sample Output 2 :
-1
2
'''

from sys import stdin

# METHOD - 1 (Time complexity of this solution is O(n^2).)
# def arrayEquilibriumIndex(arr, n):
#     for i in range(n):
#         leftSum = 0
#         rightSum = 0
#         for j in range(i):
#             leftSum = leftSum + arr[j]
#         for j in range(i+1, n):
#             rightSum = rightSum + arr[j]
#         if leftSum == rightSum:
#             return i

# METHOD - 2 (The idea is to get total sum of array first.
#             Then Iterate through the array and keep updating the left sum which is initialized as zero.
#             In the loop, we can get right sum by subtracting the elements one by one.)
# NOTE: A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
#       Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
#       This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

def arrayEquilibriumIndex(arr, n):

    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):

        # total_sum is now right sum for index i
        total_sum -= num

        if leftsum == total_sum:
            return i
        leftsum += num

    return -1        # If no equilibrium index found, then return -1


# Your code goes here


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1