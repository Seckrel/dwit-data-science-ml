class Vehicles:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.year} {self.make} {self.model} engine started."

    def stop_engine(self):
        return f"{self.year} {self.make} {self.model} engine stopped."


class Car(Vehicles):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_trunk(self):
        return "The car trunk is now open."

class Bike(Vehicles):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def pop_wheelie(self):
        return "The bike pops a wheelie!"

    
my_car = Car("Toyota", "Camry", 2021, 4)
my_bike = Bike("Yamaha", "YZF-R3", 2022, "Sport")

print(my_car.start_engine())
print(my_bike.start_engine())

print(my_car.open_trunk())     
print(my_bike.pop_wheelie()) 
