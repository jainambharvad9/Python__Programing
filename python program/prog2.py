''' 
1) Bimary 


'''

def binearysearch(data,find):
    
    low = 0 
    high = len(data) - 1
    while low <= high:
        mid = (low+high)//2
        
        if data[mid] > find:
            high = mid-1
        elif data[mid] < find:
            low = mid+1
        else:
            return mid+1
        
    return 0
data = [10,20,30,40,50,60,70]
find = 50 
pos = binearysearch(data,find)
text = "data {} found {} pos {}"       

print(text.format(data,find,pos))