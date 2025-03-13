print("\n.........................Creating Own Modules.........................\n")

print("1. Using mymodule.py")
import mymodule
n = int(input("Enter how many numbers you want multiply: "))
for_multiply = []
for i in range(n):
    value = eval(input("Enter the value: "))
    for_multiply.append(value)
mymodule.display()
print("The product of all the numbers :", mymodule.my_mul(for_multiply))