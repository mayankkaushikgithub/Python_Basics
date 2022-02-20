# x = 10
# x = "abcd"
# print(x)
#
# a = 10
# id1 = id(a)
# print(id1)
# b = a + 2-2
# id2 = id(b)
# print(id2)
#
# print(17//10)

# a = int(input())
# b=int(input())
# C = a+b
# print(C)

# a = int(input())
# b = int(input())
# c = int(input())
# #avg = (a + b + c)/3
# print((a + b + c)/3)

# for i in range(1,5,2):
#     print(i,end=' ')

# for i in range(5):
#     print(i,end= ' ')

########################################### BREAK ######################################
# i=1
# while i<5:
#     if i==3:
#         break
#     print(i,end=" ")
#     i = i +1

# i=1
# while i<3:
#     j=1
#     while j<5:
#         if j==3:
#             break
#         print(j, end=" ")
#         j = j + 1
#     i = i + 1

################################### BREAK WITH ELSE ####################################
# i=1
# while i<5:
#     if i == 6:
#         break
#     print(i,end=" ")
#     i = i + 1
# else:               # here break is not executed Control will go to 'Else'
#     print("Else is also printed")
#
# i=1
# while i<5:
#     if i == 3:
#         break
#     print(i,end=" ")
#     i = i + 1
# else:               # here break is executed so control will 'not' go to 'Else' and program will end.
#     print("Else is also printed")

############################## CONTINUE #####################################
# i=1
# while i<5:
#     if i==3:
#             continue
#     print(i,end=" ")
#     i = i + 1

# i=1
# while i<3:
#     j=0
#     while j<5:
#         j = j +1
#         if j==3:
#             continue
#         print(j,end=" ")
#     i = i +1

################################# FUNCTIONS ################################

# def func(a):
#     a = a + 10
#     return a
# a = 5
# func(a)
# print(a)

# def square(a):
#     ans  = a*a
#     return  ans
# a = 4
# a = square(a)
# print(a)

# a = 14
# def f():
#     a=12
# f()
# print(a)

# a=14
# def f():
#     global a
#     a=12
# f()
# print(a)

# a = 14
# def f():
#     a = 12
#     return a
# a = f()
# print(a)

# def function(a,b,c=1):
#     return a+b-c
# value = function(10,12)
# print(value)

# def function(a,b,c=1):
#     return a+b-c
# value = function(10,12,5)
# print(value)

# def function(a,b,c=1,d=5):
#     return a+b+c+d
# value = function(1,2,d=7)
# print(value)

############################# LISTS ##############################

# li = ['abcd', 'def']
# li.insert(4,5)
# print(li)

# li = ['abcd', 5, 'def', 5]
# li.remove(5)
# print(li)

# li = [5,2,6,8]
# li.pop(2)       # in pop() we provide index of the element to be removed
# print(li)

# li = [1,2,3,4,5]
# for i in li[1:4]:
#     print(i,end=" ")

# n = int(input())
# li = []
# for i in range(n):
#     li.append(input())
# print(li)

# li = [x for x in input().split()]
# print(li)

####################### Mutable-ImMutable Concept ########################

# def change(li):
#     li[1] = li[1] + 2
# li = [1,2,3,4,5]
# change(li)
# print(li)

# def change(li):
#     li[1] = li[1] + 2
#     li = [3,3,3,4,5]
# li = [1,2,3,4,5]
# change(li)
# print(li)


################################# STRINGS ###############################
# s = "abcd"
# print(s[-2])
#
# s="abcd"
# s[0]='c'
# print(s)

# s ="abcd"
# a = "abcd"
# if id(s) == id(a):
#     print("They are same")
# else:
#     print("They are not same")

# s = "abcd"
# b = s + "ef"
# print(s)

# s = "abcd"
# b = s + 2
# print(b) # will give error, as we can't append integer directly to string

# s = "abcdef"
# print (s[2:])

# s = "abcdef"
# print (s[4:2:-1])


############################################# 2 Dimensional Lists ####################################

# li = [[1,2,3],[4,5,6],[7,8,9]]
# print(li[2][1])
#
# li = [[1,2,3],[4,5,6],[7,8,9]]
# print(li[1][3])
#
# li = [[1,2,3,4],[5,6],[7,8,9]]
# print(li[2])
#
# li = [[1,2,3,4],[5,6],[7,8,9]]
# print(li[1][3])
#
# li = [ele**2 for ele in range(5)]
# print(li)
#
# li = [ele**2 for ele in range(10) if ele%3 ==0]
# print(li)
#
# li = [[ i*j for j in range(4)] for i in range(3)]
# print(li)

############################## Tuples, Dictionary, Sets

# TUPLES

# a = 5,6,7
# print(a[1:])

# a = 5,6,7
# a[2] = 9
# print(a)

# a = 1,2
# b = (4,5)
# d = (a,b)
# print(d[0])

# a = 1,2
# b = (4,5)
# d = (a+b)
# print(d[2])

# a = ("ab","abc","def")
# print(min(a))

# def multiply(a,b,c,*more):
#     value = a*b*c
#     for i in more:
#         value = value * i
#     return value
# V = multiply(1,2,3,4,5)
# print(V)

# def sum_multiply(a,b,*more):
#     sum_value = a+b
#     m_value = a*b
#     for i in more:
#         sum_value += i
#         m_value*=i
#     return sum_value,m_value
# s_m = sum_multiply(2,3,4)
# print(s_m)


# DICTIONARY

# d = {1:2, "abc":5, "def":7}
# print(d[0])

# d = {1:2, "abc":5, "def":7}
# print(d.get(0,5))

# d = {1:2, "abc":5, "def":7}
# if 2 in d:
#     print("Present")
# else:
#     print("Not Present")

# a = {1: 2, 'list': [1, 2], 3: 5}
# b = {4: 5, 3: 7}
# a.update(b)
# print(a[3])

# a = {1:2,'list':[1,2],3:5}
# a.pop('list')
# a['list'] = [3,5]
# print(a['list'])


# SETS

# s = {1, 2, 3, 5, 4, 2, 3, 1}
# print(len(s), end=" ")
# s.add(4)
# s.add(3)
# print(len(s))

# s = {}
# s.add(4)
# s.add(4)
# print(len(s))

j = 4
i = 0
count = j - i + 1
n = count * (count - 1) // 2
print(n)