class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.odometer=0
    def drive(self,km):
        self.odometer+=km
    def show_odometer(self):
        print(f"Odometer: {self.odometer} km")

car1=Car("Toyota","Innova")
car1.drive(120)
car1.drive(30)
car1.show_odometer()

car1.drive(50)
car1.show_odometer()

car1.drive(20)
car1.show_odometer()
print(car1.make,car1.model)
        