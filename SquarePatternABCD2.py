'''
To Print:
    ABCD
    BCDE
    CDEF
    DEFG
ASCII value is needed 
'''
n = int(input())
i = 1
k = 0
while i <=n:
    j = 1
    while j <= n:
        print(chr(65+j-1+k),end="")
        j += 1
    print()
    i += 1
    k += 1

'''
Alternative method
start_char = chr(odr('A') + i - 1)
charP = chr(odr(start_char) + j - 1)
'''
