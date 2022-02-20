# Check Armstrong
#
# Write a Program to determine if the given number is Armstrong number or not.
# Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that the sum of its digits
# raised to nth power is equal to the number itself.
#
# For example:            371, as 3^3 + 7^3 + 1^3 = 371
#                        1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
#
# Input Format :      Integer n
# Output Format :     true or false
#
# Sample Input 1 :    1
# Sample Output 1 :   true
# Sample Input 2 :    103
# Sample Output 2 :   false

def is_armstrong(number):

    order = len(str(number))    # order of number

    sum = 0                     # initialize sum

    temp = number
    while temp > 0:
        digit = temp % 10       # this will give remainder or last digit
        sum += digit ** order
        temp //= 10             # this will give quotient or remaining number

    return (number == sum)      # if condition satisfies

n = int(input("Enter a no. to check if it's Armstrong Number or not:\n"))
result = is_armstrong(n)
if (result):
    print("True")
else:
    print("False")


