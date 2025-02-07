my_dicts=[{"id": 1,"name":"Tan", "age":20, "city":"Hanoi"},
    {"id": 2, "name": "Tran Thi B", "age": 21, "city": "Ho Chi Minh"},
    {"id": 3, "name": "Le Van C", "age": 20, "city": "Hanoi"},
    {"id": 4, "name": "Pham Thi D", "age": 22, "city": "Da Nang"},
    {"id": 5, "name": "Hoang Van E", "age": 18, "city": "Hanoi"},
    {"id": 6, "name": "Vu Thi F", "age": 23, "city": "Hai Phong"},
    {"id": 7, "name": "Do Van G", "age": 20, "city": "Hanoi"},
    {"id": 8, "name": "Bui Thi H", "age": 19, "city": "Can Tho"},
    {"id": 9, "name": "Nguyen Thi I", "age": 21, "city": "Hanoi"}]
print('Danh sách sinh viên')       
for student in my_dicts:
    print(student)
print('Danh sách sinh viên trên 20 tuổi')
for student in my_dicts:
    if student["age"]>=20:
        print(student)
print('Danh sách sinh viên ở Hà Nội')
for student in my_dicts:
    if student["city"]=="Hanoi":
        print(student)
    