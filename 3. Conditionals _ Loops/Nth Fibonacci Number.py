# Nth Fibonacci Number
#
# Nth term of Fibonacci series F(n) is calculated using the following formula -
#     F(n) = F(n-1) + F(n-2),
#     Where, F(1) = F(2) = 1
# Provided N you have to find out the Nth Fibonacci Number.

# Input Format :    # The first line of each test case contains a real number ‘N’.
# Output Format :   # For each test case, return its equivalent Fibonacci number.
# Constraints:      # 1 <= N <= 10000
# Where ‘N’ represents the number for which we have to find its equivalent Fibonacci number.
#
# Time Limit: 1 second
# Sample Input 1:   # 6
# Sample Output 1:  # 8
# Explanation of Sample Input 1:
# Now the number is ‘6’ so we have to find the “6th” Fibonacci number
# So by using the property of the Fibonacci series i.e
#
# [ 1, 1, 2, 3, 5, 8]
# So the “6th” element is “8” hence we get the output.


n = int(input("Enter the no. up to which you want series to be printed\n"))

def fibonacci_series(n):
    a = 0
    b = 1
    for i in range(1,n):
        a, b = b, a+b
        print(a, end="  ")

series = fibonacci_series(n)
# print(type(series))


def checkMember(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return checkMember(n-1) + checkMember(n-2)


num = int(input("\nEnter the no. you want to search for\n"))
checkMember(num)
if(checkMember(n)):
    print("True! It exist")
else:
    print("False! It doesn't exist")