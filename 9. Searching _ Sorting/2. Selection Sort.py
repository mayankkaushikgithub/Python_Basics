'''
The selection sort is best used when you have a small list of items to sort, the cost of swapping values does not matter,
and checking of all the values is mandatory.
The selection sort does not perform well on huge lists
Other sorting algorithms, such as quicksort, have better performance when compared to the selection sort.

Time Complexity Of Selection Sort
The sort complexity is used to express the number of execution times it takes to sort the list.
The implementation has two loops.

    The outer loop which picks the values one by one from the list is executed n times
    where n is the total number of values in the list.

    The inner loop, which compares the value from the outer loop with the rest of the values, is also executed n times
    where n is the total number of elements in the list.

    Therefore, the number of executions is (n * n), which can also be expressed as O(n2)
'''




from sys import stdin


def selectionSort(arr, n):

    for i in range(len(arr)):                   # put the correct element at ith position
        min_idx = i
        for j in range(i+1, len(arr)):          # Find the minimum element in remaining unsorted array

            if arr[i] > arr[j]:
                min_idx = j
                # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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
print("\nSorted List:",selectionSort(arr, n))

