'''Bài 1: Viết chương trình tính giá trị của biểu thức Toán học sau (x1, x2 nhập vào từ bàn phím)

(x1 + x2)/ (x1 − x2) với x1, x2 ∈ R'''
x1=float(input("x1="))
x2=float(input("x2="))
if (x1-x2)==0:
    print("Khong xac dinh")
else:
    print("(x1+x2)/(x1-x2)=",(x1+x2)/(x1-x2))
    
