from typing import Union, List, TypeVar, Callable, overload, Any
import math

import re
from datetime import datetime
from collections import Counter
from typing import List, Union
from functools import lru_cache

# Type variable for generic handling
T = TypeVar("T", int, str)
NumberOrList = Union[T, List[T]]


# Helper function to apply a function to a single value or list
def singlyList(
    func: Callable[[T], Any], value: NumberOrList[T], error_message: str
) -> Any:
    """Apply a function to either a single value or a list of values."""
    if isinstance(value, list):
        return [func(item) for item in value]

    if (isinstance(value, int) and func.__name__ not in ["is_palindrome"]) or (
        isinstance(value, str) and func.__name__ == "is_palindrome"
    ):
        return func(value)
    raise ValueError(error_message)


# Cached prime checker for repeated calls
@lru_cache(maxsize=1024)
def _check_prime(n: int) -> bool:
    """Efficiently check if a number is prime with caching for performance."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Only check divisibility by 6k±1 up to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


@lru_cache(maxsize=1024)
def _fibonacci_single(n: int) -> int:
    """Calculate Fibonacci number with caching for performance."""
    if n < 2:
        return n

    # Using matrix exponentiation for efficient calculation
    def matrix_mult(A, B):
        return [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],
                A[0][0] * B[0][1] + A[0][1] * B[1][1],
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],
                A[1][0] * B[0][1] + A[1][1] * B[1][1],
            ],
        ]

    def matrix_pow(M, exp):
        result = [[1, 0], [0, 1]]
        while exp:
            if exp % 2:
                result = matrix_mult(result, M)
            M = matrix_mult(M, M)
            exp //= 2
        return result

    F = [[1, 1], [1, 0]]
    return matrix_pow(F, n - 1)[0][0]


def is_even(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are even."""
    if isinstance(number, list):
        return [n % 2 == 0 for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_even' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return number % 2 == 0


def is_odd(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are odd."""
    if isinstance(number, list):
        return [n % 2 != 0 for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_odd' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return number % 2 != 0


def factorial(number: Union[int, List[int]]) -> Union[int, List[int]]:
    """Compute factorial(s)."""

    def _factorial(n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError("Factorial is only defined for non-negative integers. Received value: {}".format(number))
        return math.factorial(n)

    if isinstance(number, list):
        return [_factorial(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'factorial' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return _factorial(number)


def is_prime(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are prime."""

    def _is_prime_wrapper(n: int) -> bool:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError("Prime check is only valid for non-negative integers. Received value: {}".format(n))
        return _check_prime(n)

    if isinstance(number, list):
        return [_is_prime_wrapper(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_prime' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return _is_prime_wrapper(number)


def fibonacci(number: Union[int, List[int]]) -> Union[int, List[int]]:
    """Compute Fibonacci number(s)."""

    def _fibonacci_wrapper(n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError(
                "Fibonacci numbers are only defined for non-negative integers. Received value: {}".format(n)
            )
        return _fibonacci_single(n)

    if isinstance(number, list):
        return [_fibonacci_wrapper(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'fibonacci' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return _fibonacci_wrapper(number)


def is_palindrome(string: Union[str, List[str]]) -> Union[bool, List[bool]]:
    """Check if string(s) are palindromes."""

    def _is_palindrome(s: str) -> bool:
        if not isinstance(s, str):
            raise ValueError("Input must be a string.")
        return s == s[::-1]

    if isinstance(string, list):
        return [_is_palindrome(s) for s in string]
    if not isinstance(string, str):
        raise ValueError(
            "The 'is_palindrome' function expects a string or a list of strings. "
            "Received: {}".format(type(string).__name__)
        )
    if not string:
        raise ValueError("Input string cannot be empty.")
    return _is_palindrome(string)


def is_armstrong(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are Armstrong numbers."""

    def _is_armstrong(n: int) -> bool:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError(
                "Armstrong number check is only valid for non-negative integers."
            )
        digits = str(n)
        order = len(digits)
        return n == sum(int(digit) ** order for digit in digits)

    if isinstance(number, list):
        return [_is_armstrong(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_armstrong' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return _is_armstrong(number)


def is_perfect(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are perfect numbers."""

    def _is_perfect(n: int) -> bool:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 1:
            raise ValueError(
                "Perfect number check is only valid for positive integers. Received value: {}".format(n)
            )

        sum_divisors = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                sum_divisors += i
                if i != n // i:
                    sum_divisors += n // i

        return sum_divisors == n

    if isinstance(number, list):
        return [_is_perfect(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_perfect' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return _is_perfect(number)


def is_harshad(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are Harshad numbers."""

    def _is_harshad(n: int) -> bool:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 1:
            raise ValueError(
                "Harshad number check is only valid for positive integers."
            )
        return n % sum(int(digit) for digit in str(n)) == 0

    if isinstance(number, list):
        return [_is_harshad(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_harshad' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__)
        )
    return _is_harshad(number)


def is_disarium(number: Union[int, List[int]]) -> Union[bool, List[bool]]:
    """Check if number(s) are Disarium numbers."""

    def _is_disarium(n: int) -> bool:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 1:
            raise ValueError(
                "Disarium number check is only valid for positive integers."
            )
        return n == sum(int(digit) ** (i + 1) for i, digit in enumerate(str(n)))

    if isinstance(number, list):
        return [_is_disarium(n) for n in number]
    if not isinstance(number, int):
        raise ValueError(
            "The 'is_disarium' function expects an integer or a list of integers. "
            "Received: {}".format(type(number).__name__),
        )
    return _is_disarium(number)


def camel_to_snake(name: str) -> str:
    """Convert camel case string to snake case."""
    if not isinstance(name, str):
        raise ValueError(
            "The 'camel_to_snake' function expects a string. "
            "Received: {}".format(type(name).__name__)
        )
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def snake_to_camel(name: str) -> str:
    """Convert snake case string to camel case."""
    if not isinstance(name, str):
        raise ValueError(
            "The 'snake_to_camel' function expects a string. "
            "Received: {}".format(type(name).__name__)
        )
    return "".join(word.capitalize() or "_" for word in name.split("_"))


def slugify(text: str) -> str:
    """Convert a string into a URL-friendly slug."""
    if not isinstance(text, str):
        raise ValueError(
            "The 'slugify' function expects a string. "
            "Received: {}".format(type(text).__name__)
        )
    text = re.sub(r"\W+", " ", text)  # Replace non-alphanumeric characters with spaces
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)  # Replace spaces with hyphens
    return text


def time_ago(timestamp: datetime, detailed: bool = True, short: bool = False) -> str:
    """Calculate time ago from a datetime object with multiple granularity options."""
    if not isinstance(timestamp, datetime):
        raise ValueError(
            "The 'time_ago' function expects a datetime object. "
            "Received: {}".format(type(timestamp).__name__)
        )
    now = datetime.now()
    diff = now - timestamp
    seconds = int(diff.total_seconds())

    intervals = [
        ("year", "y", 31536000),  # 365 days
        ("month", "mo", 2592000),  # 30 days
        ("week", "w", 604800),
        ("day", "d", 86400),
        ("hour", "h", 3600),
        ("minute", "m", 60),
        ("second", "s", 1),
    ]

    parts = []
    for name, short_name, duration in intervals:
        value = seconds // duration
        if value:
            seconds %= duration
            if short:
                parts.append(f"{value}{short_name}")
            else:
                parts.append(f"{value} {name}{'s' if value > 1 else ''}")

            if not detailed:
                break

    return " ".join(parts) + " ago" if parts else "just now"


def mean_val(numbers: List[Union[int, float]]) -> float:
    """Calculate the mean of a list of numbers."""
    if not isinstance(numbers, list):
        raise ValueError(
            "The 'mean_val' function expects a list of numbers. "
            "Received: {}".format(type(numbers).__name__)
        )
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def median_val(numbers: List[Union[int, float]]) -> float:
    """Calculate the median of a list of numbers."""
    if not isinstance(numbers, list):
        raise ValueError(
            "The 'median_val' function expects a list of numbers. "
            "Received: {}".format(type(numbers).__name__)
        )
    if not numbers:
        return 0.0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_numbers[n // 2]


def mode_val(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Calculate the mode(s) of a list of numbers."""
    if not isinstance(numbers, list):
        raise ValueError(
            "The 'mode_val' function expects a list of numbers. "
            "Received: {}".format(type(numbers).__name__)
        )
    if not numbers:
        return []
    counts = Counter(numbers)
    max_count = max(counts.values())
    return [number for number, count in counts.items() if count == max_count]


def count_words(text: str) -> int:
    """Count words in a given text."""
    if not isinstance(text, str):
        raise ValueError(
            "The 'count_words' function expects a string. "
            "Received: {}".format(type(text).__name__)
        )
    if not text:
        return 0
    words = re.findall(r'\b\w+\b', text)
    return len(words)



def get_word_count(text: str) -> dict:
    """Count the occurrences of each word in a text."""
    if not isinstance(text, str):
        raise ValueError(
            "The 'get_word_count' function expects a string. "
            "Received: {}".format(type(text).__name__)
        )
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))


def get_char_count(text: str) -> dict:
    """Count the occurrences of each character in a text."""
    if not isinstance(text, str):
        raise ValueError(
            "The 'get_char_count' function expects a string. "
            "Received: {}".format(type(text).__name__)
        )
    return dict(Counter(text))


def get_current_date(format_str: str = '%Y-%m-%d') -> str:
    """Get the current date formatted as string."""
    if not isinstance(format_str, str):
        raise ValueError(
            "The 'get_current_date' function expects a string for format_str."
        )
    now = datetime.now()
    return now.strftime(format_str)


def get_current_time(format_str: str = '%H:%M:%S') -> str:
    """Get the current time formatted as string."""
    if not isinstance(format_str, str):
        raise ValueError(
            "The 'get_current_time' function expects a string for format_str."
        )
    now = datetime.now()
    return now.strftime(format_str)


def get_day_of_week() -> str:
    """Get the current day of the week."""
    now = datetime.now()
    return now.strftime('%A')


def calculate_age(birth_date: str, date_format: str = '%Y-%m-%d') -> int:
    """Calculate age given a birth date string."""
    if not isinstance(birth_date, str) or not isinstance(date_format, str):
        raise ValueError(
            "The 'calculate_age' function expects string arguments for birth_date and date_format."
        )
    try:
        birth_date_obj = datetime.strptime(birth_date, date_format).date()
    except ValueError:
        raise ValueError("Invalid date format. Please use format like YYYY-MM-DD.")
    today = datetime.now().date()
    age = today.year - birth_date_obj.year - ((today.month, today.day) < (birth_date_obj.month, birth_date_obj.day))
    return age


def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError(
            "The 'convert_to_celsius' function expects a number (int or float) for fahrenheit."
        )
    return (fahrenheit - 32) * 5/9


def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise ValueError(
            "The 'convert_to_fahrenheit' function expects a number (int or float) for celsius."
        )
    return (celsius * 9/5) + 32


def kg_to_lbs(kg: float) -> float:
    """Convert kilograms to pounds."""
    if not isinstance(kg, (int, float)):
        raise ValueError(
            "The 'kg_to_lbs' function expects a number (int or float) for kg."
        )
    return kg * 2.20462


def lbs_to_kg(lbs: float) -> float:
    """Convert pounds to kilograms."""
    if not isinstance(lbs, (int, float)):
        raise ValueError(
            "The 'lbs_to_kg' function expects a number (int or float) for lbs."
        )
    return lbs / 2.20462


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    if not isinstance(miles, (int, float)):
        raise ValueError(
            "The 'miles_to_km' function expects a number (int or float) for miles."
        )
    return miles * 1.60934


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    if not isinstance(km, (int, float)):
        raise ValueError(
            "The 'km_to_miles' function expects a number (int or float) for km."
        )
    return km / 1.60934


def average(*args: float) -> float:
    """Calculate the average of a list of numbers."""
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError(
            "The 'average' function expects numbers (int or float) as arguments."
        )
    if not args:
        return 0.0
    return sum(args) / len(args)


def percentage(part: float, whole: float) -> float:
    """Calculate the percentage of a part in relation to a whole."""
    if not all(isinstance(arg, (int, float)) for arg in [part, whole]):
        raise ValueError(
            "The 'percentage' function expects numbers (int or float) for part and whole."
        )
    if whole == 0:
        raise ValueError("The whole value cannot be zero.")
    return 100 * part / whole

def percentile(data: List[float], n: float) -> float:
    """Calculate the nth percentile of a list of numbers."""
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError(
            "The 'percentile' function expects a list of numbers (int or float) for data."
        )
    if not isinstance(n, (int, float)) or n < 0 or n > 100:
        raise ValueError(
            "The 'percentile' function expects a number (int or float) between 0 and 100 for n."
        )
    data.sort()
    k = (len(data) - 1) * n / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    d0 = data[int(f)] * (c - k)
    d1 = data[int(c)] * (k - f)
    return d0 + d1


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two numbers."""
    if not all(isinstance(arg, int) for arg in [a, b]):
        raise ValueError(
            "The 'gcd' function expects integers for a and b."
        )
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two numbers."""
    if not all(isinstance(arg, int) for arg in [a, b]):
        raise ValueError(
            "The 'lcm' function expects integers for a and b."
        )
    return abs(a * b) // gcd(a, b)
