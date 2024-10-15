

class Car:
    total_car = 0
    def __init__(self , model, brand):
        self.__brand = brand
        self.__model= model
        Car.total_car +=1
    
    def get_brand(self):
        return self.__brand
    def full_name(self):
        print(f"{self.brand} {self.model}")


    def fuel_type(self):
        return "Petrol Deseil"

    @staticmethod
    def genrel_description():
        return "car gernal description"
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, model, brand, battraysize):
        super().__init__(model, brand)
        self.battraysize = battraysize


    def fuel_type(self):
        return "Eletric charge"

tesala_car = ElectricCar("tesala" ,"model s" , "80kwh")


# print(tesala_car.battraysize)
# print(tesala_car.full_name())

# my_car = Car("Toyota", "Corllo")
# print(my_car.fuel_type())
# print(tesala_car.fuel_type())

# print(Car.total_car)
# # print(my_car.full_name())

# print(Car.genrel_description())

print(isinstance(tesala_car , Car))
print(isinstance(tesala_car,ElectricCar))