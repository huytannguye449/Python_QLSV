class SACH:
    def __init__(self, ten_sach, tac_gia, gia_ban):
        self.ten_sach= ten_sach
        self.tac_gia=tac_gia
        self.gia_ban=gia_ban
    def nhap(self):
        self.ten_sach= input("Nhập tên sách:")
        self.tac_gia=input("Nhập tên tác giả:")
        self.gia_ban=int(input("Nhập giá bán:"))
    def in_du_lieu(self):
        print(f"|{self.ten_sach:5}|{self.tac_gia:5}|{self.gia_ban:5}|")
class BIA(SACH):
    def __init__(self, ten_sach, tac_gia, gia_ban,ma_hinh_anh, tien_ve):
        super().__init__(ten_sach, tac_gia, gia_ban)
        self.ma_hinh_anh=ma_hinh_anh
        self.tien_ve=tien_ve
    def nhap(self):
        super().nhap()
        self.ma_hinh_anh=input("Nhập mã ảnh")
        self.tien_ve=int(input("Nhập tiền vẽ"))
    def in_du_lieu(self):
        super().in_du_lieu()
        print(f"|{self.ma_hinh_anh:5}|{self.tien_ve:5}|")
class HOASY():
    def __init__(self, ten_hoa_sy, dia_chi):
        self.ten_hoa_sy=ten_hoa_sy
        self.dia_chi=dia_chi
    def nhap(self):
        self.ten_hoa_sy=input("Nhập tên họa sỹ")
        self.dia_chi=input("Nhập địa chỉ")
    def in_du_lieu(self):
        print(f"|{self.ten_hoa_sy:5}|{self.dia_chi:5}|")
class SACHVEBIA(BIA, HOASY):
    def __init__(self, ten_sach, tac_gia, gia_ban, ma_hinh_anh, tien_ve,ten_hoa_sy,dia_chi):
        BIA.__init__(self,ten_sach, tac_gia, gia_ban, ma_hinh_anh, tien_ve)
        HOASY.__init__(self,ten_hoa_sy,dia_chi)
    def nhap(self):
        BIA.nhap(self)
        HOASY.nhap(self)
    def tong_tien(self):
        return self.gia_ban + self.tien_ve
    def in_du_lieu(self):
        BIA.in_du_lieu(self)
        HOASY.in_du_lieu(self)
        print(f"Tổng số tiên {self.tong_tien()}")
def menu():
        print("\n---Menu---")
        print("1.Nhập danh sách")
        print("2.In danh sách")
        print("3.Sắp xếp danh sách các sách có vẽ theo giá tăng dần")
        print("4.Tìm kiếm tác giả vẽ sách")
        print("0.EXIT")
        choice=input("Your choice:")
        return choice
danh_sach_sach_co_ve=[]
danh_sach_khong_bia=[]
while True:
    choice=menu()
    if choice=="1":
     n=int(input("Nhập sách vẽ bìa"))
     for i in range(n):
        sach=SACHVEBIA("","","","",0,"","")
        print(f"Nhập quyển số {i+1}")
        sach.nhap()
        danh_sach_sach_co_ve.append(sach)
     m=int(input("Nhập số lượng sách không vẽ bìa:"))
     for i in range (m):
        sach=SACH("","",0)
        print(f"Nhập quyển số{i+1}")
        sach.nhap()
        danh_sach_khong_bia.append(sach)
    elif choice=="2":
        print("\n Danh sách các sách không bìa")
        print("|{'ten_sach':5}|{'tac_gia':5}|{'gia_ban':5}|")
        for sach in danh_sach_khong_bia:
            sach.in_du_lieu()
        print("\n Danh sách các sách có bìa")
        print("|{'ten_sach':5}|{'tac_gia':5}|{'gia_ban':5}|{'ma_hinh_anh':5}|{'tien_ve':5}|{'ten_hoa_sy':5}|{'dia_chi':5}|")
        for sach in danh_sach_sach_co_ve:
                sach.in_du_lieu()
    elif choice=="3":
        danh_sach_sach_co_ve.sort(key= lambda x: x.gia_ban)
        print("\n Danh sách các sách có bìa sau sắp xếp lai")
        print("|{'ten_sach':5}|{'tac_gia':5}|{'gia_ban':5}|{'ma_hinh_anh':5}|{'tien_ve':5}|{'ten_hoa_sy':5}|{'dia_chi':5}|")
        for sach in danh_sach_sach_co_ve:
            sach.in_du_lieu()
    elif choice=="4":
        ten_tim_kiem=input("Nhập tên tìm kiếm")
        for sach in danh_sach_sach_co_ve:
            if sach.tac_gia == ten_tim_kiem:
                sach.in_du_lieu()
            else:
                print("Không có sách của tác giả" )
    elif choice=="0":
         print("EXIT PROGRAM")
         break
    else:
         print("Sorry! you must repeat input ")