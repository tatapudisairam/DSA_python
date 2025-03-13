print("\n.........................break and continue.........................\n")

# break is used to terminate the loop
print("1. Usage of break statement")
l = [10, 54, 2, 61, 15]
print("List is: ", l)
n = eval(input("Enter a number to check it's position in the above list: "))
index = 0
for i in l:
    if i == n:
        print(i, n, "Found at position: ",index+1)
        break      
    else:
        print(i, n, "Not found")
    index = index+1             
print()

# continue is used to skip the iteration of a loop
print("2. Usage of continue statement")
n = int(input("Enter a number to print the even numbers till that number: "))
exclude = int(input("Enter a even number in that range to avoid that number: "))
for i in range(n+1):
    if i==exclude:
        continue               
    if i%2==0:
        print(i)
print()