from tkinter import *
import tkinter.messagebox as m
import time

root = Tk()
root.geometry("900x850")
root.title("ATM MACHINE")

root.configure(bg = "black")

Tops = Frame(root,bg ="white", width =800, height =50, relief = SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root,width =300, height =700,bg="black",relief = SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width =400, height =700,bg ="black",relief = SUNKEN)
f2.pack(side = RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops,font=('aria',30,'bold'),text="BANK MANGEMENT SYSTEM", fg ="Powder Blue", bg="black", bd=10,anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops,font=('aria',20,),text=localtime,fg ="Powder Blue", bg ="black", anchor=W)
lblinfo.grid(row=1,column=0)


number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "

def bank():
    global acca
    accno =["009879","0001234","0009829","1002789","2030456"]
    account =number.get()
    if account in accno:
        label.config(text="Registered User")
        bank={"009879":10000,"0001234":2000,"0009829":30000}
        balance = bank[account]
        acca = balance
        
    else:
        m.showwarning("Non Resgistered User")
        

        
def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Net Balance:",str(bal)))


def withdrawn():
    global acca
    wd= float(withd.get())
    if acca>=wd:
        ace = acca-wd
        label4.config(text = ("Net Balance:",str(ace)))
    else:
        label4.config(text="Insufficient Balance")

        
def bal():
    global acca
    label5.config(text=("Net Balance",str(acca)))


def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
    
    

lb1 = Label(f1,font=('aria',16,'bold'),text ="Enter the account number:        ", bg="black",fg ="Powder Blue", bd=10,anchor='w')
lb1.grid(row=0,column=3)
txt = Entry(f1,font=('ariel',16,'bold'),textvariable=number,bd=6, insertwidth=4,bg="Powder Blue",justify='right')
txt.grid(row=0,column=4)
label =Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label.grid(row=1,column=4)
btnsubmit =Button(f2, padx=16, pady=4, bd=10, fg="black",font=('aria',16,'bold'),width=7,text ="SUBMIT",bg="Powder Blue", command= bank)
btnsubmit.grid(row=0,column=4)

lb1Total = Label(f1,text="                  ",fg="white",bg="black")
lb1Total.grid(row=3,columnspan=10)




lb1 = Label(f1,font=('aria',16,'bold'),text ="Enter the amount to be deposited:", bg="black",fg ="Powder Blue", bd=10,anchor='w')
lb1.grid(row=4,column=3)
txt = Entry(f1,font=('ariel',16,'bold'),textvariable=amount,bd=6, insertwidth=4,bg="Powder Blue",justify='right')
txt.grid(row=4,column=4)
label3=Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label3.grid(row=5,column=4)
btndeposit =Button(f2, padx=16, pady=4, bd=10, fg="black",font=('aria',16,'bold'),width=7,text ="DEPOSIT",bg="Powder Blue", command= deposit)
btndeposit.grid(row=4,column=4)

lb1Total = Label(f1,text="                       ",fg="white",bg="black")
lb1Total.grid(row=7,columnspan=10)


lb1 = Label(f1,font=('aria',16,'bold'),text ="Enter the amount to be withdrawn:        ", bg="black",fg ="Powder Blue", bd=10,anchor='w')
lb1.grid(row=8,column=3)
txt = Entry(f1,font=('ariel',16,'bold'),textvariable=withd,bd=6, insertwidth=4,bg="Powder Blue",justify='right')
txt.grid(row=8,column=4)
label4 =Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label4.grid(row=9,column=4)
label5 =Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label5.grid(row=10,column=4)




btnwithdraw = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text='WITHDRAWL',bg="Powder Blue",command=withdrawn)
btnwithdraw.grid(row=8,column=4)
btnbal= Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text='BALANCE',bg="Powder Blue",command=bal)
btnbal.grid(row=10,column=4)
btnrest= Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text='REST',bg="Powder Blue",command=reset)
btnrest.grid(row=11,column=4)
btnexit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text='EXIT',bg="Powder Blue",command=root.destroy)
btnexit.grid(row=12,column=4)

root.mainloop()
