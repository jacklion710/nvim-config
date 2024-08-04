from my_module import calculate_area, greet, is_prime


def main():
    # Test greet function
    name = "Alice"
    greeting = greet(name)
    print(greeting)

    # Test calculate_area function
    length = 5.0
    width = 3.0
    area = calculate_area(length, width)
    print(f"The area of a rectangle with length {length} and width {width} is: {area}")

    # Test is_prime function
    number = 17
    if is_prime(number):
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")


if __name__ == "__main__":
    main()
