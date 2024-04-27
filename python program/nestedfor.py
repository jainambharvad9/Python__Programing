

# for i in range(10,0,-1):
#      for j in range(0,i):
#         print("*" ,end=" ")
#      print()

    

# k = 0

# for i in range(1, 6+1):
#     for space in range(1, (6-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
   
#     k = 0
#     print()
            
            
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()


    
# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
         
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()