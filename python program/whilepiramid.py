n = int(input("Enter Odd Number Only..!!!"))
m = (n+1)/2

i = 1 

while i <= n:
    if i > m:
        b  = n - i 
        s  = 2*(i-m)+1
    else:
        b = i - 1
        s = 2*(m-i)+1
    
    j = 1
    while j <= b:
        print(".", end="")
        j = j + 1
    j = 1
    while j <= s:
        print("*",end="")
        j = j + 1
    print( )
    i = i + 1