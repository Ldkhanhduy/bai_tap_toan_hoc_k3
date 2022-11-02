'''Bài 8: Tọa độ của 1 điểm trong không gian 3 chiều được biểu diễn qua 3 giá trị hoành độ - x – và
tung độ - y – và cao độ - z. Hãy viết chương trình tính khoảng cách giữa 2 điểm A và B có tọa độ
lần lượt là (xA, yA, zA) và (xB, yB, zB)'''
import math

xa=float(input("xa="))
ya=float(input("ya="))
za=float(input("za="))
print("diem A=(",xa,",",ya,",",za,")")
xb=float(input("xb="))
yb=float(input("yb="))
zb=float(input("zb="))
print("diem B=(",xb,",",yb,",",zb,")")
print("Khoang cach giua hai diem A va B la:")
print(math.sqrt((xa-xb)**2+(ya-yb)**2+(za-zb)**2))
