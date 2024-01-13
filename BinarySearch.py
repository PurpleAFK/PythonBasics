# It is necessary that the given array is sorted

def binarysearch(arr,element):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if (arr[mid] == element):
            return mid
        elif(arr[mid] < element):
            start = mid + 1
        else:
            end = mid - 1
    return -1;
 
arr = [0,1,2,3,4,5,6,7,8,9,10]
n = int(input())
index = binarysearch(arr,n)
print(index)
