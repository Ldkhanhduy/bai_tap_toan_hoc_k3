'''Bài 4: Viết chương trình tính giá trị của biểu thức sau

((x1 + x2)/(x1 − x2)) >1/(1 + e**(2x1+4x2)) với xi ∈ R'''
import math

x1=float(input("x1="))
x2=float(input("x2="))
if (x1-x2)==0:
    print("Khong xax dinh")
else:
    if ((x1 + x2)/(x1-x2)) >1/(1 + math.exp(2*x1+4*x2)):
        print("ket qua theo de bai la:",((x1 + x2)/(x1-x2)) >1/(1 + math.exp(2*x1+4*x2)))
        print(((x1 + x2)/(x1-x2)),">",1/(1 + math.exp(2*x1+4*x2)))
    else:
        print("ket qua theo de bai la:", ((x1 + x2) / (x1 - x2)) > 1 / (1 + math.exp(2 * x1 + 4 * x2)))
        print(((x1 + x2) / (x1 - x2)), "<", 1 / (1 + math.exp(2 * x1 + 4 * x2)))
