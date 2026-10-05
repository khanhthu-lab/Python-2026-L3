import math

def is_prime(n):
    if n < 2:
        return False
    # Only need to check divisors up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    if n < 2:
        return False
    total = 0
    for i in range(1, n):          # proper divisors: every divisor except n itself
        if n % i == 0:
            total += i
    return total == n


def remove_dollar_sign(s):
    return s.replace("$", "")


def extract_even(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)
    return result


def factorial(n):
    if n < 0:
        raise ValueError("factorial is only defined for non-negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def print_pattern(m, n):
    for row in range(m):
        cells = []
        for col in range(n):
            on_border = row == 0 or row == m - 1 or col == 0 or col == n - 1
            cells.append("*" if on_border else " ")
        print(" ".join(cells))


# Exercise 1: area of a circle
print("--- Exercise 1 ---")
radius = float(input("Enter circle radius? "))
print("Circle area =", 3.14 * radius ** 2)


# Exercise 2: Celsius -> Fahrenheit
print("\n--- Exercise 2 ---")
celsius_text = input("Enter the temperature in Celsius? ")
fahrenheit = float(celsius_text) * 9 / 5 + 32
print(celsius_text, "(C) =", fahrenheit, "(F)")


# Exercise 3: prime number
print("\n--- Exercise 3 ---")
number = int(input("Enter a number? "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is a NOT prime number")


# Exercise 4: perfect number
print("\n--- Exercise 4 ---")
number = int(input("Enter a number? "))
if is_perfect(number):
    print(number, "is a perfect number")
else:
    print(number, "is a NOT perfect number")


# Exercise 5: favorite color in a list
print("\n--- Exercise 5 ---")
colors = ["Blue", "Yellow", "Black", "Red", "White"]
favorite = input("What is your favorite color? ").strip().capitalize()
if favorite in colors:
    print("Your color is at index", colors.index(favorite), "in my list")
else:
    print("Sorry, I could not find your color")


# Exercise 6: sequences with range()
print("\n--- Exercise 6 ---")
range1 = range(0, 7)          # 0, 1, 2, 3, 4, 5, 6
range2 = range(1, 11, 3)      # 1, 4, 7, 10
range3 = range(5, 0, -1)      # 5, 4, 3, 2, 1
range4 = range(6, -3, -2)     # 6, 4, 2, 0, -2
print("range1:", list(range1))
print("range2:", list(range2))
print("range3:", list(range3))
print("range4:", list(range4))


# Exercise 7: remove_dollar_sign
print("\n--- Exercise 7 ---")
print(remove_dollar_sign("$12$3.50$"))   # 123.50


# Exercise 8: extract_even
print("\n--- Exercise 8 ---")
print(extract_even([1, 4, 5, -1, 10]))   # [4, 10]


# Exercise 9: factorial
print("\n--- Exercise 9 ---")
n = int(input("Enter a non-negative integer? "))
print(f"{n}! =", factorial(n))


# Exercise 10: all divisors of a number
print("\n--- Exercise 10 ---")
n = int(input("Enter a positive integer? "))
print("Divisors of", n, ":", get_divisors(n))


# Exercise 11: distance between two points
print("\n--- Exercise 11 ---")
x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))
print("Distance =", distance((x1, y1), (x2, y2)))


# Exercise 12: hollow rectangle pattern
print("\n--- Exercise 12 ---")
m = int(input("Number of rows (m)? "))
n = int(input("Number of columns (n)? "))
print_pattern(m, n)