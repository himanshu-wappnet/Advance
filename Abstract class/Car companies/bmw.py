#we are importing car module which is our index/main file.
import car

#overriding abstract method
class tyre(car.Car):
    def bmw(self):
        car.Car.car(self) 
        print("BMW will have alloy wheels")
        
#overriding abstract method
class body(car.Car):
    def bmw(self):
       print("The body of BMW will be metallic.")
       
#overriding abstract method        
class color(car.Car):
    def bmw(self):
        print("BMW will be available in White, Black and Blue.")

#overriding abstract method        
class model(car.Car):
    def bmw(self):
        print("The availabe model for BMW are X1, X6, 320d, 5520d, X5, X7")

#overriding abstract method
class milage(car.Car):
    def bmw(self):
        print("BMW's milage will be around 33kmpl. ")
        
#overriding abstract method
class speed(car.Car):
    def bmw(self):
        print("Top speed of BMW will be 350 km/hr.")

#overriding abstract method
class price(car.Car):
    def bmw(self):
        print("It will cost around 60 lakhs - 75 lakhs.")