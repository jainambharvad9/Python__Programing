class Bank:
           
           def __init__(self,p,r,n):
                   self.p = p
                   self.r = r
                   self.n = n 

           def interest(self):
                   i=self.p*self.r*self.n / 100
                   print("simple inter = ",i)
           
           
b1 =  Bank(10000,10,2)
b2 = Bank(20000,12,5)
