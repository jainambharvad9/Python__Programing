#write py code to print factor of given number 12 = 1,2,3,4,6,12
def factor(n):
           for i in range(1, n +1):
                      if n % i == 0:
                                 print(i)

factor(2000)