
def reverse_list(li):
    length = len(li)
    for i in range(length//2):
        li[i], li[length-i-1] = li[length-i-1], li[i]
        return li

# def reverse_list(li): # same as above
#     length = len(li)
#     for i in range(length//2):
#         li[i], li[-i-1] = li[-i-1], li[i]
#         return li


n = int(input("Enter the no. of elements you want to insert in List\n"))
li = []
li = [int(x) for x in input().split()]

result = reverse_list(li)

print(result)





