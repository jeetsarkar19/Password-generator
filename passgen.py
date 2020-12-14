# This is the password generator using random letters
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
    return pas
# MAIN
num = int(input("Enter the number of characters : "))
p = pass_gen(num)
print(p)
