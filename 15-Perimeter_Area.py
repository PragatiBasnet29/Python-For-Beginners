import math

# Perimeter and Area Calculate

# Square
def square_properties(side_length):
    perimeter = 4 * side_length
    area = side_length ** 2
    return perimeter, area


# Rectangle
def rectangle_properties(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area


# Circle
def circle_properties(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area


# Triangle
def triangle_properties(base, height, side1, side2, side3):
    perimeter = side1 + side2 + side3
    area = 1/2 * (base * height)
    return perimeter, area


# main function Take user inputs
def main():
    print("Basic Shapes Perimeter and Area Calculator V 1.0")
    print("Developed by Sampath Tharanga")
    print("Select a shape:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        side_length = float(input("Enter the side length of the square: "))
        perimeter, area = square_properties(side_length)
        print("Perimeter: ", perimeter)
        print("Area: ", area)
    elif choice == '2':
        length = float(input("Enter the lenght of the rectangle: "))
        width = float(input("Enter the width of the rectangle:"))
        perimeter, area = rectangle_properties(length, width)
        print("Perimeter: ", perimeter)
        print("Area: ", area)
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        perimeter, area = circle_properties(radius)
        print("Perimeter :", perimeter)
        print("Area: ", area)
    elif choice == '4':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter the lenght of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the lenght of side 3: "))
        perimeter, area = triangle_properties(base, height, side1, side2, side3)
        print("Perimeter: ", perimeter)
        print("Area: ", area)
    else:
        print("Invalid choice")


# Call the main function to start the program
main()