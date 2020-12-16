# A small GUI application of password generator
import random as rn

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
    return (pas)    
    pass_check(pas, n)
    
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
        return(pas)
    else:
        pass_gen()
#-------------------------------------------------MAIN-------------------------------------------------------#
num=rn.randint(10,20)
p=pass_gen(num)
print(f"The given password is {p}")





