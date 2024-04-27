def my_def_x(func):
    def inar_func(x,y):
        print(" i am dividing ",x ,"and",y)
        if y == 0 or x  == 0:
            print("divizon By Zero Is Not Working.....")
            return
        return func(x ,y)
    return inar_func
    
@my_def_x
def go_dividing(x,y):
    return x/y

print(go_dividing(20,2))
print(go_dividing(0,0))


