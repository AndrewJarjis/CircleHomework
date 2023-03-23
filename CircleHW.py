import math

print('Welcome to my Circle Tester!')

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius


while True:
    radius_str = input("Please enter the radius of the circle: ")
    if radius_str.replace(".", "", 1).isdigit():
        radius = float(radius_str)
        break
    else:
        print("Invalid input. Please enter a valid number.")

my_circle = Circle(radius)

print("Diameter: {}".format(my_circle.calculate_diameter()))
print("Circumference: {}".format(my_circle.calculate_circumference()))
print("Area: {}".format(my_circle.calculate_area()))

while True:
    answer = input("Would you like to grow the circle? (y/n): ").lower()
    if answer == "y":
        my_circle.grow()
        print("New radius: {}".format(my_circle.get_radius()))
        print("New diameter: {}".format(my_circle.calculate_diameter()))
        print("New circumference: {}".format(my_circle.calculate_circumference()))
        print("New area: {}".format(my_circle.calculate_area()))
    elif answer == "n":
        print("Goodbye! The radius of the circle is {}.".format(my_circle.get_radius()))
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
