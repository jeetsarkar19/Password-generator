# A small GUI application of password generator
import random as rn
import tkinter as tk
win=tk.Tk()
win.title("Password Generator")
blank=tk.Entry(master=win)
def pass_gen():
    blank.delete(0,tk.END)
    n = rn.randint(10,20)
    pas=''
    space1 =[]
    for k in range(33, 125):
        j = chr(k)
        space1.append(j)
    list2 = rn.choices(space1, k=n)
    for m in list2:
        pas = pas+m
    pass_check(pas, n)
    return (pas)
# Creating the password checker, that is, whether it manages to create a password which can be accepted by the websites 
def pass_check(pas,n):
    c1=c2=c3=c4=0
    for j in pas:
        ch=ord(j)
        if((ch>=33 and ch<=47) or (ch>=58 and ch<=64) or (ch>=123 and ch>=125)):
            c1+=1
        elif(ch>=48 and ch<=57):
            c2+=1
        elif(ch>=65 and ch<=90):
            c3+=1
        else:
            c4+=1
    if (c1>0 and c2>0 and c3>0 and c4>0):
        blank.insert(0,pas)
    else:
        pass_gen()
def del_text():
    blank.delete(0,tk.END)
    return 0
def quit_gui():
    win.destroy()
    return 0

#Turning the text based code into a GUI application 

label=tk.Label(master=win,text="Welcome to the Password Generator")
btn1=tk.Button(master=win,text="click me", command=pass_gen)  
btn2=tk.Button(master=win,text="Delete", command=del_text)  
btn3=tk.Button(master=win,text="Quit", command=quit_gui)   
label.grid(row=0,column=1)
btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)
blank.grid(row=1,column=1)
win.mainloop()
