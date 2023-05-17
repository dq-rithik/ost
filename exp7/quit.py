from tkinter import *
  
root = Tk()
a = Button(root,text='quit',command=root.destroy,font=('Times',24))
a.pack(expand=True)
root.geometry("500x500")
root.mainloop()