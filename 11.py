from tkinter import *


root = Tk()
c = Canvas(root,width=400,height=500,bg='grey')
c.pack(side = 'top')


for i in range(5):
    for j in range(10):
        x=3+45*j
        y=i*25+3
        c.create_rectangle(x, y, x+40, y+20,fill='red')

c.create_rectangle(150, 300, 250, 350,fill='blue')

button = Button(root, text="Quit", command=root.destroy)


root.mainloop()
