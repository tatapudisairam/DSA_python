print("\n.........................User Defined Functions.........................\n")


# user defined function to add 
def my_add(a, b):
    c = a+b
    return c

def my_mul(x):
    result = 1
    for i in x:
        result = result*i
    return result


print("1. Creating addion function")
print("Give two numbers to add them.")
first = eval(input("Enter the first number: "))
second = eval(input("Enter the second number: "))
print("The addition is: ", my_add(first, second))
print()

print("2. Printing all the members available in a module (math)")
import math
print(dir(math))
# for i in dir(math):
#     print(i)
print()

print("3. First way to access members")
import math
print("Value of pi :", math.pi)
print("Value of e  :", math.e)
print("2 to the power 3 is :", math.pow(2, 3))
print()

print("4. Second way to use (using aliases)")
import math as m
print("Value of pi :", m.pi)
print("Value of e  :", m.e)
print()

# we can directly use the members (no need to use the namespace qualifiers)
print("5. Third way to use")
from math import pi, e
print("Value of pi :", pi)
print("Value of e  :", e)
print()

print("6. Fourth way to use")
from math import pi as PI, e as E
print("Value of pi :", PI)
print("Value of e  :", E)
print()