'''
Leaders in array

Given an integer array A of size n. Find and print all the leaders present in the input array.
An array element A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
Print all the leader elements separated by space and in the same order they are present in the input array.

Input Format :
        Line 1 : Integer n, size of array
        Line 2 : Array A elements (separated by space)
Output Format :
        leaders of array (separated by space)

Constraints :   1 <= n <= 10^6

Sample Input 1 :        6                                           Sample Output 1 :        34 2 0 -1
                        3 12 34 2 0 -1

Sample Input 2 :        5                                           Sample Output 2 :        17 6
                        13 17 5 4 6
'''



from sys import stdin


def leadersInArray(arr,size):

    for i in range(0, size):
        for j in range(i, size):
            if arr[i] < arr[j]:
                break
            if j == size - 1:  # If loop didn't break
                print(arr[i], end = " ")

# Taking input using fast I/O method

def takeInput():
    print("Enter size of array:")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter elements: ")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

# main
arr, n = takeInput()
leadersInArray(arr, n)

#222
# 448 241 363 161 447 333 369 28 169 474 161 485 433 238 188 423 111 59 144 354 346 80 463 246 356 72 159 377 430 229 395 444 111 72 486 491 397 110 30 458 48 471 39 105 366 330 371 462 463 137 352 83 200 439 284 411 71 439 48 385 355 337 234 38 351 51 128 381 491 453 9 116 6 451 64 407 204 468 189 379 222 208 255 318 387 462 273 167 35 239 81 378 329 485 493 431 220 362 384 469 296 202 453 417 284 93 334 220 470 367 374 430 226 263 281 292 239 1 351 222 378 146 299 162 442 299 137 171 258 418 247 393 345 389 116 41 487 411 341 490 177 209 224 237 465 208 291 67 258 385 244 107 91 306 239 191 309 116 468 438 482 138 323 361 208 213 406 452 230 431 344 251 49 33 297 218 386 448 100 417 3 209 337 6 480 330 129 352 102 178 134 272 3 345 178 338 184 146 58 42 409 4 367 221 374 241 243 129 323 105 137 328 94 253 161 209 257 414 196 376 218 457
