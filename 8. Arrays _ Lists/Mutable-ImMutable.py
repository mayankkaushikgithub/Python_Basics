####################### Mutable-ImMutable Concept ########################

def change(li):
    li[1] = li[1] + 2
li = [1,2,3,4,5]
change(li)
print(li)

def change(li):
    li[1] = li[1] + 2
    li = [3,3,3,4,5]
li = [1,2,3,4,5]
change(li)
print(li)