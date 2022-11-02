'''Bài 6: Hãy tính giá trị các biểu thức sau với a, b và α nhập vào từ bàn phím:'''
import math
a=float(input("a="))
b=float(input("b="))
print("\n\n\n\nBai a:")
print("sin(a+b)=", math.sin(a+b))
print("sin(a)*cos(b)=", math.sin(a)*math.cos(b))
print("sin(b)*cos(a)=", math.sin(b)*math.cos(a))
if math.sin(a+b) > math.sin(a)*math.cos(b)+math.sin(b)*math.cos(a):
    print("sin(",a+b,") > sin(",a,")cos(",b,")+sin(",b,")cos(",a,")")
    print("Vi", math.sin(a+b),">",math.sin(a)*math.cos(b)+math.sin(b)*math.cos(a))
else:
    print("sin(", a + b, ") < sin(", a, ")cos(", b, ")+sin(", b, ")cos(", a, ")")
    print("Vi", math.sin(a + b), "<", math.sin(a) * math.cos(b) + math.sin(b) * math.cos(a))
print("\n\n\nBai b:")
print("cos(a)-sin(a)=", math.cos(a)-math.sin(a))
print("cos(a+pi/4)=", math.cos(a+(math.pi/4)))
if math.cos(a)-math.sin(a) <= math.sqrt(2)*math.cos(a+(math.pi/4)):
    print("cos(",a,")-sin(",a,") <= sqrt(2)cos(",a,"+pi/4")
    print("Vi", math.cos(a)-math.sin(a),"<=",math.sqrt(2)*math.cos(a+(math.pi/4)))
else:
    print("cos(",a,")-sin(",a,") > sqrt(2)cos(",a,"+pi/4")
    print("Vi", math.cos(a)-math.sin(a),">",math.sqrt(2)*math.cos(a+(math.pi/4)))
print("\n\n\nBai c:")
print("tan(2a)=", math.tan(2*a))
print("2tan(a)=", 2*math.tan(a))
print("1-tan(a)^2=", 1-math.tan(a)**2)
if math.tan(2*a) != (2*math.tan(a))/(1-math.tan(a)**2):
    print("tan(",2*a,") !=2tan(",a,")/(1-tan(",a,")^2")
    print("Vi", math.tan(2*a),"!=",(2*math.tan(a))/(1-math.tan(a)**2))
else:
    print("tan(",2*a,") == 2tan(",a,")/(1-tan(",a,")^2")
    print("Vi", math.tan(2*a),"==",(2*math.tan(a))/(1-math.tan(a)**2))