#we are importing car module which is our index/main file.
import car

#overriding abstract method
class tyre(car.Car):
    def renault(self):
        car.Car.car(self)
        print("Renault will have alloy wheels with Diamond Shape.")
        
#overriding abstract method
class body(car.Car):
    def renault(self):
        print("Body will be Glossy Metallic.")
        
#overriding abstract method
class color(car.Car):
    def renault(self):
        print("It will be available in Red, Black and Blue.")
        
#overriding abstract method
class model(car.Car):
    def renault(self):
        print("Duster, kwid, cluster, climber.")

#overriding abstract method
class milage(car.Car):
    def renault(self):
        print("It's milage will be around 33kmpl - 50kmpl ")
        
#overriding abstract method
class speed(car.Car):
    def renault(self):
        print("The Top speed of renault will be 200 km/hr.")

#overriding abstract method
class price(car.Car):
    def renault(self):
        print("It will cost around 6 lakhs - 65 lakhs.")