''' Python :
 Searching Tech :

1) Sequential (Linear)
2) Binary 

1) Sequential (l)
    a = [10,20,30,40,50]
    find:5
    ans:pos = 3
     
'''
    
    
    
def sequntilasearch(data,find):
    p = 0
    for d in data:
        p=p+1
        if d == find:
            return p 
    return 0

data = [10,20,5,30,45,5,78,90]
print("Found 5 at =",sequntilasearch(data,5))
print("Found 5 at =",sequntilasearch(data,78))