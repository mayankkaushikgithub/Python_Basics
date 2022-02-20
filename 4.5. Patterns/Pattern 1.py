# n = int(input())
# i = 0
# j = 0
# for i in range(n+1):
#     for j in range(i):
#         print('*', end=" ")
#         j = j + 1
#     print()
#     i = i + 1
#
#####################################################

# n = int(input())
# i = 0
# j = 0
# #for i in range(n+1):
# while i<=n:
#     for j in range(i):
#         print(i, end=" ")
#         j = j + 1
#     print()
#     i = i + 1

#####################################################

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 6 5 4 3 2 1

# n = int(input())
# i = 0
# j = 0
# for i in range(n+1):
# #while i<=n:
#     for j in range(i):
#         print(i, end=" ")
#         j = j + 1
#         i = i - 1
#     print()
#     i = i + 1

#####################################################
'''
@ A B C D E F
@ A B C D E F
@ A B C D E F
@ A B C D E F
@ A B C D E F
@ A B C D E F
@ A B C D E F
@ A B C D E F
'''
n = int(input())
i = 1
j = 0
for i in range(n+1):
    for j in range(n):
        charP = chr(ord('A') + j)
        # charP = chr(ord('A') + j - 1)
        #ord() gives the ASCII value of Character #chr() gives the character of corresponding ASCII value.
        print(charP, end=" ")
    print()

###############################################################################
# A
# B C
# C D E
# D E F G
# E F G H I
# F G H I J K

# n = int(input())
# for row in range(n):
#     k = ord('A') + row
#     for column in range(row+1):
#         #ord() gives the ASCII value of Character #chr() gives the character of corresponding ASCII value.
#         print(chr(k), end=" ")
#         k = k + 1
#     print()

###############################################################################

# E
# D E
# C D E
# B C D E
# A B C D E

# n = int(input())
# for row in range(n):
#     k = ord('A') - row
#     for column in range(row+1):
#         print(chr(k+n-1), end=" ")
#         k = k + 1
#     print()

########################################################################

# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1 1
#
# n = int(input())
# i = 1
# for row in range(n):
#     for column in range(row+1):
#         print(i, end=" ")
#     print()

#######################################################################
'''
1
1 1
2 0 2
3 0 0 3
4 0 0 0 4
5 0 0 0 0 5
'''

# n = int(input())
# row = 1
# for row in range(n):
#     for column in range(row+1):
#         if row == 0 and column == 0:
#             print(1, end="")
#         elif column == 0 or column == row :
#             print(row, end=" ")
#         else:
#             print(0, end=" ")
#     print()

########################################################################

# 1
# 1 1
# 1 2 1
# 1 2 2 1
# 1 2 2 2 1
# 1 2 2 2 2 1

# n = int(input())
# row = 1
# for row in range(n):
#     for column in range(row+1):
#         if row == 0 and column == 0:
#             print(1, end=" ")
#         elif column == 0 or column == row:
#             print(1, end =" ")
#         else:
#             print(2, end=" ")
#     print()
#
###################################################################################

# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
#
# n = int(input())
# for row in range(n, 0, -1):
#     for column in range(1, row+1):
#         print(column, end=" ")
#     print()

############################################################################

# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
#
# n = int(input())
# k = ord('A')
#
# for row in range(n):
#     for column in range(row+1):
#         print(chr(k), end=" ")
#     k = k + 1
#     print()



