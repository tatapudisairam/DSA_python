print("\n.........................Some problems using Recursion.........................\n")

# finding sum of n natural numbers
print("1. Finding sum of n-natural numbers using Recursion")
def sum_of_n_natural_numbers(n): # it takes O(n) time complexity but we can simply write return (n*(n+1))/2 which takes unit time to execute
    if n==1:
        return 1
    else:
        return n + sum_of_n_natural_numbers(n-1)
n = int(input("Enter the value of n to find the sum of n natural numbers: "))
print("Sum is:", sum_of_n_natural_numbers(n))

print("2. Finding value of n-Factorial ")
def factorial_of_n(n):
    if n==0:
        return 1
    else:
        return n*factorial_of_n(n-1)
n = int(input("Enter the value of n to find it's factorial value: "))
print("Factorial value is:", factorial_of_n(n))