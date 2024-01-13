def reverselist(li):
    length = len(li)
    for i in range(length//2):
        li[i],li[-i-1] = li[-i-1],li[i]  # You can also swap i with length-i-1

li = [1,2,3,4,5]
reverselist(li)
print(li)


# Or you can just reverse a list in one line SMH
nli = li[::-1]
print(nli)
