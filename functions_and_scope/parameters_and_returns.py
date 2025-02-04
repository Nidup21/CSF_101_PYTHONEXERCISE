def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Bob")


def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(5, 3)
print(f"The area of the rectangle is: {area}")


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")


def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([5, 2, 8, 1, 9])
print(f"Min: {result[0]}, Max: {result[1]}")


def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([5, 2, 8, 1, 9])
print(f"Min: {result[0]}, Max: {result[1]}")
