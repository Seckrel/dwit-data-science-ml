class Vehicle:
    __model = ""  

    def __init__(self, make, model, number_of_wheels):
        self.__make = make  
        self.__model = model
        self._number_of_wheels = number_of_wheels  

    def get_make(self): 
        return self.__make

    def get_model(self): 
        return self.__model

    def get_number_of_wheels(self): 
        return self._number_of_wheels

    def set_make(self, make): 
        if isinstance(make, str):
            self.__make = make
        else:
            print("Invalid make")


class Car(Vehicle): 
    def __init__(self, make, model, number_of_wheels):
        super().__init__(make, model, number_of_wheels)
        self.__make = "Toyota"
        self._number_of_wheels = 3

    def __str__(self):  # String representation of the Car object
        return f"{self.get_make()} {self.get_model()} with {self.get_number_of_wheels()} wheels."


# Creating an instance of Car
car = Car("Tesla", "Model S", 4)
print(car) 
print(car.get_model())
print(car.get_number_of_wheels())
# print(car.__make) # not allowed
# print(car._number_of_wheels) # not allowed (py allows it)
