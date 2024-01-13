'''
To Print:
    ABCD
    ABCD
    ABCD
    ABCD

ASCII value is needed 
'''
n = int(input())
# 'A' + j - 1
i = 1
while i <=n:
    j = 1
    while j <= n:
        print(chr(65+j-1),end="")
        j += 1
    print()
    i += 1

