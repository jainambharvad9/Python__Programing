import tkinter as tk

W  = tk.Tk()

frm1  = tk.Frame()
frm2 = tk.Frame()

lb1 = tk.Label(master=frm1,text="Frame 1")
lb2 = tk.Label(master=frm2,text="Frame 2")

frm1.pack()
frm2.pack()

lb1.pack()
lb2.pack()

W.mainloop
