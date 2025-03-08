def is_even(number):
    """
    Check if a number is even.

    Args:
        number: The number to check

    Returns:
        bool: True if the number is even, False otherwise
    """

    if not isinstance(number, int):
        raise ValueError("Only integers can be even or odd")

    return number % 2 == 0


def fact(number):
    """
    Calculate the factorial of a number.

    Args:
        number: A non-negative integer

    Returns:
        int: The factorial of the number
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Factorial is only defined for non-negative integers")

    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number - 1)
