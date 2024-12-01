class Animal:
    is_wild = False
    species_name = "Unknown"

    def get_species_name(self):
        print(self.species_name)

    def sound(self):
        print("Animals Make Sound")


class Dog(Animal):
    has_tail = True

    def __init__(self, breed, eye_color, fur_color="golden"):
        self.breed = breed
        self.eye_color = eye_color
        self.fur_color = fur_color

    def sound(self):
        print("Bark!!!")

    def print_self(self):
        print(self)

    def get_dog_info(self):
        print(self.breed)
        print(self.eye_color)
        print(self.fur_color)
        print(self.has_tail)

    def __repr__(self) -> str:
        return self.breed


tommy = Dog(
    "husky",
    "black",
)

# print(tommy.is_wild)

# tommy.get_species_name()
tommy.sound()
print(type(tommy))