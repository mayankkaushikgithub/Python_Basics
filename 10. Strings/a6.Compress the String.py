'''
Compress the String

Write a program to do basic string compression.
 For a character which is consecutively repeated more than once,
 replace consecutive duplicate occurrences with the count of repetitions.

Example:    If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

The string is compressed only when the repeated character count is more than 1.
Note :  Consecutive count of every character in the input string is less than or equal to 9.

Input Format:
    The first and only line of input contains a string without any leading and trailing spaces.
Output Format:
    The only line of output prints the updated string.

Note:   You are not required to print anything. It has already been taken care of.
Constraints:    0 <= N <= 10^6      Where N is the length of the input string.
Time Limit: 1 second
Sample Input 1:     aaabbccdsa              Sample Output 1:    a3b2c2dsa
Sample Input 2:     aaabbcddeeeee           Sample Output 2:    a3b2cd2e5
'''

from sys import stdin


def getCompressedString(string):
    encoded_message = ""
    i = 0

    while (i <= len(string) - 1):
        count = 1
        ch = string[i]
        j = i
        while (j < len(string) - 1):
            if (string[j] == string[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + ch + str(count)
        i = j + 1
    return encoded_message


    # res = ""
    # count = 0
    # while (len(string) > 0):
    #     count = 1
    #     res = ""
    #     for j in range(1, len(string)):
    #         if string[0] == string[j]:
    #             count = count + 1
    #         else:
    #             res = res + string[j]
    #     print(string[0], count, end=" ")


# Your code goes here


# main
string = stdin.readline().strip();
ans = getCompressedString(string)

print(ans)