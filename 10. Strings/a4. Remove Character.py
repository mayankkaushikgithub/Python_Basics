'''
Remove character

For a given a string(str) and a character X, write a function to remove all the occurrences of X
from the given string.
The input string will remain unchanged if the given character(X) doesn't exist in the input string.

Input Format:
    The first line of input contains a string without any leading and trailing spaces.
    The second line of input contains a character(X) without any leading and trailing spaces.
Output Format:
    The only line of output prints the updated string.

Note:   You are not required to print anything explicitly. It has already been taken care of.
Constraints:    0 <= N <= 10^6      Where N is the length of the input string.
Time Limit: 1 second

Sample Input 1:     aabccbaa                Sample Output 1:    bccb
                    a
Sample Input 2:     xxyyzxx                 Sample Output 2:    xxzxx
                    y
'''

from sys import stdin


def removeAllOccurrencesOfChar(string, ch):

    my_list = list(string)

    res = [i for i in my_list if i != ch]

    string_to_return = ' '.join(str(ele) for ele in res)

    return string_to_return


# Your code goes here


# main
print("Enter a String:")
string = stdin.readline().strip()
print("\nEnter the Character:")
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)