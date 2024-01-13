'''
To print:
    1111
    2222
    3333
    4444
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
       print(i,end="")  #Printed i cuz we are alr looping and can use i to print the numbers 
       j += 1
    print()
    i+=1
