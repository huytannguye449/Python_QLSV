nam=int(input("Nhập số năm bạn muốn: "))
if nam%400==0:
    print("NĂM NHUẬN ")
elif nam%4==0 and nam %100!=0:
    print("NĂM NHUẬN ")
else:
    print("LÀ NĂM KHÔNG NHUẬN")
 