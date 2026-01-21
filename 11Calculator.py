from tkinter import*
result = ''

def clear():
    global result
    result = ""
    equation.set("")


def equalpress():
    try:
        global result
        total = str(eval(result))
        equation.set(total)
        result=""
    except:
        equation.set('error')
        result = ""


window = Tk()
window.title('Calculator Python Project Created by JP')
window.geometry('300x200')
window.configure(bg='light gray')
window.resizable(False, False)
equation = StringVar()
btn= Button(window,text = '1', width = 6, height=2, fg='blue',font=('Times', 10), command=lambda: press(1))
btn.grid(row=1,column=0)
btn2= Button(window,text = '4', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(4))
btn2.grid(row=2,column=0)
btn3= Button(window,text = '7', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(7))
btn3.grid(row=3,column=0)
btn4= Button(window,text = '0', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(0))
btn4.grid(row=6,column=0)
btn5= Button(window,text = '.', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("."))
btn5.grid(row=6,column=3)
btn6= Button(window,text = '2', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(2))
btn6.grid(row=1,column=1)
btn7= Button(window,text = '5', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(5))
btn7.grid(row=2,column=1)
btn8= Button(window,text = '8', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(8))
btn8.grid(row=3,column=1)
btn9= Button(window,text = 'Clear', width = 6, height=2, fg='blue',font=('Times', 10),command=clear)
btn9.grid(row=6,column=1)
btn10= Button(window,text = '3', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(3))
btn10.grid(row=1,column=2)
btn11= Button(window,text = '6', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(6))
btn11.grid(row=2,column=2)
btn12= Button(window,text = '9', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(9))
btn12.grid(row=3,column=2)
btn13= Button(window,text = '=', width = 6, height=2, fg='blue',font=('Times', 10),command=equalpress)
btn13.grid(row=6,column=2)
btn14= Button(window,text = '+', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("+"))
btn14.grid(row=1,column=3)
btn15= Button(window,text = '-', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("-"))
btn15.grid(row=2,column=3)
btn16= Button(window,text = '*', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("*"))
btn16.grid(row=3,column=3)
btn17= Button(window,text = '/', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("/"))
btn17.grid(row=6,column=3)
btn18= Button(window,text = '(', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("("))
btn18.grid(row=1,column=4)
btn19= Button(window,text = ')', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press(")"))
btn19.grid(row=2,column=4)
btn20= Button(window,text = '**', width = 6, height=2, fg='blue',font=('Times', 10),command=lambda: press("**"))
btn20.grid(row=3,column=4)

def press(num):
    global result
    result = result + str(num)
    equation.set(result)








txt1 = Entry(window,width = 30,font=('Arial',10), text=equation)
txt1.grid(row=0,column=0,columnspan=4)

window.mainloop()