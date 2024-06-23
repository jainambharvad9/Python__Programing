n = int(input("Enter new Number"))

table = [n*i for i in range (1,11)]
with open("tabel.txt", "a") as f:
    f.write(f"Tale of {n}:{str(table)} \n")