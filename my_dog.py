class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking!")
    
    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!")
    
    def sit(self):
        print(f"{self.name} is sitting!")
    
    def stay(self):
        print(f"{self.name} is staying!")
