def fibonacci():
    a,b = 1,0
    while True:
        yield a
        a,b = b , a+b
        
f1  = fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

list1 = [41,32,4,56,34,63,6,34,0,39,20]
n = len(list1)

for i in range(n):
    for  j in range(i+1,n):
        if list1[i]  > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)