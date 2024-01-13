'''
To Print:
    1
    23
    456
    78910
'''
n = int(input())
i = 1
k = i
while i<=n:
    j = 1
    while j<=i:
        print(k,end="")           
        j += 1
        k += 1
    print()
    i+=1
