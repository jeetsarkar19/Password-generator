# This is a small attempt on building a password generator and tweaking it into a gui type application
import random as rn
import tkinter as tk
blank=tk.Entry()
def pass_gen():
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
#Turning the text based code into a GUI application 

win = tk.Tk()

frame1=tk.Frame()
frame1.grid(row=0,column=2)
label=tk.Label(frame1,text="Welcome to the Password Generator")
btn1=tk.Button(text="click me", command=pass_gen)  
btn2=tk.Button(text="Delete", command=del_text)      
label.pack()
btn1.grid(row=2,column=2)
btn2.grid(row=2,column=3)
blank.grid(row=3,column=2)
win.mainloop() 

