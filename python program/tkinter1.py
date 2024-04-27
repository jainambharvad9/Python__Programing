import tkinter as tk
root=tk.Tk()
root.geometry("600x400")

name_var = tk.StringVar()
pass_var = tk.StringVar()
sub_btn = tk.Button(text="submit",width=15)

def submit():
    name = name_var.get()
    password=pass_var.get()
    print(name)
    print(password)
    
    name_var.set(" ")
    pass_var.set(" ")
    
name_lable = tk.Label(root,text="Username")
name_entry = tk.Entry(root,textvariable=name_var)
pass_lable = tk.Label(root,text="Password")
pass_entry = tk.Entry(root,textvariable=pass_var)

name_lable.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_lable.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)

sub_btn.grid(row=2,column=1)
root.mainloop()


