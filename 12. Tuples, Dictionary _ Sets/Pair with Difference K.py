'''
Pairs with difference K

You are given with an array of integers and an integer K.
You have to find and print the count of all such pairs which have difference K.

Note: Take absolute difference between the elements of the array.

Input Format:
The first line of input contains an integer, that denotes the value of the size of the array.
    Let us denote it with the symbol n.
    The following line contains n space separated integers, that denote the value of the elements of the array.
    The following line contains an integer, that denotes the value of K.
Output format :
    The first and only line of output contains count of all such pairs which have an absolute difference of K.

Constraints :   0 <= n <= 10^4      Time Limit: 1 sec

Sample Input 1 :    4                           Sample Output 1 :   2
                    5 1 2 4
                    3

Sample Input 2 :    4                           Sample Output 2 :   6
                    4 4 4 4
                    0
9
2 -1 3 5 6 0 -1 2 6
3
'''

'''
Method 2 (Use Hashing) 
We can also use hashing to achieve the average time complexity as O(n) for many cases. 
 

1) Initialize count as 0.
2) Insert all distinct elements of arr[] in a hash map.  While inserting, 
   ignore an element if already present in the hash map.
3) Do following for each element arr[i].
   a) Look for arr[i] + k in the hash map, if found then increment count.
   b) Look for arr[i] - k in the hash map, if found then increment count.
   c) Remove arr[i] from hash table. 
'''

def printPairDiffK(arr, k):

    # ---------------------- Soln. 1 (simple)---
    # count = 0
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if (arr[i] - arr[j] == k) or (arr[j] - arr[i] == k):
    #             count += 1
    # return count
    # -------------------------------------------

    # ------------------------ Soln. 2 (using Hashing) (MY Soln.) (PARTIALLY CORRECT)
    # count = 0
    # mydict = {}
    # for i in arr:
    #     if ((arr[i]+k) in mydict):
    #         count += 1
    #     if ((arr[i]-k) in mydict):
    #         count  += 1
    #     if i in mydict:
    #         mydict[i] += 1
    #     else:
    #         mydict[i] = 1
    # return count

    # ------------------------ Soln. 2 (using Hashing) (CN Soln.) (CORRECT)
    pairCount = 0
    m = {}

    for num in l:
        if num + k in m:
            pairCount += m[num + k]  # counting the value if  corresponding key
        if k != 0 and num - k in m:
            pairCount += m[num - k]
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
    return pairCount
    #------------------------------------------------



# Main
n = int(input())
l = list(int(i) for i in input().strip().split(' '))
k = int(input())
print(printPairDiffK(l, k))

