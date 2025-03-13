print("\n.........................Searching Techniques (Linear and Binary).........................\n")

# function for linear or sequential searching
# it takes O(n) time complexity
def linear_search(l, value):
    index = 0
    while(index<len(l)):
        if l[index] == value:
            return index
        index = index+1
    return -1

# for binary search list should be sorted
# it takes O(logn) time complexity
def binary_serach(l, value):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid] == value:
            return mid
        elif value < l[mid]:
            high = mid-1
        elif value > l[mid]:
            low = mid+1
    return -1

def binary_search_recursive(l2, value, low, high):
    if low>high:
        return -1
    elif low<=high:
        mid = (low+high)//2
        if l2[mid] == value:
            return mid
        elif value < l2[mid]:
            return binary_search_recursive(l2, value, low, mid-1)
        elif value > l2[mid]:
            return binary_search_recursive(l2, value, mid+1, high)

print("1. Implementing Linear Search")
l = [1, 2, 34, "Simba", 65, 54, 35, 44.4, "Roy"]
print("This is the list =", l)
input_value = input("Enter something to check if it is present or not on above list: ")
if input_value.isdigit() or input_value.replace(".","").isdigit(): # for checking numerical values
    input_value = eval(input_value)
result = linear_search(l, input_value)
if result == -1:
    print("Element not found in the above list.")
else:
    print("Element found at index", result)
print()

# for binary search the list should be sorted
print("2. Implementing Binary Search")
l1 = [1, 3, 4, 5, 7, 8, 13, 15, 26, 28, 37, 35, 37, 47, 48, 52, 54, 57, 59, 62, 65, 68, 71, 74, 77, 83, 85, 89, 90]
print("This is the list =", l1)
n = int(input("Enter the element to find it's index: "))
result = binary_serach(l1, n)
if result == -1:
    print("Element not found in the above list")
else:
    print("Element found at index", result)
print()

# binary search using recursion
print("3. Implementing binary search using Recursion")
l2 = [1, 3, 4, 5, 7, 8, 13, 15, 26, 28, 37, 35, 37, 47, 48, 52, 54, 57, 59, 62, 65, 68, 71, 74, 77, 83, 85, 89, 90]
print("This is the list =", l2)
n = int(input("Enter the element to find it's index: "))
result = binary_search_recursive(l2, n, 0, len(l2)-1)
if result == -1:
    print("Element not found in the above list")
else:
    print("Element found at index", result)