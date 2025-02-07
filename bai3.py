def chuoi():
    list=list(map(int,input("Nhập một chuỗi các số ngăn cách bơi dấu cách: ").split()))
    s=0
    for i in list:
        if i%2==0:
         s+=i
    list.sort()
    print(f'Tổng các số trong chuỗi: {sum(list)}')
    print(f'Tổng Các số chắn là: {s}')
    print(f'Phần tử lớn nhất là: {max(list)}')
    print(f'Sắp xếp phần tử từ nhỏ đến lớn',list)