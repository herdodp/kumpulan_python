from tkinter import *

def activateMotors():
    if motorsOn.get() == 1:
        scale.config(state=ACTIVE)
    elif motorsOn.get() == 0:
        scale.config(state=DISABLED)


root = Tk()
root.wm_title('Servo Control')
motorsOn= IntVar()
motorsCheck=Checkbutton(root, 
    text="Motors ON(checked)/OFF(unchecked)", 
    variable=motorsOn, 
    command=activateMotors)
motorsCheck.pack()

scale = Scale(root, from_=0, to=180, 
              orient=HORIZONTAL,label="Motor #",state=DISABLED)
scale.pack()
root.mainloop()