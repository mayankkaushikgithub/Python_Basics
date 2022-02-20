
def linear_search(li, ele): # li is the list & 'ele' is the element to be searched

    for index in range(len(li)):
        if li[index] == ele: # if element is found return its 'index'
            return index
    return -1               # else return -1 (no need for this)

    pass

n = int(input("Enter the no. of elements you want to insert in List\n"))
li = []
li = [int(x) for x in input().split()]

ele = int(input("Enter the element you want to search for\n"))

result = linear_search(li, ele)

if result:
    print(f"Index of {ele} is: {result}")
else:
    print("Element is not present")












