# This is the password generator using random letters
# This is a small attempt on building a password generator and tweaking it into a gui type application
import random as rn
def pass_gen(n):
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
        print("The password is",pas)
    else:
        pass_gen(n)

------------# MAIN---------------------------------
num = int(input("Enter the number of characters : "))
pass_gen(num)

