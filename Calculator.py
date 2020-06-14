from tkinter import *

r = Tk()
global f_num
global j


def button_add(n):
    c = e.get()
    e.delete(0, END)
    e.insert(0, str(c) + str(n))


def button_comp(m):
    first = e.get()
    global f_num
    global j
    f_num = int(first)
    if m == '+':
        j = 'p'
    elif m == '-':
        j = 'm'
    elif m == '*':
        j = 'mt'
    elif m == '/':
        j = 'd'
    else:
        e.delete(0, END)
    e.delete(0, END)


def button_equal():
    result = 0
    s_num = e.get()
    if j == 'p':
        result = f_num + int(s_num)
    elif j == 'm':
        result = f_num - int(s_num)
    elif j == 'mt':
        result = f_num * int(s_num)
    elif j == 'd':
        result = f_num / int(s_num)
    e.delete(0, END)
    e.insert(0, result)


e = Entry(r, width=50, borderwidth=5)
e.grid(column=0, row=0, columnspan=4, padx=10, pady=10)
one = Button(r, text='1', padx=40, pady=20, command=lambda: button_add('1'))
two = Button(r, text='2', padx=40, pady=20, command=lambda: button_add('2'))
three = Button(r, text='3', padx=40, pady=20, command=lambda: button_add('3'))
four = Button(r, text='4', padx=40, pady=20, command=lambda: button_add('4'))
five = Button(r, text='5', padx=40, pady=20, command=lambda: button_add('5'))
six = Button(r, text='6', padx=40, pady=20, command=lambda: button_add('6'))
seven = Button(r, text='7', padx=40, pady=20, command=lambda: button_add('7'))
eight = Button(r, text='8', padx=40, pady=20, command=lambda: button_add('8'))
nine = Button(r, text='9', padx=40, pady=20, command=lambda: button_add('9'))
zero = Button(r, text='0', padx=40, pady=20, command=lambda: button_add('0'))
plus = Button(r, text='+', padx=40, pady=20, command=lambda: button_comp('+'))
minus = Button(r, text='-', padx=40, pady=20, command=lambda: button_comp('-'))
mult = Button(r, text='*', padx=40, pady=20, command=lambda: button_comp('*'))
div = Button(r, text='/', padx=40, pady=20, command=lambda: button_comp('/'))
equal = Button(r, text='=', padx=40, pady=20, command=lambda: button_equal())
clear = Button(r, text='C', padx=40, pady=20, command=lambda: button_comp('C'))
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
plus.grid(row=1, column=3)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
minus.grid(row=2, column=3)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
mult.grid(row=3, column=3)
div.grid(row=4, column=0)
clear.grid(row=4, column=1)
zero.grid(row=4, column=2)
equal.grid(row=4, column=3)

r.mainloop()
