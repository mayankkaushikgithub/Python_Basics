'''
Maximise the sum

Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum
and return the maximum sum.
That is, we can switch from one array to another array only at common elements.
If no intersection element is present, we need to take sum of all elements from the array with greater sum.

Input Format :
     Line 1 : An integer M i.e. size of first array
     Line 2 : M integers which are elements of first array, separated by spaces
     Line 3 : An integer N i.e. size of second array
     Line 4 : N integers which are elements of second array, separated by spaces
Output Format :
     Maximum sum value

Constraints :   1 <= M, N <= 10^6

Sample Input :      6                                   Sample Output :     81
                    1 5 10 15 20 25
                    5
                    2 4 5 9 15

Explanation :
We start from array 2 and take sum till 5 (sum = 11). Then we'll switch to array at element 10 and take till 15.
So sum = 36. Now, no elements left in array after 15, so we'll continue in array 1. Hence sum is 81
'''


from sys import stdin

def maximizePathSum(arr1, m, arr2, n):

    i, j = 0, 0                                             # initialize indexes for ar1[] and ar2[]

    result, sum1, sum2 = 0, 0, 0                            # Initialize result and current sum through ar1[] and ar2[]

    while (i < m and j < n):                                # Below 3 loops are similar to merge in merge sort

        if arr1[i] < arr2[j]:                               # Add elements of ar1[] to sum1
            sum1 += arr1[i]
            i += 1

        elif arr1[i] > arr2[j]:                             # Add elements of ar2[] to sum2
            sum2 += arr2[j]
            j += 1

        else:                                               # we reached a common point

            result += max(sum1, sum2)                       # Take the maximum of two sums and add to result

            sum1, sum2 = 0, 0                               # Update sum1 & sum2 for elements after this intersection point

            temp = i                                        # Keep updating result while there are more common elements

            while i < m and arr1[i] == arr2[j]:
                sum1 += arr1[i]
                i += 1

            while j < n and arr1[temp] == arr2[j]:
                sum2 += arr2[j]
                j += 1

            result += max(sum1, sum2)
            sum1 = sum2 = 0

    while i < m:                                            # Add remaining elements of ar1[]
        sum1 += arr1[i]
        i += 1

    while j < n:                                            # Add remaining elements of b[]
        sum2 += arr2[j]
        j += 1

    result += max(sum1, sum2)                               # Add maximum of two sums of remaining elements

    return result



# Taking Input Using Fast I/O
def takeInput() :

    print("\nEnter size of Array:")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter elements of Array:")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#main

arr1, m = takeInput()
arr2, n = takeInput()

print("\nMaximum Path Sum:")
result = maximizePathSum(arr1, m, arr2, n)
print(result)