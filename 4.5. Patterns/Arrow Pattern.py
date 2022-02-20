################# ARROW PATTERN #################
# Assume N is always odd. # Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# Input format :  # Integer N (Total no. of rows)
# Output format : # Pattern in N lines

n = int(input())

k = int((n+1)/2)
for row in range(1, k+1):
    for space in range(row-1):
        print(" ", end=" ")
    for upper in range(row):
        print("*", end=" ")

    print()

m = int((n-1)/2)
for row in range(m):
    for space in range(m-row,1,-1):
        print(" ", end=" ")
    for lower in range(m-row):
        print("*", end=" ")
    print()

