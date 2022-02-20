'''
Sum or product

Write a program that asks the user for a number N and a choice C.
And then give them the possibility to choose between computing the sum
and computing the product of all integers in the range 1 to N (both inclusive).

If C is equal to -
 1, then print the sum
 2, then print the product
 Any other number, then print '-1' (without the quotes)

Input format :      Line 1 : Integer N          Line 2 : Choice C
Output Format :     Sum or product according to user's choice
Constraints :       <= N <= 12

Sample Input 1 :    10                          Sample Output 1 :   55
                    1

Sample Input 2 :    10                          Sample Output 2 :   3628800
                    2

Sample Input 3 :    10                          Sample Output 3 :   -1
                    4
'''


n = int(input())

c = int(input())

if c == 1:
    sum = 0
    for i in range(n+1):
        sum = sum + i
    print(sum)

elif c == 2:
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    print(prod)

else:
    print(-1)



