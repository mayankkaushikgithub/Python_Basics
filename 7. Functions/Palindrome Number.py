# Palindrome number

# Write a program to determine if given number is palindrome or not.
# Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

# Sample Input 1 :    121
# Sample Output 1 :   true
# Sample Input 2 :    1032
# Sample Output 2 :   false


def checkPalindrome(n):
    # Implement Your Code Here
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    if num == rev:
        return True
    else:
        return False


num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome):
    print('true')
else:
    print('false')
