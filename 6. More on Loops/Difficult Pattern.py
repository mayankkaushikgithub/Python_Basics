# Print the pattern
# Input format : N (Total no. of rows)
# Output format : Pattern in N lines

# Print the following pattern for the given number of rows.

# Sample Input :                      Sample Output :
#  N = 4                               1  2  3  4
#                                      9 10 11 12
#                                     13 14 15 16
#                                      5  6  7  8

# Sample Input :                        Sample Output :
#  N = 5                               1    2   3    4   5
#                                      11   12  13   14  15
#                                      21   22  23   24  25
#                                      16   17  18   19  20
#                                      6    7    8   9   10

# Sample Input:                         Sample Output:
#   N = 8                             1  2  3  4  5  6  7  8
#                                     17 18 19 20 21 22 23 24
#                                     33 34 35 36 37 38 39 40
#                                     49 50 51 52 53 54 55 56
#                                     57 58 59 60 61 62 63 64
#                                     41 42 43 44 45 46 47 48
#                                     25 26 27 28 29 30 31 32
#                                     9 10 11 12 13 14 15 16

n = int(input())
# p = n

for i in range (1, n+1, 2):
    k = (i - 1) * n + 1         # Crux of program

    for j in range(0, n):
        print (k, end=" ")
        k+=1

    print()

if n % 2 != 0:
    p = n - 1

for i in range(p, 1, -2):
    k = (i - 1) * n + 1

    for j in range(n):
        print(k, end=" ")
        k += 1

    print()

