def ls(arr,target):
           for i in range(len(arr)):
                      if arr[i] == target:
                                 return i
                      return -1

mylist = [2,4,6,8,10]
targetele = int(input("Enter Number"))
myele = ls(mylist,targetele)

if(myele != -1):
          print(f"Element {targetele} found at index {myele}.")
else:
    print(f"Element {targetele} not found in the list.")
           
