'''Bài 7: Tọa độ của 1 điểm trong không gian 2 chiều được biểu diễn qua 2 giá trị hoành độ - x – và
tung độ - y. Hãy viết chương trình tính khoảng cách giữa 2 điểm A và B có tọa độ lần lượt là
(xA, yA) và (xB, yB)'''
import math
xa=float(input("xa="))
ya=float(input("ya="))
print("diem A=(",xa,",",ya,")")
xb=float(input("xb="))
yb=float(input("yb="))
print("diem B=(",xb,",",yb,")")
print("khoang cach giua hai diem A va B la:")
print(math.sqrt((xa-xb)**2+(ya-yb)**2))
