from tkinter import*
expression = ""
def press(num):
 global expression
 expression=expression+str(num)
 equation.set(expression)
def equalpress():
 try:
  global expression
  total = str(eval(expression)) 
  equation.set(total)
  expression= ""
 except:
  equation.set("error") 
  expression= ""
def clear():
 global expression
 expression = ""
 equation.set("")

if __name__ == "__main__":
 window=Tk()
 window.title("Simple Calculator")
 window.geometry("400x400")
 equation = StringVar()
 expression_field= Entry(window, textvariable=equation)
 expression_field.grid(columnspan=3,ipadx=50)
 equation.set('Enter your expression')

 clear= Button(window, text='clear',fg='#fff', bg='#000',command=clear, height=1, width=7)
 clear.grid(row=0, column=3)
 
 button1=Button( window,text='1',fg='#fff',bg='#000',command=lambda:press(1),height=1, width=7)
 button1.grid(row=1, column=0,pady=5)

 button2=Button( window,text='2',fg='#fff',bg='#000',command=lambda:press(2),height=1, width=7)
 button2.grid(row=1, column=1)

 button3=Button( window,text='3',fg='#fff',bg='#000',command=lambda:press(3),height=1, width=7)
 button3.grid(row=1, column=2)

 equal = Button(window, text='=',fg='#fff',bg='#000',command=equalpress,height=1,width=7)
 equal.grid(row=1,column=3)

 button4=Button( window,text='4',fg='#fff',bg='#000',command=lambda:press(4),height=1, width=7)
 button4.grid(row=2, column=0,pady=5)

 button5=Button( window,text='5',fg='#fff',bg='#000',command=lambda:press(5),height=1, width=7)
 button5.grid(row=2, column=1)

 button6=Button( window,text='6',fg='#fff',bg='#000',command=lambda:press(6),height=1, width=7)
 button6.grid(row=2, column=2)

 plus=Button(window,text='+',fg='#fff',bg='#000',command=lambda:press("+"),height=1,width=7)
 plus.grid(row=2,column=3)

 button7=Button( window,text='7',fg='#fff',bg='#000',command=lambda:press(7),height=1, width=7)
 button7.grid(row=3, column=0)

 button8=Button( window,text='8',fg='#fff',bg='#000',command=lambda:press(8),height=1, width=7)
 button8.grid(row=3, column=1,pady=5)

 button9=Button( window,text='9',fg='#fff',bg='#000',command=lambda:press(9),height=1, width=7)
 button9.grid(row=3, column=2)
 
 minus= Button(window, text='-',fg='#fff',bg='#000',command=lambda:press("-"),height=1,width=7)
 minus.grid(row=3,column=3)

 button0=Button( window,text='0',fg='#fff',bg='#000',command=lambda:press(0),height=1, width=7)
 button0.grid(row=4, column=0,pady=5)

 decimal=Button(window,text='.',fg='#fff',bg='#000',command=lambda:press("."),height=1,width=7)
 decimal.grid(row=4,column=1)

 multiply=Button( window,text='*',fg='#fff',bg='#000',command=lambda:press("*"),height=1, width=7)
 multiply.grid(row=4, column=2)

 divide=Button( window,text='/',fg='#fff',bg='#000',command=lambda:press("/"),height=1, width=7)
 divide.grid(row=4, column=3)

 window.mainloop()
