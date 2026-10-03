# Creating a class
class Vehicle:
    #creating a class attribute
    class_attribute = "This is a vehicle class"


    # creating constructor
    def __init__(self, name, color):

        #instance variables
        self.name = name
        self.color = color


    #creating class method
    @classmethod
    def class_method(cls):
        print("this is a class method")
        print(f"i can access the class attribute : {cls.class_attribute}")

    # instance method
    def display_info(self):
        print(f"Name : {self.name}, color : {self.color}")

    #static method
    @staticmethod
    def static_method():
        print("I am a static method, I cannot access anything")

# create an object
vehicle= Vehicle("coolcar", "red")
# print(f"{vehicle.name} {vehicle.color}")
vehicle.display_info()

# inheritence
class Car(Vehicle):
    pass

# calling inheritance class
car = Car("mercedez", "black")
car.display_info()


#method overriding
class Car2(Vehicle):
    def __init__(self,name, color, fuel_type):
        super().__init__(name, color)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"{self.name}, {self.color}, {self.fuel_type}")


car_2 = Car2("honda_civic", "purple", "petrol")
car_2.display_info()

#class attribute printing
print(Vehicle.class_attribute)

#calling class method
Vehicle.class_method()

#calling static method
Vehicle.static_method()