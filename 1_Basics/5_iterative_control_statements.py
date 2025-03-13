print("\n.........................Iterative Control Statements.........................\n")

# usage of while loop (it executes repeatedly untill the condition becomes False)
print("Simple while loop to print n number of digitis starting from 1.")
n = int(input("Enter the value of n:"))
i = 1
while i<=n:
    print(i)
    i = i+1
print("End.")
print()

# usage of for loop
print("Iterating over the string, e.g.: SimbaRoy")
for i in "SimbaRoy":
    print(i)
print()

print("Iterating using range() function")

x = range(int(input("Enter a number: ")))
for i in x:
    print(i)
print()

for i in range(0, int(input("Enter a number to print the even numbers till that number: "))+1, 2):
    print(i)
print()

print("Usage of range function like this range(10, 0, -2)")
for i in range(10, 0, -2):
    print(i)
print()