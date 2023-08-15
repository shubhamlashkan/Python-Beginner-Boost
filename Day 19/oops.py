#           Python Begineer Boost

#           Object Oriented Programming - Part 1


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print(f"{self.make} Engine Started")

    def stop_engine(self):
        print(f"{self.make} Engine stopped")  


print("Creating toyota car")

car1 = Car("Toyota","Corolla",2022)
print(car1.make)
car1.start_engine()
car1.stop_engine()

print("Creating Honda car")

car2 = Car("Honda","camry",2012)
print(car2.make)
print(car2.model)
print(car2.year)

car2.start_engine()
car2.stop_engine()