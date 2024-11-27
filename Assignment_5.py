# Base class for Animals
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class for Dog
class Dog(Animal):
    def move(self):
        print("The dog is running 🐕")


# Derived class for Fish
class Fish(Animal):
    def move(self):
        print("The fish is swimming 🐟")


# Base class for Vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class for Car
class Car(Vehicle):
    def move(self):
        print("Driving the car 🚗")


# Derived class for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying the plane ✈️")


def main():
    # Create instances of animals
    dog = Dog()
    fish = Fish()

    # Create instances of vehicles
    car = Car()
    plane = Plane()

    # List of animals and their movements
    animals = [dog, fish]
    print("Animal Movements:")
    for animal in animals:
        animal.move()

    # List of vehicles and their movements
    vehicles = [car, plane]
    print("\nVehicle Movements:")
    for vehicle in vehicles:
        vehicle.move()


if __name__ == "__main__":
    main()