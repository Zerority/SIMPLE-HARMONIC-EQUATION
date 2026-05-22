#Nhập các giá trị của phương trình dao động
biendo = float(input("Nhập biên độ (A): "))
tanso = float(input("Nhập tần số (f): "))
pha = float(input("Nhập pha (phi) (đơn vị độ): "))
#Chuyển pha từ độ sang radian
import math
pha_rad = math.radians(pha)
#Tính tần số góc (omega)
omega = 2 * math.pi * tanso
#Nhập thời gian thực hiện dao động
thoigian = float(input("Nhập thời gian (t): "))
#Tính giá trị của phương trình dao động tại thời gian t
x = biendo * math.sin(omega * thoigian + pha_rad)
lamtron = round(x, 2)
#In kết quả
print("Giá trị của phương trình dao động điều hoà tại thời gian t là :", lamtron)