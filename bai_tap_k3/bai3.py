'''Bài 3: Viết chương trình tính giá trị của biểu thức Toán học sau (x1, x2, x3 nhập vào từ bàn phím)

1/
1 + e**(2*x1+4*x2−5*x3)'''
import math

x1=float(input("x1="))
x2=float(input("x2="))
x3=float(input("x3="))
print("ket qua theo de bai la:", 1/(1+math.exp(2*x1+4*x2-5*x3)))

