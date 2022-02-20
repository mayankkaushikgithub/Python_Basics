'''
Decimal to Binary

Given a decimal number (integer N), convert it into binary and print.
The binary number should be in the form of an integer.

Input format :      Integer N
Output format :     Corresponding Binary number (long)

Constraints :       0 <= N <= 10^5

Sample Input 1 :    12                              Sample Output 1 :   1100

Sample Input 2 :    7                               Sample Output 2 :   111
'''


num = int(input())

ans = 0     # stores the final answer (reversed binary no.)
pv = 1      # stores the place value of every remainder

while (num != 0):

    rem = num % 2
    # print(rem, end=" ")

    ans = ans + (rem * pv) # reversing digits by multiplying them with their place value

    num = num // 2          # update num (go to next quotient)

    pv = pv * 10            # update pv unit -> tens -> so on

print(ans, end="")



