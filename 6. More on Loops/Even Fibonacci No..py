'''
Even Fibonacci Numbers

Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N.
Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.

Input Format        Line 1 : An integer N
Output Format       Total Sum

Input Constraints   1 <= N <= 10^6

Sample Input 1:     8                           Sample Output 1 :   10

Sample Input 2:     400                         Sample Output 2:    188
'''






def fibonacci_series(n):

    a = 0
    b = 1
    sum = 0

    while (a < n):

        if (a % 2 == 0):
            sum += a

        a, b = b, a+b

    return sum


n = int(input())

print(fibonacci_series(n))


