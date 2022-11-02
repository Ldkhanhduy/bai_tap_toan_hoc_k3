'''Bài 5: Xét phương trình bậc 2:
ax^2 + bx + c = 0 với các hệ số a, b, c ∈ R được nhập vào từ bàn phím, hãy tính biểu thức:
∆ = b^2 − 4ac'''
import math

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
print("∆=", math.pow(b,2)-4*a*c)

