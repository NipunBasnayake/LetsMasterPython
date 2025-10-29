class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

acc1 = BankAccount("Bob")
acc1.deposit(100)

print(acc1.balance)

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"{self.brand} running around {self.speed}km/h"

car1 = Car("BMW", 80)
print(car1)