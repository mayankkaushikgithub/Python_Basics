'''
Remove Consecutive Duplicates

For a given string(str), remove all the consecutive duplicate characters.

Example:    Input String: "aaaa"        Expected Output: "a"

Input String: "aabbbcc"     Expected Output: "abc"
Input Format:
    The first and only line of input contains a string without any leading and trailing spaces.
    All the characters in the string would be in lower case.
Output Format:
    The only line of output prints the updated string.
Note:   You are not required to print anything. It has already been taken care of.
Constraints:    0 <= N <= 10^6      Where N is the length of the input string.
Time Limit: 1 second

Sample Input 1: aabccbaa        Sample Output 1:    abcba
Sample Input 2: xxyyzxx         Sample Output 2:    xyzx
'''

from sys import stdin

# The idea is to keep track of two indexes, index of current character in str and
# index of next distinct character in str.
# Whenever we see same character, we only increment current character index.
# We see different character, we increment index of distinct character.

def removeConsecutiveDuplicates(string):

    i = 0 # index of current character
    j = 0 # index of next distinct character in string

    string = list(string)               # 'str' object does not support item assignment, so first convert it in list

    for i in range(len(string)):        # traversing the string
        if (string[j] != string[i]):    # If current character S[i] is different from S[j]
            j += 1
            string[j] = string[i]

    j += 1
    string = string[0:j]

    list_to_return = ' '.join(str(ele) for ele in string) # convert the list back into string

    return list_to_return





# main
print("Enter the String:")
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)
# print(type(ans))

print(ans)