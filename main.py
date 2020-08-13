from tkinter import *
from math import *
import tkinter.messagebox

def msgbox():
    tkinter.messagebox.showinfo('About Calci','Made By Gaurav Singh e-mail (101701010@smail.iitpkd.ac.in) ')

root = Tk()
root.title('GS Calculator')
root.geometry('480x600')
root.resizable(0,0)

var=''
data=StringVar()

def btnclick(numbers):
    global var
    var=var+str(numbers)
    data.set(var)

def allclr():
    screen.delete(0,END)
    var=" "

def eqls():

    data.set(eval(data.get()))

def regular():
    root.geometry('480x600')

def scientific():
    root.geometry('1024x600')

menu=Menu(root)
root.config(menu=menu)

submenu=Menu(menu)

menu.add_cascade(label='Calci Type',menu=submenu)
submenu.add_command(label='Regular',command=regular)
submenu.add_command(label='Scientific',command=scientific)

menu.add_cascade(label='Help?',menu=submenu)
submenu.add_command(label='About Calci',command=msgbox)

f0=Frame(root, width=100, height=200)
f0.pack(expand=True,fill=BOTH)


screen=Entry(f0,font=('arial' ,30,'bold'),bd=30,textvariable=data,justify='right',bg='cyan')
screen.pack(expand=True,fill=BOTH)

f1=Frame(root)
f1.pack(expand=True,fill=BOTH)

b1=Button(f1,padx=16,pady=16,text='1',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(1))
b1.pack(side=LEFT,expand=True,fill=BOTH)

b2=Button(f1,padx=16,pady=16,text='2',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(2))
b2.pack(side=LEFT,expand=True,fill=BOTH)

b3=Button(f1,padx=16,pady=16,text='3',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(3))
b3.pack(side=LEFT,expand=True,fill=BOTH)

b4=Button(f1,padx=16,pady=16,text='4',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(4))
b4.pack(side=LEFT,expand=True,fill=BOTH)

bsin=Button(f1,padx=16,pady=16,text='sin',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:sin())
bsin.pack(side=LEFT,expand=True,fill=BOTH)

bcos=Button(f1,padx=16,pady=16,text='cos',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:cos())
bcos.pack(side=LEFT,expand=True,fill=BOTH)

btan=Button(f1,padx=16,pady=16,text='tan',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:tan())
btan.pack(side=LEFT,expand=True,fill=BOTH)

bcot=Button(f1,padx=16,pady=16,text='cot',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:cot())
bcot.pack(side=LEFT,expand=True,fill=BOTH)

f2=Frame(root)
f2.pack(expand=True,fill=BOTH)

b5=Button(f2,padx=16,pady=16,text='5',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(5))
b5.pack(side=LEFT,expand=True,fill=BOTH)

b6=Button(f2,padx=16,pady=16,text='6',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(6))
b6.pack(side=LEFT,expand=True,fill=BOTH)

b7=Button(f2,padx=16,pady=16,text='7',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(7))
b7.pack(side=LEFT,expand=True,fill=BOTH)

b8=Button(f2,padx=16,pady=16,text='8',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(8))
b8.pack(side=LEFT,expand=True,fill=BOTH)

bsec=Button(f2,padx=16,pady=16,text='sec',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:sec())
bsec.pack(side=LEFT,expand=True,fill=BOTH)

bcosec=Button(f2,padx=16,pady=16,text='cosec',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:cosec())
bcosec.pack(side=LEFT,expand=True,fill=BOTH)

bpi=Button(f2,padx=16,pady=16,text='π',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:pi())
bpi.pack(side=LEFT,expand=True,fill=BOTH)

be=Button(f2,padx=16,pady=16,text='e',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:e())
be.pack(side=LEFT,expand=True,fill=BOTH)


f3=Frame(root)
f3.pack(expand=True,fill=BOTH)

b9=Button(f3,padx=16,pady=16,text='9',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(9))
b9.pack(side=LEFT,expand=True,fill=BOTH)

b0=Button(f3,padx=16,pady=16,text='0',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:btnclick(0))
b0.pack(side=LEFT,expand=True,fill=BOTH)

badd=Button(f3,padx=16,pady=16,text='+',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick('+'))
badd.pack(side=LEFT,expand=True,fill=BOTH)

bsub=Button(f3,padx=16,pady=16,text='-',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick('-'))
bsub.pack(side=LEFT,expand=True,fill=BOTH)

blog=Button(f3,padx=16,pady=16,text='log',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:log())
blog.pack(side=LEFT,expand=True,fill=BOTH)

blog10=Button(f3,padx=16,pady=16,text='log10',bd=10,font=('arial' ,20,'bold'),bg='cyan',command=lambda:log10())
blog10.pack(side=LEFT,expand=True,fill=BOTH)

broot=Button(f3,padx=16,pady=16,text='√',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:sqrt())
broot.pack(side=LEFT,expand=True,fill=BOTH)

brandom=Button(f3,padx=16,pady=16,text='Random',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:random())
brandom.pack(side=LEFT,expand=True,fill=BOTH)

f4=Frame(root)
f4.pack(expand=True,fill=BOTH)

bdiv=Button(f4,padx=16,pady=16,text='/',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick('/'))
bdiv.pack(side=LEFT,expand=True,fill=BOTH)

bmul=Button(f4,padx=16,pady=16,text='*',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick('*'))
bmul.pack(side=LEFT,expand=True,fill=BOTH)

bdot=Button(f4,padx=16,pady=16,text='.',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick('.'))
bdot.pack(side=LEFT,expand=True,fill=BOTH)

ballclr=Button(f4,text='C',bd=10,font=('arial',18,'bold'),bg='cyan',command=lambda:allclr())
ballclr.pack(side=LEFT,expand=True,fill=BOTH)

bleft=Button(f4,padx=16,pady=16,text='(',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick('('))
bleft.pack(side=LEFT,expand=True,fill=BOTH)

bright=Button(f4,padx=16,pady=16,text=')',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:btnclick(')'))
bright.pack(side=LEFT,expand=True,fill=BOTH)

bfactorial=Button(f4,padx=16,pady=16,text='!',bd=10,font=('arial',20,'bold'),bg='cyan',command=lambda:factorial())
bfactorial.pack(side=LEFT,expand=True,fill=BOTH)

brad=Button(f4,text='rad',bd=10,font=('arial',18,'bold'),bg='cyan',command=lambda:radians())
brad.pack(side=LEFT,expand=True,fill=BOTH)

f5=Frame(root)
f5.pack(expand=True,fill=BOTH)

beqls=Button(f5,text='=',bd=10,font=('arial',18,'bold'),bg='cyan',command=lambda:eqls())
beqls.pack(side=LEFT,expand=True,fill=BOTH)

status=Label(text='A Simple Calculator With Tkinter....',relief=SUNKEN,bd=2,anchor=W)
status.pack(fill=X,side=BOTTOM)
root.mainloop()
