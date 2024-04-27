def reverse(n):
           r= 0
           while n >0:
                      a = n % 10
                      r = r * 10 + a
                      n = n // 10

           return r
print(reverse(123))
