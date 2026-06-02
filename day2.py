from tkinter import *
import math

root = Tk()
root.title("Advanced Calculator")
root.geometry("420x600")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

expression = ""

def press(value):
    global expression

    if value == "^":
        expression += "**"
    else:
        expression += str(value)

    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def square_root():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def percentage():
    global expression
    try:
        result = str(eval(expression) / 100)
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

equation = StringVar()

entry = Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    justify="right",
    bd=10,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew", ipady=15)

buttons = [
    ('C',1,0), ('⌫',1,1), ('%',1,2), ('/',1,3),
    ('7',2,0), ('8',2,1), ('9',2,2), ('*',2,3),
    ('4',3,0), ('5',3,1), ('6',3,2), ('-',3,3),
    ('1',4,0), ('2',4,1), ('3',4,2), ('+',4,3),
    ('√',5,0), ('0',5,1), ('.',5,2), ('^',5,3)
]

for text, row, col in buttons:

    if text == 'C':
        cmd = clear
    elif text == '⌫':
        cmd = backspace
    elif text == '%':
        cmd = percentage
    elif text == '√':
        cmd = square_root
    else:
        cmd = lambda t=text: press(t)

    Button(
        root,
        text=text,
        command=cmd,
        font=("Arial", 16),
        width=6,
        height=2,
        bg="#3a3a3a",
        fg="white",
        activebackground="#505050"
    ).grid(row=row, column=col, padx=2, pady=2)

Button(
    root,
    text="=",
    command=equal,
    font=("Arial", 18, "bold"),
    bg="#ff9500",
    fg="white",
    height=2
).grid(row=6, column=0, columnspan=4, sticky="nsew", padx=2, pady=5)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Keyboard Support
def key_press(event):
    key = event.char

    if key in "0123456789.+-*/":
        press(key)

    elif key == "\r":
        equal()

    elif event.keysym == "BackSpace":
        backspace()

    elif event.keysym == "Escape":
        clear()

root.bind("<Key>", key_press)

root.mainloop()