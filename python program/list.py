#list
#declear with []
#list is collection of data
#EXp
a= [10,20,30,40,50]
print(a)
print(a[2:])
print(a[2:4])
for i in a:
           print(i)
b = [10,100.23,"welcome",True]

for i in b:
           print(i)

print(list(enumerate(a)))
t1 = tuple(a)
print(t1)


#print (int(t1.__add__(20)))