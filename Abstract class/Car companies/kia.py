#we are importing car module which is our index/main file.
import car

#overriding abstract method
class tyre(car.Car):
    def kia(self):
        car.Car.car(self)
        print("Kia will have also have both alloy and metallic wheels.")
        
#overriding abstract method
class body(car.Car):
    def kia(self):
        print("Kia's body will be metallic with shiny look.")
        
#overriding abstract method
class color(car.Car):
    def kia(self):
        print("It will be available in Red, Black, Brown, Blue and Maroon")

#overriding abstract method        
class model(car.Car):
    def kia(self):
        print("Seltos, Karrens, Sonet, Carnival")

#overriding abstract method
class milage(car.Car):
    def kia(self):
        print("It's milage will be around 33kmpl - 46kmpl ")

#overriding abstract method        
class speed(car.Car):
    def kia(self):
        print("Top speed will be 200 km/hr.")

#overriding abstract method
class price(car.Car):
    def kia(self):
        print("It will cost around 8 lakhs - 45 lakhs.")