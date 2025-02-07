def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def chuanhoa():
    a=str(input('Nhập kí tự'))
    a=a.strip()
    a=a.title()
    a=a.split()
    s=" "
    a=s.join(a)
    print(a)
def danhsach():
    number=list(map(int,input("Nhập một chuỗi các số ngăn cách bơi dấu cách: ").split()))
    k= int (input('Nhập số nguyên k: '))
    s=0
    for i in number:
        if i%2==0:
            s+=i
    number.sort()
    if k in number:
        print('Yes')
    else:
        print('No')
    print(f'Tổng các số trong chuỗi: {sum(number)}')
    print(f'Tổng Các số chắn là: {s}')
    print(f'Phần tử lớn nhất là: {max(number)}')
    print(f'Sắp xếp phần tử từ nhỏ đến lớn',number)
    