#we are importing car module which is our index/main file.
import car

#overriding abstract method
class tyre(car.Car):
    def hyundai(self):
        car.Car.car(self)
        print("Hyundai will have both metallic and alloy wheels")

#overriding abstract method    
class body(car.Car):
    def hyundai(self):
        print("The body of Hyundai cars will be metallic")
        
#overriding abstract method
class color(car.Car):
    def hyundai(self):
        print("They will be available in Red, Black, Blue, and white.")
        
#overriding abstract method
class model(car.Car):
    def hyundai(self):
        print("Venue, Creta, i10, i20, santafe")

#overriding abstract method
class milage(car.Car):
    def hyundai(self):
        print("It's milage will be around 33kmpl - 45kmpl. ")
        
#overriding abstract method
class speed(car.Car):
    def hyundai(self):
        print("Top speed will be 150km/pr - 200 km/hr.")

#overriding abstract method
class price(car.Car):
    def hyundai(self):
        print("It will cost around 8 lakhs - 60 lakhs.")