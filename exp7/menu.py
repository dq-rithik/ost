from tkinter import *
  
root = Tk()

def onclick():
    c = Button(root, text='quit', command=root.destroy)
    c.grid(row=1, column=0)
b = Button(root, text='clickme', command=onclick)
b.grid(row=0, column=0)
root.geometry("500x500")
root.mainloop()