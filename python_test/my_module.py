def greet(name: str) -> str:
    """
    Greet the person with the given name.
    """
    return f"Hello, {name}!"


def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    """
    return length * width


def is_prime(number: int) -> bool:
    """
    Check if a number is prime.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
