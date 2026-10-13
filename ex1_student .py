class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def afficher_infos(self):
        print(f"name : {self.name}, age : {self.age}")
        
student1 = Student (" Alice ", 20)
print (student1.name)
print (student1.age)

student1 = Student (" Alice ", 20)
student2 = Student (" Marc ", 24)
student3 = Student (" Sarah ", 19)

print (f"nom = {student1.name}, age = {student1.age}ans")
print (f"nom = {student2.name}, age = {student2.age}ans")
print (f"nom = {student3.name}, age = {student3.age}ans")
        
# la classe student: est le modèle permettant de créer des objets student1.
# l'objet student1: est ce qu'on fabrique à partir du plan. 
