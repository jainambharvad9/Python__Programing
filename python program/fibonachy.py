import fibonachi


def fib_seq(n):
    A = 0 
    B = 1
    if n==1:
        print(A)
    elif n ==2:
        print(A,B)

    else:
        print(A,B,end="  ")
        c = A + A
        A=B
        B=c
        print(c,end=" ")

fib_seq(10)