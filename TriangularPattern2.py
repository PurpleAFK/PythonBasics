'''
To Print:
    1
    23
    345
    4567
'''
n = int(input())
i = 1
while i<=n:
    k = i
    j = 1
    while j<=i:
        print(k,end="")   # Or u can use the formula i+j-1
        j += 1
        k += 1
    print()
    i+=1





