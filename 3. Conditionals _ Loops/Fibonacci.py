# Member of Fibonacci
#
# You are given a single non-negative integer, N.
# You need to find out whether N is a part of the fibonacci sequence.
# Print "Yes" if it is and "No" if it's not.
# Draw a flowchart for this process
# Note 1: The first two terms of the fibonacci sequence are 0 and 1.


n = int(input("Enter the no. upto which you want series to be printed\n"))

def fibonacci_series(n):
    a = 0
    b = 1
    for i in range(1,n):
        if i <= n:
            a, b = b, a+b
        print(a, end="  ")

series = fibonacci_series(n)

num = int(input("\nEnter the no. you want to search for\n"))
a=0
b=1

while True:
    if num > a:
        a, b = b, a + b
        #break
    else:
        if num == a:
            print("Yes")
            #break
        else:
            print("No")
            #break
        break



