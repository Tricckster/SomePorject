from tkinter import *


root = Tk()
c = Canvas(root,width=400,height=300,bg='grey')
c.pack(side = 'top')
for i in range(10):
    x=3
    y=i*25+3
    c.create_rectangle(x, y, x+40, y+20)

button = Button(root, text="Quit", command=root.destroy)

root.mainloop()