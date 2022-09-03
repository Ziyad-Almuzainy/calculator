import tkinter
from tkinter import *
from tkmacosx import Button

root = Tk()
root.title('Calculator')
root.geometry('387x395+450+150')
root.resizable(False, False)
root.configure(bg='#FFFFFF')

func=''

def show(value):
    global func
    func += value
    ResultLabel.config(text=func)

def Clear():
    global func
    func = ''
    ResultLabel.config(text=func)

def solv():
    global func
    calc = ''
    if func != '':
        try:
            calc = eval(func)
        except:
            calc = 'Math ERROR'
            func = ''
    ResultLabel.config(text=calc)



ResultLabel = Label(root, width=25, height=2, text='',font=('arial',40,), bg='#0A122A', fg='white')
ResultLabel.pack()

clear_button=Button(root, text='AC', width=90, height=50, font=('arial', 30, 'bold'),  fg='#fff', bg='#A52A2A', command= lambda :Clear())
clear_button.place(x=5, y=100)
remainder_button=Button(root, text='%', width=90, height=50, font=('arial', 30, 'bold'),  fg='#fff', bg='#585858', command=lambda :show('%'))
remainder_button.place(x=100, y=100)
Dividing_button= Button(root, text='÷', width=90, height=50, font=('arial', 30, 'bold'),  fg='#fff', bg='#585858', command=lambda :show('/'))
Dividing_button.place(x=195, y=100)


seven_button=Button(root, text='7', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('7'))
seven_button.place(x=5, y=160)
eight_button=Button(root, text='8', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('8'))
eight_button.place(x=100, y=160)
nine_button=Button(root, text='9', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('9'))
nine_button.place(x=195, y=160)
multiplaction_button=Button(root, text='x', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#585858', command=lambda :show('*'))
multiplaction_button.place(x=290, y=100)


four_button=Button(root, text='4', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('4'))
four_button.place(x=5, y=220)
five_button=Button(root, text='5', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('5'))
five_button.place(x=100, y=220)
six_button=Button(root, text='6', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('6'))
six_button.place(x=195, y=220)
Subtraction_button=Button(root, text='-', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#585858', command=lambda :show('-'))
Subtraction_button.place(x=290, y=160)

one_button=Button(root, text='1', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('1'))
one_button.place(x=5, y=280)
two_button=Button(root, text='2', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('2'))
two_button.place(x=100, y=280)
three_button=Button(root, text='3', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('3'))
three_button.place(x=195, y=280)
Addition_button=Button(root, text='+', width=90, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#585858', command=lambda :show('+'))
Addition_button.place(x=290, y=220)


zero_button=Button(root, text='0', width=185, height=50, font=('arial', 30, 'bold'), fg='#fff', bg='#0A122A', command=lambda :show('0'))
zero_button.place(x=5, y=340)
Point_button=Button(root, text='.', width=90, height=50, font=('arial', 30, 'bold'),  fg='#fff', bg='#0A122A', command=lambda :show('.'))
Point_button.place(x=195, y=340)
equal_button=Button(root, text='=', width=90, height=110, font=('arial', 30, 'bold'),  fg='#fff', bg='#FFA500', command=lambda:solv())
equal_button.place(x=290, y=280)



root.mainloop()