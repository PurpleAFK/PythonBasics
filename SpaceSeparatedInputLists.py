from re import split

n = input() 
list1 = []

# We have to use the split function
# This will make a list but there wont be any numbers but there will be strings of the numbers
splitn = n.split(" ") 

for i in splitn:
    list1.append(int(i))
print(list1)


# You can also do this in one line
li = [int(x) for x in input().split()]
print(li)

