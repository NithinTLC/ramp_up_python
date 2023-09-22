class Employee:
    def __init__(self,Name,Dept,Experience,ID):
        self.Name= Name
        self.Dept= Dept
        self.Exp = Experience
        self.id =ID
    def Showdetails(self):
        print(f"Name of the employee: {self.Name}")
        print(f"Department               : {self.Dept}")
        print(f"Years of experience: {self.Exp}")
        print(f"ID: {self.id}")

class Managers(Employee):
    def __init__(self, Name, Dept, Experience, ID,Role="manager"):
        super().__init__(Name,Dept,Experience,ID)
        self.Role =Role
    def Showdetails(self):
        super().Showdetails()
        print(f"Role: {self.Role}")
        print("**********************")


class Developers(Employee):
    def __init__(self, Name, Dept, Experience, ID,Lang):
        super().__init__(Name,Dept,Experience,ID)
        self.Lang =Lang
    def Showdetails(self):
        super().Showdetails()
        print(f"Role: Developer")
        print(f"Language: {self.Lang}")
        print("**********************")


emp1=Managers("Nithin","Engg",2,5)
emp2=Developers("Sai","Engg",1,2,"Python")

emp1.Showdetails()
emp2.Showdetails()

print(Managers.__mro__)

