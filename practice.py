

# 1. Print Hello world!
print("Hello, world!")



# 2. Add Two Numbers
num1 = 5
num2 = 3
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))



# 3. Find the Square Root
import math
num = 16
sqrt = math.sqrt(num)
print("The square root of", num, "is", sqrt)



# 4. Calculate the Area of a Triangle
base = 10
height = 5
area = 0.5 * base * height
print("The area of the triangle is", area)



# 5. Solve Quadratic Equation
import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solutions are {0} and {1}'.format(sol1,sol2))



# 6. Swap Two Variables
x = 5
y = 10
x, y = y, x
print("After swapping x =", x, "and y =", y)



# 7. Generate a Random Number
import random
print("Random number:", random.randint(1, 100))



# 8. Convert Kilometers to Miles
kilometers = 5.5
conv_factor = 0.621371
miles = kilometers * conv_factor
print("{0} kilometers is equal to {1} miles".format(kilometers, miles))



# 9. Convert Celsius To Fahrenheit
celsius = 37.5
fahrenheit = (celsius * 9/5) + 32
print("{0} Celsius is equal to {1} Fahrenheit".format(celsius, fahrenheit))



# 10. Check if a Number is Positive, Negative or 0
num = -5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
