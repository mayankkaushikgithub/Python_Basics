'''
First non repeating character

In a given string, find the first non-repeating character .You are given a string, that can contain repeating characters.
Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once.
The string will contain characters only from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z').
If there is no non-repeating character print the first character of string.

Input Format :      Line 1 : A String , as mentioned above.
Output Format :     First non-repeating character

Sample Input 1 :    aDcadhc                 Sample Output 1:    D

Sample Input 2 :    gdhIgHada               Sample Output 2 :   h
'''

def getCharCount(string):

    noOfChars = 256
    count = [0]*noOfChars

    for i in string:
        count[ord(i)] += 1
    return count

def nonRepeatingChar(string):

    count = getCharCount(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index






# Main
string = input()
index = nonRepeatingChar(string)

print(string[index])
