'''
To print:
    4321
    4321
    4321
    4321
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    r = n  #Either this way or we can just print (n-j+1)
    while j <= n:
        print(r,end="")
        r -= 1
        j += 1
    print()
    i += 1
        
