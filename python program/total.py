class student:
           def __init__(self,m1,m2,m3):
                      self.m1 = m1
                      self.m2 = m2
                      self.m3 = m3

           def showresult(self):
                      total = self.m1+self.m2+self.m3
                      per = total/3
                      print("total is = ",total)
                      print(" per is =",per)

s1 = student(60,50,70)

s1.showresult()
           
