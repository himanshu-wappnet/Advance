#we are importing car module which is our index/main file.
import car

#overriding abstract method
class tyre(car.Car):
    def suzuki(self):
        car.Car.car(self)
        print("Suzuki car will have alloy glosy wheels.")
        
#overriding abstract method
class body(car.Car):
    def suzuki(self):
        print("The body of suzuki car will be metallic")
        
#overriding abstract method
class color(car.Car):
    def suzuki(self):
        print("It will be available in Red, Black, Blue, Purple, Cyan")

#overriding abstract method        
class model(car.Car):
    def suzuki(self):
        print("Wagon R, ertiga, Baleno, S-cross, Dzire, Swift")

#overriding abstract method
class milage(car.Car):
    def suzuki(self):
        print("It's milage will be around 33kmpl - 69kmpl ")
        
#overriding abstract method
class speed(car.Car):
    def suzuki(self):
        print("Top speed will be 230 km/hr.")

#overriding abstract method
class price(car.Car):
    def suzuki(self):
        print("It will cost around 6 lakhs - 55 lakhs.")