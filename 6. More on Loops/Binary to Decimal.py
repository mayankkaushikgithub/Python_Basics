'''
Binary to decimal

Given a binary number as an integer N, convert it into decimal and print.

Input format :      An integer N in the Binary Format
Output format :     Corresponding Decimal number (as integer)

Constraints :       0 <= N <= 10^9

Sample Input 1 :    1100            Sample Output 1 :   12

Sample Input 2 :    111             Sample Output 2 :   7
'''

num = int(input())

ans = 0
pv = 1

while num > 0:

    last_digit = num % 10

    ans = ans + (pv * last_digit)

    pv *= 2

    num = num // 10

print(ans)








