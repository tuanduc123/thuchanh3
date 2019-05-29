import math
def Tinh(R):
   if R<0:
       print ("R khong hop le")
   else:
       C = 2*R*math.pi
       S = R*R*math.pi
       print ("Chu vi la :", C)
       print ("Dien tich la :", S)

R = float(input("Nhap ban kinh hinh tron: "))
Tinh(R)
