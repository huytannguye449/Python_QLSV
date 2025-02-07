nam=int(input("Nhập Năm: "))
thang=int(input("Nhập Tháng: "))
if thang>12 or thang==0 :
 print("Nhập lại")
elif (nam%400==0 or nam%4==0) and (nam %100!=0) and (thang==2):
  print("29")
elif thang <= 7 and thang %2==0:
  print("30")
elif thang > 7 and thang %2==0:
  print("31")
else:
  print("28")