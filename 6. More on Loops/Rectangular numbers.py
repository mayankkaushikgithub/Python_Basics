# Rectangular numbers
# Print the following pattern for the given number of rows.

# Pattern for N = 4     # 4444444                            N = 3      #     33333
                        # 4333334                                       # 3    222     3
                        # 4322234                                       # 32    1     23
                        # 4321234                                       # 3    222     3
                        # 4322234                                       # 3    3333
                        # 4333334
                        # 4444444

# Input format : N (Total no. of rows)
# Output format : Pattern in N lines

n = int(input())

s = int(2*n-1)                                  # number of rows and columns to be printed

# for row in range(0, int(s / 2) + 1):            # UPPER HALF
#
#     m = n
#
#     for decr in range(0, row):                  # Decreasing part
#         print(m, end=" ")
#         m -= 1
#
#     for cons in range(0, s - 2 * row):          # Constant Part
#         print(n - row, end=" ")
#
#     m = n - row + 1                             # Increasing part.
#     for incr in range(0, row):
#         print(m, end=" ")
#         m += 1
#     print()

for row in range(int(s / 2)-1, -1, -1):                          # LOWER HALF

    m = n
    x = int(s / 2)
    for j in range(0, row):                             # Decreasing Part
        print(m, end=" ")
        m -= 1

    for k in range(0, s - 2 *row):                      # Constant Part
        print(n - row, end=" ")

    m = n - row + 1                                      # Increasing Part
    for l in range(0, row):
        print(m, end=" ")
        m += 1

    print()















