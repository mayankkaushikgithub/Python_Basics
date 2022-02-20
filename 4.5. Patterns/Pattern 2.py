# * * * * *
# * * * *
# * * *
# * *
# *
#
# n = int(input())
# for row in range(n,0,-1):
#     for column in range(row):
#         print("*", end=" ")
#     print()

############################################

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
#
# n = int(input())
# for row in range(n,0,-1):
#     for column in range(row):
#         print(n, end=" ")
#     n = n - 1
#     print()

##############################################
#
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
# * * * * * *
#
# n = int(input())
# for row in range(n):
#
#     for space in range(n-row): #for printing spaces
#         print(" ", end=" ")
#
#     for column in range(row+1):
#         print("*", end=" ")
#     print()
#----------------------------------------------------

'''
        *
      * * *
    * * * * *
  * * * * * * *
'''

# n = int(input())
# for row in range(n):
#
#     for space in range(n-row-1): #for printing spaces
#         print(" ", end="")
#
#     for column in range(2*row+1):
#         print("*", end="")
#     print()

#######################################################

#     1
#    12
#   123
#  1234
# 12345

# n = int(input())
# for row in range(1,n):
#
#     for space in range(n-row): # for printing spaces
#         print(" ", end="")
#
#     for column in range(1,row+1):
#         print(column, end="")
#     print()

######################################################

''' PYRAMID OF NUMBERS 1
          1
        1 2 1
      1 2 3 2 1
    1 2 3 4 3 2 1
  1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1

'''
# n = int(input())
# for row in range(n):
#
#     # for printing spaces
#     for space in range(n-row-1):
#         print(" ", end=" ")
#
#     # for increasing column
#     for inc_column in range(0,row+1):
#         print(inc_column+1, end=" ")
#
#     # for decreasing column
#     for dec_column in range(row, 0, -1):
#         print(dec_column, end=" ")
#         dec_column = dec_column - 1
#     print()
#
############################################################

##### PYRAMID OF STARS #####
#
# n = int(input())
#
# for row in range(n):
#
#     for space in range (n-row-1):
#         print(" ", end="")
#
#     for inc_column in range(row+1):
#         print("*",end="")
#
#     for dec_column in range(row, 0, -1):
#         print("*", end="")
#
#     print()

################################################################
#
''' PYRAMID OF NUMBERS 2 
          1 
        2 3 2 
      3 4 5 4 3 
    4 5 6 7 6 5 4 
  5 6 7 8 9 8 7 6 5 
6 7 8 9 10 11 10 9 8 7 6 
'''
# n = int(input())
# for row in range(n):
#
#     # for printing spaces
#     for space in range(n-row-1):
#         print(" ", end=" ")
#
#     # for increasing column
#     for inc_column in range(0,row+1):
#         print(row+1, end=" ")
#         row = row + 1
#
#
#     # for decreasing column
#     for dec_column in range(row, 1, -2):
#         print(row-1, end=" ")
#         row = row - 1
#
#     print()

######################################################

##### DIAMOND OF STARS (Method-1) #####
#
# n = int(input())
#
# for row in range(0, n, 1):
#
#     # for printing spaces
#     for up_space in range(n - row - 1):
#         print(" ", end=" ")
#
#     # for increasing column
#     for inc_column in range(0, row+1, 1):
#         print("*", end=" ")
#
#     for dec_column in range(row, 0, -1):
#         print("*", end=" ")
#
#     print()
#
# for row in range(n-1, 0, -1):
#
#     for down_space in range(0, n-row):
#         print(" ", end=" ")
#
#     for down_inc_col in range(0, row):
#         print("*", end=" ")
#
#     for down_dec_col in range(row-1, 0, -1):
#         print("*", end=" ")
#
#     print()

########################################################################

##### DIAMOND OF STARS (Method-2) #####

# def pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1) + '* '*(i+1))
#
#     for j in range(rows-1, 0, -1):
#         print(' '*(rows-j) + '* '*(j))
#
# n = int(input())
# pyramid(n)

###########################################################################

##### DIAMOND OF STARS (Method-2) #####

# n = int(input())
#
# for row in range(0, n-1, 2):
#     # print(row) # for n = 10 -> row = 0, 2, 4, 6, 8
#
#     # for printing spaces
#     for space in range(n - row - 1):
#         print(" ", end="")
#
#     # for increasing column
#     for column in range(0, row+1, 1):
#         print("*", end="")
#
#     print()
#
# for row in range(n, 0, -2):
#     # print(row) # for n = 10 -> row = 8, 6, 4, 2, 0
#
#     for down_space in range(0, n-row-1):
#         print(" ", end="")
#
#     for down_inc_col in range(0, row):
#         print("*", end="")
#
#     print()

#################################################################












