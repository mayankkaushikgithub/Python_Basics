'''
Unique triangles

You are given n triangles. You are required to find how many triangles are unique out of given triangles.
For each triangle you are given three integers a, b and c (the sides of a triangle).
A triangle is said to be unique if there is no other triangle with same set of sides.

Note : It is always possible to form triangle with given sides.

Input Constraints :
    Line 1 : Integer n, the number of triangles
    Next n lines : Three integers a,b,c (sides of a triangle).
Output Format :
    print single integer, the number of unique triangles.

Constraints :   1 <= n <= 10^4      1 <= a,b,c <= 10^15.

Sample Input :                  Sample Output :
5                                     1
7 6 5
5 7 6
8 2 9
2 3 4
2 4 3

'''

from sys import stdin

def uniqueTriangles(arr):
    sides = [None for i in range(n)]
    mydict = {}

    for ele in arr:
        if ele in mydict:
            mydict[ele] += 1
        else:
            mydict[ele] = 1

    for i in range(0, n):
        # Push all the sides of the current triangle
        sides[i] = (arr[i])

        # Sort the three sides
        sides[i] = tuple(sorted(sides[i]))

        # Store the frequency of the sides of the triangle
        m[sides[i]] += 1

    # To store the count of unique triangles
    count = 0
    for i in m:

        # If current triangle has unique sides
        if m[i] == 1:
            count += 1

    return count


def takeInput() :
    print("\nEnter size of Array:")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter elements of Array:")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#main
print("Enter the no. of Triangles: ")
t = int(stdin.readline().strip())

while t > 0 :
    arr, n = takeInput()

    print("\nArray with Intersection of elements:")
    print(uniqueTriangles(arr, n))

    t -= 1