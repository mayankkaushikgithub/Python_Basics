'''
Trailing zeroes in n!

Find and return number of trailing 0s in n factorial without calculating n factorial.

Sample Input        50
Sample Output       12

Input Size Limit    n < 10^11
'''


n = int(input())

count = 0
i = 5

while n >= 5:   # keep dividing n by powers of 5 and update count

    n = n // 5
    count = count + n

print(count)



