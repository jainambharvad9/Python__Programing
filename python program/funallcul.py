def funsum(x,y):
    print("geting Sum....")
    return(x+y)

def funsub(x,y):
    print("geting Sub....")
    return(x-y)

def funmul(x,y):
    print("geting mul...")
    return(x*y)

def fundiv(x,y):
    print("geting Div....")
    return(x/y)

def funmod(x,y):
    print("geting Mod....")
    return(x%y)

def mymenu():
    print("My Menu...")
    
    print("1 > Choice Sum...")
    
    print("2 > Choice Sub...")
    
    print("3 > Choice mul...")
    
    print("4 > Choice Div...")
    
    print("5 > Choice Mod...")
    
    choice = int(input("Enter Your Choice..."))
    
    return choice

def cal():
    ch = mymenu()
    
    num1 = int(input("input Your Number 1..."))
    num2 = int(input("Imput Your Number 2..."))
    
    if ch == 1:
        result = funsum(num1,num2)
        
    elif ch == 2:
        result = funsub(num1,num2)
        
    elif ch == 3:
        result = funmul(num1,num2)
        
    elif ch == 4:
        result = fundiv(num1,num2)
        
    elif ch == 5:
        result = funmod(num1,num2)
        
    print(result)

cal()