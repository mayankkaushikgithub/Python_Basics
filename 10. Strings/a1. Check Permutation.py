'''
Check Permutation

For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Permutations of each other
Two strings are said to be a permutation of each other when either of the string's characters
can be rearranged so that it becomes identical to the other one.

Example:    str1= "sinrtg"      str2 = "string"

The character of the first string(str1) can be rearranged to form str2 and hence we can say that
the given strings are a permutation of each other.

Input Format:
The first line of input contains a string without any leading and trailing spaces,
representing the first string 'str1'.
The second line of input contains a string without any leading and trailing spaces,
representing the second string 'str2'.

Note:   All the characters in the input strings would be in lower case.
Output Format:
The only line of output prints either 'true' or 'false', denoting whether the two strings
are a permutation of each other or not.

You are not required to print anything. It has already been taken care of. Just implement the function.
Constraints:    0 <= N <= 10^6      Where N is the length of the input string.
Time Limit: 1 second

Sample Input 1:     abcde       baedc                               Sample Output 1:    true
Sample Input 2:     abc         cbd                                 Sample Output 2:    false

'''

from sys import stdin


def isPermutation(string1, string2):
    no_of_chars = 256

    # Create an array and initialize all values as 0
    frequency_array = [0]*no_of_chars

    # We can increment the value in count array for characters in str1 and decrement for characters in str2.
    # Finally, if all count values are 0, then the two strings are Permutation of each other.

    # For each character in input string1, increment array in the corresponding count array
    for i in (string1):
        frequency_array[ord(i)] = frequency_array[ord(i)] + 1
        print(i, " ", ord(i))

    # For each character in input string2, decrement array in the corresponding count array
    for i in (string2):
        frequency_array[ord(i)] = frequency_array[ord(i)] - 1
        print(i, " ", ord(i))

    # See if there is any non-zero value in count array
    for i in range(no_of_chars):
        if (frequency_array[i]):
            return False
    return True




# main
print("\nEnter String 1:")
string1 = stdin.readline().strip()

print("\nEnter String 2:")
string2 = stdin.readline().strip()

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')

