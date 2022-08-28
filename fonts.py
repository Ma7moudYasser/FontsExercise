from tkinter import *
pro = Tk()
pro.geometry('500x500')

lbl1 = Label(pro,text = 'Learn python 2020', font= ('Times New Roman',12,'underline'))
lbl1.pack()

lbl2 = Label(pro, text = 'Learn python 2021', font = ('Helvetica', 12, 'bold'))
lbl2.pack()

lbl3 = Label(pro, text = 'Learn python 2022', font = ('Impact',12 , 'italic'))
lbl3.pack()
pro.mainloop()
