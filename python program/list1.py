


class List:
	def __init__(self):self.item=[]
     
	def length(self):return(self.item)
	def get(self,pos):
		if pos >= 0 and pos < self.length()-1:return self.item[pos]
	
	def insert(self,value,pos):
		self.item.insert(pos,value)

	def delete(self,pos): 
     d = self.item.pop(pos)
     print("poped item = ",d)
	
	def replace(self,pos,newval):
		self.item[pos] = newval
	def isEmpty(self):
		if len(self.item) > 0:
			return False
		else:
			return True

	def show(self):
		c = self.length()
		for i in range(0,c):
			print(self.item[i])

s  = List()
while True:
    print("1 .Inser")
    print("2 .Delete")
    print("3 .isEmpty")
    print("4 .Length")
    print("5 .Show")
    print("6 .Replace")
    print("7 .Get")
    print("8 .Exit")
    ch = int(input("enter your choice:"))
    
    if ch==1:
        value = int(input("Enter Value")); pos=int(input("Enter Pos"))
        
    elif ch==2:
        pos = int(input("Enter Pos")); s.delete(pos)
        
    elif ch==3:
        print(" ",s.isEmpty())
        
    elif ch==4:
        print(s.length())
        
    elif ch==5:
        s.show()
        
    elif ch==6:
        newval = int(input("Enter Val")); pos = int(input("Enter Pos")); s.replace(pos,newval)
        
    elif ch==7:
        pos = int(input("Enter Pos")); print(s.get(pos))
        
    else:
        break
  
  