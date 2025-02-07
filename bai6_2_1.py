a=("Rose", "Tulip", "Sunflower", "Daisy", "Lily", "Orchid", "Daffodil", "Lavender", "Marigold")
F1=a[:5]
F2=a[5:]
print(f'F1:',F1)
print(f'F2:',F2)
dem1= tuple(len(a) for a in F1)
dem2= tuple(len(a) for a in F2)
print('Số kí tự F1:',dem1)
print('Số kí tự F2:',dem2)