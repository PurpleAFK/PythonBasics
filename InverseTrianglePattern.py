'''
To Print:
       *
      **
     ***
    ****
'''
# First we need to print the spaces and then the stars
# So you are basically printing a square with spaces and stars
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ",end="")
        j += 1
    k = 1
    while k <= i:
        print("*",end="")
        k += 1
    print()
    i += 1
