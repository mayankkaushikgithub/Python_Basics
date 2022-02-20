# Array Sum
#
# Given an array of length N, you need to find and print the sum of all elements of the array.
#
# Input Format :      Line 1 : An Integer N i.e. size of array
#                     Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :     Sum
# Constraints :       1 <= N <= 10^6

# Sample Input :      3
#                     9 8 9
# Sample Output :     26


n = int(input("Enter the Size of Array\n"))
li = []                                     # create an empty list
li = [int(x) for x in input().split()]      # convert each element of array(from string to int)
print("The Elements in List are\n",li)      # and store inside the list

sum = 0
for item in li:
    sum = sum + item
print("Sum of Elements is:", sum)












