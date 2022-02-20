'''
Even Count

You are provided with an integer array where each number is present either odd number of times or even number of times.
You have to find and return the number which is present even number of times.
If multiple numbers are present even number of times, then return that number which occurs first among these numbers
in the given array. If no such number exists, then return -1.

Note : You may take extra space but solve this problem in O(n) time.

Input Format:
        Line 1 : An Integer N i.e. size of array
        Line 2 : N integers which are elements of the array, separated by spaces
Output Format:
        Array element occurring even no. of times

Constraints :   1 <= N <= 10^5

Sample Input:   6                       Sample Output:  5
                2 5 3 5 3 4
'''

def evenCount(arr):

    mydict = {}

    for ele in arr:
        if ele in mydict:
            mydict[ele] += 1
        else:
            mydict[ele] = 1

    # ----------------------------- My Soln.
    # count = []
    # for key, val in mydict.items():
    #     if val % 2 == 0:
    #         count.append(key)
    # return count[0]
    #-----------------------------

    #----------------------------- CN Soln. (better)
    for val in arr:
        if mydict[val] % 2 == 0:
            return val
    #------------------------------


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(evenCount(arr))
