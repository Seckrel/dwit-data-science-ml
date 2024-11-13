class Vehicles:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_number_of_wheels(self):
        return 1

    def start_engine(self):
        return f"{self.year} {self.make} {self.model} engine started."

    def stop_engine(self):
        return f"{self.year} {self.make} {self.model} engine stopped."


class Car(Vehicles):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_number_of_wheels(self):
        return 4

    def open_trunk(self):
        return "The car trunk is now open."
    

vechicle = Vehicles("Toyota", "Corola", "1999")
print(vechicle.get_number_of_wheels())

car = Car("Toyota", "Corola", "1999", 2)
print(car.get_number_of_wheels())
