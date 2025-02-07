class person:
    def __init__(self, id, name,country,date):
         self.id=id
         self.name=name
         self.country= country
         self.date=date
class enginer(person):
     def __init__(self, id, name, country, date,subject,year):
          super().__init__(id, name, country, date)
          self.subject=subject
          self.year=year
     def add(self):
          self.id=input("ID:")
          self.name=input("NAME:")
          self.country=input("COUNTRY:")
          self.date=input("DATE:")
          self.subject=input("SUBJECT:")
          self.year= input("YEAR:")
     def show(self):
          print(f'|{self.id:10}|{self.name:10}|{self.date:10}|{self.country:10}|{self.subject:10}|{self.year:10}|')
     def set_name(self, new_id, new_name):
          if self.id == new_id:
               self.name = new_name
def detele(listKs, new_id):
     for ks in listKs:
          if ks.id==new_id:
               listKs.remove(ks)
               print("The enginer had {ks.id} was deteled ")
               return
          else:
               print("No enginer had {ks.id}")
def menu():
        print("\n---Menu---")
        print("1.Show enginer's information")
        print("2.Show enginer graduate near")
        print("3.Detele enginer by finding id")
        print("4.Fix name enginer by finding id")
        print("0.EXIT")
        choice=input("Your choice:")
        return choice

listKs=[]
a=int(input("The quanity of engier:"))
for i in range(a):
     ks=enginer("","","","","","")
     print(f"Input eginer {i+1}")
     ks.add()
     listKs.append(ks)
while True:
    choice=menu()
    if choice=="1":
         print("\n ---List enginer---")
         print(f"|{'id':10}|{'name':10}|{'date':10}|{'country':10}|{'subject':10}|{'year':10}|")
         print(f"_____________________________________________________________________________")
         for ks in listKs:
          ks.show()
    elif choice=="2":
        print("\n -list enginer arrange graduate year -")
        max_year=max(ks.year for ks in listKs )
        print(f"|{'id':10}|{'name':10}|{'date':10}|{'country':10}|{'subject':10}|{'year':10}|")
        print(f"_____________________________________________________________________________")
        for ks in listKs:
            if ks.year==max_year:
                 ks.show()
    elif choice=="3":
         new_id=input("Id enginer you want to detele")
         detele(listKs,new_id)
         print("\n-List enginer without enginer was deteled-")
         for ks in listKs:
            ks.show()
    elif choice == "4":
        new_id = input("ID of the engineer you want to fix: ")
        new_name = input("New name: ")
        for ks in listKs:
            ks.set_name(new_id, new_name)
        print("\n---List of Engineers After Name Fix---")
        for ks in listKs:
            ks.show()
    elif choice=="0":
         print("EXIT PROGRAM")
         break
    else:
         print("Sorry! you must repeat input ")

             
            
