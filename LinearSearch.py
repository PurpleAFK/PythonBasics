'''
Seach thru a list to see if its present and
   if it is ---> return the element
   if it is not ---> return -1
'''
n = int(input())
li = [int (x) for x in input().split(" ")]
ele = int(input("Enter the element to search: "))
isFound = False
for i in range(len(li)):
    if li[i] == ele:
        print(i)
        isFound = True
        break
if isFound != True:
    print(-1)

