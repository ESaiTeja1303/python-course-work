#Eraram Sai Teja Goud (PFS-22)
#Car Rental Management System
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    @abstractmethod
    def get_role(self):
        pass

    def get_details(self):
        return f"Name: {self.name}, Contact: {self.contact}, Role: {self.get_role()}"

class Customer(Person):
    def __init__(self, name, contact, license_number):
        super().__init__(name, contact)
        self.license_number = license_number

    def get_role(self):
        return "Customer"

    def get_customer_info(self):
        return f"{self.get_details()}, License: {self.license_number}"

class Car:
    total_cars = 0

    def __init__(self, car_id, model, price_per_day):
        self.car_id = car_id
        self.model = model
        self.price_per_day = price_per_day
        self.available = True
        Car.total_cars += 1

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def get_info(self):
        return f"ID: {self.car_id}, Model: {self.model}, Price/Day: ₹{self.price_per_day}, Available: {self.available}"

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

class Reservation:
    def __init__(self, customer, car, days):
        self.customer = customer
        self.car = car
        self.days = days
        self.total_amount = self.calculate_amount()
        car.mark_unavailable()

    def calculate_amount(self):
        return self.car.price_per_day * self.days

    def get_receipt(self):
        return f"{self.customer.name} rented {self.car.model} for {self.days} days. Total: ₹{self.total_amount}"

class CarRentalSystem:
    def __init__(self):
        self.customers = []
        self.cars = []
        self.reservations = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_car(self, car):
        self.cars.append(car)

    def show_available_cars(self):
        for car in self.cars:
            if car.available:
                print(car.get_info())

    def make_reservation(self, customer_name, car_id, days):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        car = next((c for c in self.cars if c.car_id == car_id and c.available), None)
        if customer and car:
            reservation = Reservation(customer, car, days)
            self.reservations.append(reservation)
            print("Reservation Successful!")
            print(reservation.get_receipt())
        else:
            print("Reservation Failed! Either customer not found or car unavailable.")

    @staticmethod
    def welcome():
        return "Welcome to FastRide Car Rentals!"

print(CarRentalSystem.welcome())

system = CarRentalSystem()

c1 = Customer("Arun", "9876543210", "DL12345")
c2 = Customer("Sneha", "9123456780", "DL67890")
system.add_customer(c1)
system.add_customer(c2)

car1 = Car(101, "Toyota Innova", 2000)
car2 = Car(102, "Hyundai i20", 1500)
car3 = Car(103, "Maruti Swift", 1200)
system.add_car(car1)
system.add_car(car2)
system.add_car(car3)

print("\nAvailable Cars:")
system.show_available_cars()

print("\nBooking 1:")
system.make_reservation("Arun", 102, 3)

print("\nBooking 2:")
system.make_reservation("Sneha", 101, 2)

print("\nAvailable Cars After Bookings:")
system.show_available_cars()
