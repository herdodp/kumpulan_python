from tkinter import*

def masukkan():
    display = Text(root, width=50, height=50)
    display.grid(row=1, column=1)
    display.insert(INSERT,inputteks.get())

root = Tk()
root.geometry('500x500')
root.title('insert herdo')
root.resizable(0,0)

inputteks = Entry(root, width=20)
inputteks.grid(row=0, column=1)

button1 = Button(root, text='input', command=masukkan)
button1.grid(row=2, column=1)


root.mainloop()