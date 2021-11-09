from tkinter import *
import random

b=[]
bricks = []
root = Tk()
c = Canvas(root,width=1600,height=900,bg='blue')
c.pack(side = 'top')

for i in range(6):
    for k in range(20):
        random.shuffle(BRICK_COLOR)
        #сделать важную вещь, создать функцию на создание кирпичиков
        b.append(z)
    bricks.append(b)
button = Button(root, text="Quit", command=root.destroy)

root.mainloop()