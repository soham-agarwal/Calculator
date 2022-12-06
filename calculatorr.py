from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("500x500")

expression = ""
equation = StringVar()


def clear_button():
    global expression
    expression = ""
    equation.set("")


def num_press(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)
    # e1.set(expression)


def equal():
    try:
        global expression
        ans = str(eval(expression))
        equation.set(ans)
        # e1.set(ans)
    except:
        equation.set("Error")
        # e1.set("Error")


a = u"\u00F7"


def delete():
    global expression
    expression = equation.get()
    expression = expression[:-1]
    equation.set(expression)


b1 = Button(root, text=a, font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press('/')).place(x=290, y=410)

b2 = Button(root, text='x', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press('*')).place(x=290, y=320)

b3 = Button(root, text='+', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press('+')).place(x=290, y=230)

b4 = Button(root, text='-', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press('-')).place(x=290, y=140)

b5 = Button(root, text="1", font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(1)).place(x=0, y=140)

b6 = Button(root, text='2', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(2)).place(x=95, y=140)

b7 = Button(root, text='3', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(3)).place(x=190, y=140)

b8 = Button(root, text='4', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(4)).place(x=0, y=230)

b9 = Button(root, text="5", font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(5)).place(x=95, y=230)

b10 = Button(root, text='6', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(6)).place(x=190, y=230)

b11 = Button(root, text='7', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(7)).place(x=0, y=320)

b12 = Button(root, text='8', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(8)).place(x=95, y=320)

b13 = Button(root, text="9", font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(9)).place(x=190, y=320)

b14 = Button(root, text='0', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press(0)).place(x=95, y=410)

b15 = Button(root, text='.', font=("Calibri", 30, 'bold'), width=4, command=lambda: num_press('.')).place(x=0, y=410)

b16 = Button(root, text='Del', font=("Calibri", 30, 'bold'), width=4, command=delete).place(x=390, y=140)

b17 = Button(root, text="AC", font=("Calibri", 30, 'bold'), width=4, command=clear_button).place(x=390, y=230)

b18 = Button(root, text='=', font=("Calibri", 30, 'bold'), width=4, command=equal).place(x=190, y=410)

e1 = Entry(root, justify=RIGHT, font=("Times New Roman", 50), textvariable=equation).place(x=0, y=20, width=500,
                                                                                           height=90)

root.mainloop()