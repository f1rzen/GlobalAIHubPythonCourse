#Company Management System

print('\n')
class Employee():
   def __init__(self, name, age, language):
       self.name = name
       self.age = age
       self.language = language
       d[self.name]=self.language



d = {}

class Manager():
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
        z[self.name]=self.language

z = {}

m1 = Manager("Sergen", 48, ["Turkish"])
m2 = Manager("Akif", 21, ["German"])
m3 = Manager("Tuğrul", 32, ["German"])
m4 = Manager("Hamza", 37, ["Arabic", "English"])
m5 = Manager("Gabriela", 20, ["Dutch"])

e1 = Employee("Jack", 22, ["English"])
e2 = Employee("Abdurrahman", 27, ["Turkish"])
e3 = Employee("Larin", 25, ["English"])
e4 = Employee("Aboubakar", 29, ["French", "English"])

print("Employees:")
print('\n')
for i in d.keys():

    print(i + ":" + " " + str(d[i]) )

print('\n')
print("Managers:")
print('\n')
for i in z.keys():

    print(i + ":" + " " + str(z[i]))

#This is a Turkish Company, That is why managers more than employees. :)

"""

Created on Sun Feb  7 01:01:20 2021

@author: https://github.com/f1rzen
"""