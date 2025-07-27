# math_operations.py
import math

def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

def rectangle_area(width, height):
    return width * height

def factorial(n):
    return math.factorial(n)

def gcd(a, b):
    return math.gcd(a, b)

# main_program.py
import math_operations as mo

print("원의 넓이:", mo.circle_area(5))
print("직사각형 넓이:", mo.rectangle_area(10, 5))
print("팩토리얼 5! =", mo.factorial(5))
print("최대공약수(48, 18) =", mo.gcd(48, 18))

