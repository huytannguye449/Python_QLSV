a= ("Rose", "Tulip", "Sunflower", "Daisy", "Lily", "Orchid", "Daffodil", "Lavender", "Marigold")
F1= a[:5]
F2= a[5:]
print(f'F1:',F1)
print(f'F2:',F2)
print("số kí tự F1 là:", end= " ")
for i in range (len(F1)):
    print(len(F1[i]), end=' ')
print(end="\n")
print("số kí tự F2 là:", end= " ")
for i in range (len(F2)):
    print(len(F1[i]), end=' ')

