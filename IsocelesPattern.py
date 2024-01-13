'''
To Print:
        1
       121
      12321
     1234321
'''
'''
STEP PROCESS
first print only the inverse triangle
created another loop after to print a smaller triangle
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    while j <= n-i:
        print(" ",end="")
        j += 1
    k = 1
    while k <= i:
        print(k, end="")
        k += 1
    l = 2
    while l <= i:
        print(i-l+1, end="")
        l += 1
    print()
    i += 1

