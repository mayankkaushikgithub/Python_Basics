n = int(input("Enter the no. of elements you want to enter in list\n"))

li = []
li = [int(x) for x in input().split()]

ele = int(input("Enter the no. you want to search index of\n"))

isFound = False
for index in range(len(li)):
    if ele == li[index]:
        print(f"Index of {ele} is: {index}")
        isFound = True
        break           # if element is found break the loop and give the answer
if isFound is False:
    print("Negative, no. you entered is not present", -1)
















