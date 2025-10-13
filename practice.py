class pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def information(self): 
        """ This class creates basic information about pets."""
        return (f"This class contains the information of a pet named {self.name} with the specie {self.species} and the age is {self.age}.")
        
    def celebrate(self):
        return (f"Happy birthday dear {self.name}, you are {self.age}, and your specie is {self.species}")
  
pet_info = pet("Pretty", "German sheperd", 5 )

print(pet_info.information())
print(pet_info.celebrate())


