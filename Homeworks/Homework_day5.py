class Animal ():
    def __init__(self, specie, kind):
        self.specie = specie
        self.kind = kind
        
        
class Cat(Animal):
    def __init__(self, specie, kind):
        super().__init__(specie, kind)
        
        
class Dog(Animal):
    def __init__ (self, specie, kind, pet ):
        super().__init__(specie, kind)
        self.pet = pet 
        
        
cat1 = Cat("British Shorthair", "Home Cat")
cat2 = Cat("Chartreux", "Home Cat")

dog1 = Dog("Labrador", "Guard Dog", True)
dog2 = Dog("Kangal", "Sheep Dog", True)





            
        
