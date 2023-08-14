from tkinter import *
from tkinter.ttk import *

def press_button(num):
    global test_equation
    test_equation += str(num)
    test_equation_label.set(test_equation)


def clear_all():
    global test_equation
    test_equation_label.set("")
    test_equation = ""

def backspace():
    global test_equation
    test_equation = test_equation[:-1]
    test_equation_label.set(test_equation)


def equals_to():
    global test_equation
    try:
        total = str(eval(test_equation))
        test_equation_label.set(total)
        test_equation = total

    except ZeroDivisionError:
        test_equation_label.set("Arthmetic Error")

    except SyntaxError:
        test_equation_label.set("Syntax Error")


window = Tk()
window.title("Calculator")
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

window.configure(background='white')
window.resizable(width=True, height=True)

test_equation = ""
test_equation_label = StringVar()

label = Label(window,textvariable=test_equation_label,font="arial",
              foreground='green',
              background='black',
              borderwidth=10,
              relief= SUNKEN, #border style
              )

label.grid(row=0, columnspan=4, sticky= W + E)

AC_button = Button(window, text="AC", width=10, command= clear_all )
AC_button.grid(row=1, columnspan=2,sticky= W + E)

button_mod = Button(window, text="%", width=10, command=lambda : press_button('%'))
button_mod.grid(row=1, column=2)

button_div = Button(window, text="/", width=10, command=lambda : press_button('/'))
button_div.grid(row=1, column=3)

num7_button = Button(window, text="7", width=10, command=lambda : press_button('7'))
num7_button.grid(row=2, column=0)

num8_button = Button(window, text="8", width=10, command=lambda : press_button('8'))
num8_button.grid(row=2, column=1)

num9_button = Button(window, text="9", width=10, command=lambda : press_button('9'))
num9_button.grid(row=2, column=2)

button_mul = Button(window, text="*", width=10, command=lambda : press_button('*'))
button_mul.grid(row=2, column=3)

num4_button = Button(window, text="4", width=10, command=lambda : press_button('4'))
num4_button.grid(row=3, column=0)

num5_button = Button(window, text="5", width=10, command=lambda : press_button('5'))
num5_button.grid(row=3, column=1)

num6_button = Button(window, text="6", width=10, command=lambda : press_button('6'))
num6_button.grid(row=3, column=2)

button_sub = Button(window, text="-", width=10, command=lambda : press_button('-'))
button_sub.grid(row=3, column=3)

num1_button = Button(window, text="1", width=10, command=lambda : press_button('1'))
num1_button.grid(row=4, column=0)

num2_button = Button(window, text="2", width=10, command=lambda : press_button('2'))
num2_button.grid(row=4, column=1)

num3_button = Button(window, text="3", width=10, command=lambda : press_button('3'))
num3_button.grid(row=4, column=2)

button_add = Button(window, text="+", width=10, command=lambda : press_button('+'))
button_add.grid(row=4, column=3)

num0_button = Button(window, text="0", width=10, command=lambda : press_button('0'))
num0_button.grid(row=5, columnspan=2, sticky= W + E)

button_dot = Button(window, text=".", width=10, command=lambda : press_button('.'))
button_dot.grid(row=5, column=2)

button_equal_to = Button(window, text="=", width=10, command=equals_to)
button_equal_to.grid(row=5, column=3,)

backspace = Button(window,text = "Backspace",width= 10,command = backspace)
backspace.grid(row = 6,columnspan=4,sticky= W+E)

window.mainloop()


