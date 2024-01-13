#Linear Search Function
def linearSearch(li,ele):
    # li is the list and ele is the element to be searched
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return -1


li = [1,2,3,4,5]
i = linearSearch(li,3)
print(i)
