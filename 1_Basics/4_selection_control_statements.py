print("\n.........................Selection Control Statements.........................\n")

# if-else statements
if eval(input("Enter your age to check for vote eligible or not: ")) >= 18:
    print("You are eligible")
else:
    print("You are not eligible")
print()

# if-elif-else statements
x = eval(input("Enter a number to check if it is zero or negative or positive: "))
if x==0:
    print("You have entered zero.")
elif x>0:
    print(x, "is positive.")
else:
    print(x, 'is negative.')
print()

# about range function
x = range(5)
print("Result of x in x=range(5)    :", x) # range function creates a generator function which is able to produce each item in sequence
print("Value of x[4] in", x, ':', x[4])
print("type of", x, "is       :", type(x))
print(x)
print()

# range(0, 10, 2) it creates two steps for producing sequence (0, 2, 4, 6, 8)
# range(10, 0, -2) -------> (10, 8, 6, 4, 2)