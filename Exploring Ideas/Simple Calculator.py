from tkinter import *


root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_plus():
    number1 = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(number1)
    e.delete(0, END)


def button_minus():
    number1 = e.get()
    global f_num
    global math
    math = "minus"
    f_num = int(number1)
    e.delete(0, END)


def button_mult():
    number1 = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(number1)
    e.delete(0, END)


def button_div():
    number1 = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(number1)
    e.delete(0, END)


def button_equal():
    number2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(number2))
    elif math == "minus":
        e.insert(0, f_num - int(number2))
    elif math == "multiply":
        e.insert(0, f_num * int(number2))
    elif math == "divide":
        e.insert(0, f_num / int(number2))



# Create buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_plus = Button(root, text="+", padx=39, pady=20, command=button_plus)
button_minus = Button(root, text="-", padx=40, pady=20, command=button_minus)
button_mult = Button(root, text="*", padx=40, pady=20, command=button_mult)
button_div = Button(root, text="/", padx=40, pady=20, command=button_div)

button_equal = Button(root, text="=", padx=86, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# place buttons
button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_0.grid(row=4, column=0)

button_plus.grid(row=4, column=1)
button_minus.grid(row=4, column=2)
button_mult.grid(row=5, column=0)
button_div.grid(row=6, column=0)

button_equal.grid(row=5, column=1,  columnspan=2)
button_clear.grid(row=6, column=1,  columnspan=2)


root.mainloop()
