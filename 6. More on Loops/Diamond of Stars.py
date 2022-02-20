# Diamond of Stars
# Print the following pattern for the given number of rows.

# Sample Input 1:   # 5
# Sample Output 1:  #   *
                    #  ***
                    # *****
                    #  ***
                    #   *

# Input format :    # N (Total no. of rows and can only be odd)
# Output format :   # Pattern in N lines
# Constraints :     # 1 <= N <= 49

n = int(input())

m = int((n+1)/2)
for row in range(0, n, 2):
    print(" "*(n-row-1) + "*"*(row+1))

# k = int((n-1)/2)
# for column in range(n-1, 0, -2):
#     print(" "*(n-column) + "*"*(column-1))






