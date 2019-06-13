class Vehicle():
    licenseCode = ''
    serialCode = ''
    def acOn(self):
        print("AC : ON")

class Car(Vehicle):
   def sayHello(self):
       print("Hello")
class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estate(Vehicle):
    pass

car1 = Car()
car1.acOn()
car1.sayHello()

van1 = Van()
van1.acOn()

pickup1 = Pickup()
pickup1.acOn()

estate1 = Estate()
estate1.acOn()
