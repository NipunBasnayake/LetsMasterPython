class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__ (self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

        def bark(self):
            print("woof!")

            my_dog = Dog(name = "Buddy", age = 3)
            

            dog_name = my_dog.name
            dog_age = my_dog.age
            dog_species = my_dog.species

            my_dog.bark()  # Output: woof!
            print(f"name: {dog_name}")
            print(f"age: {dog_age}")
            print(f"species: {dog_species}")