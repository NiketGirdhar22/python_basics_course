class vehicle():
    def __init__(self,bodystyle):
        self.bodystyle = bodystyle
    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed

class car(vehicle):
    def __init__(self,engine_type):
        super().__init__("car")
        self.wheels = 4
        self.doors = 4
        self.engine_type = engine_type
    def drive(self,speed):
        super().drive(speed)
        print("Driving my ",self.engine_type," car at ",self.speed)

class motorbike(vehicle):
    def __init__(self,engine_type,has_side_car):
        super().__init__("motorbike")
        if(has_side_car):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine_type = engine_type
    def drive(self,speed):
        super().drive(speed)
        print("Driving my ",self.engine_type," motorbike at ",self.speed)

car1 = car("gas")
car2 = car("electric")
motorbike1 = motorbike("gas",True)
motorbike2 = motorbike("gas",False)

print(motorbike1.wheels)
print(motorbike2.wheels)
print(car1.engine_type)
print(car2.doors)
car1.drive(30)
car2.drive(40)
motorbike1.drive(50)
motorbike2.drive(100)