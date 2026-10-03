class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, species):
        animal = self.Animal(name,species)
        self.animals.append(animal)




    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species
        def display_info(self):
            print(f"Name : {self.name}, Species : {self.species}")


# create a zoo
my_zoo = Zoo()
# add animals to zoo
my_zoo.add_animal("Lion", "mammal")
my_zoo.add_animal("eagle", "bird")
my_zoo.add_animal("croc", "reptile")


for animal in my_zoo.animals:
    animal.display_info()