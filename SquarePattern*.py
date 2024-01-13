'''
To print:
    ****
    ****
    ****
    ****
'''
n=int(input())
i = 1
while i <= n: #This prints j loop n amount of times
    j = 1  # This is necessary since j needs to be reset every time the i loop runs
    while j <= n:  #This prints one line of star
        print("*",end="")
        j += 1
    print()
    i += 1
