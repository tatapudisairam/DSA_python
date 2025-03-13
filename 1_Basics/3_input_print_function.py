print("\n.........................input and print function.........................\n")

# input function is used to get the values from the user
x = input("Enter a value to stroe in the x: ")
print("Type of x in x=input() : ", type(x))   # the type of value returned by the input function is always string
print()

print("Enter two numbers to add ")
x = input("Enter first value : ")
y = input("Enter second value: ")
print("Addition of", x, 'and', y, ':',eval(x) + eval(y))
print()

print("Result of int(5) is   : ", int(5))
print("Result of float(5) is : ", float(5))
print("Result of eval('5') is: ", eval('5')) # eval is used to convert a value to it's respective type
print()

print("Result of 'Simba'+'Roy' : ", 'Simba'+'Roy') # concatenation operator
print("Result of 'Simba'*2     : ", 'Simba'*2)     # repeatation operator
print()

print("Result of print(3, 4)       : ", (3, 4))
print("Result of print(3 + 4)      : ", 3 + 4)
print("Result of print('10', '20') : ", '10', '20')
print("Result of print('10' + '20'): ", '10'+'20')