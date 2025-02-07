import math
n= int(input("Nhập số nguyên dương a"))
a=0
for n in range(1,n+1,1):
  a+=1/math.factorial(n)
print (f"Tổng là:{a}")

