from tkinter import *
from math import *
from random import random



page = Tk()
page.title('calculator')

a = ''
oparation = ''
text_input = StringVar()
Operators = ['+', '-','*','/','(',')','sin(','cos(','tan(','.','sqrt(','**']

def clickbtn(number):
    global oparation, a
    if a == 'equal' and number not in Operators:
        clearbtn()
    oparation = oparation + str(number)
    text_input.set(oparation)
    a = ''


def clearbtn():
    global oparation, a
    oparation = ''
    text_input.set('')
    a = ''

def equalsbtn():
    global oparation, a
    result = str(eval(oparation))
    text_input.set(result)
    oparation = result
    a = 'equal'


foreground_color_numbers = '#FFFA4D'
foreground_color = '#00ADB5'
background_color = '#222831'
monitor_bg = '#393E46'
monitor_fg = '#EEEEEE'


textdisplay = Entry(page, textvariable = text_input, font = ('Digital-7 Mono', 20, 'bold'),
bd = 30, bg = monitor_bg, width = 27 ,fg = monitor_fg, justify = 'right').grid(columnspan = 5)

Btn7 = Button(page, text = 7, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(7)).grid(row = 1, column = 0)

Btn8 = Button(page, text = 8, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(8)).grid(row = 1, column = 1)

Btn9 = Button(page, text = 9, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(9)).grid(row = 1, column = 2)

addition = Button(page, text = '+', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('+')).grid(row = 1, column = 3)

Btn4 = Button(page, text = 4, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(4)).grid(row = 2, column = 0)

Btn5 = Button(page, text = 5, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(5)).grid(row = 2, column = 1)

Btn6 = Button(page, text = 6, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(6)).grid(row = 2, column = 2)

subtraction = Button(page, text = '-', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('-')).grid(row = 2, column = 3)

Btn1 = Button(page, text = 1, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(1)).grid(row = 3, column = 0)

Btn2 = Button(page, text = 2, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(2)).grid(row = 3, column = 1)

Btn3 = Button(page, text = 3, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(3)).grid(row = 3, column = 2)

Multiplication  = Button(page, text = '×', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('*')).grid(row = 3, column = 3)

Btn0 = Button(page, text = 0, font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color_numbers, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(0)).grid(row = 4, column = 0)

BtnC = Button(page, text = 'C', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clearbtn()).grid(row = 4, column = 1)

Equal = Button(page, text = '=', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: equalsbtn()).grid(row = 4, column = 2)

Division = Button(page, text = '÷', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('/')).grid(row = 4, column = 3)

parantez_baz = Button(page, text = '(', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('(')).grid(row = 5, column = 0)

parantez_baste = Button(page, text = ')', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn(')')).grid(row = 5, column = 1)

sinus = Button(page, text = 'sin', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('sin(')).grid(row = 1, column = 4)

cosinus = Button(page, text = 'cos', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('cos(')).grid(row = 2, column = 4)

tangent = Button(page, text = 'tan', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('tan(')).grid(row = 3, column = 4)

point = Button(page, text = '.', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('.')).grid(row = 5, column = 2)

radical = Button(page, text = '√', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('sqrt(')).grid(row = 4, column = 4)

power = Button(page, text = '  y\nx', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('**')).grid(row = 5, column = 3)

logaritm = Button(page, text = 'log10', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('log10(')).grid(row = 5, column = 4)

Ln = Button(page, text = 'Ln', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('log(')).grid(row = 6, column = 0)

Pi = Button(page, text = 'π', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('pi')).grid(row = 6, column = 1)

e = Button(page, text = 'e', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('2.7182818284')).grid(row = 6, column = 2)

exponention = Button(page, text = '  x\ne', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('exp(')).grid(row = 6, column = 3)

Rand = Button(page, text = 'Ran', font = ('Digital-7 Mono', 20, 'bold'), bd = 10, bg = background_color,
 fg = foreground_color, padx = 16, pady = 16, height = 1, width = 2, command = lambda: clickbtn('random()')).grid(row = 6, column = 4)

page.resizable(width = False, height = False)
page.mainloop()