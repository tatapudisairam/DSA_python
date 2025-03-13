print("\n.........................Tuple.........................\n")

# tuples are immutable as strings
tup = (10, 'Simba', 2.85)
print("1. Accessing elements of the tuple")
print("This is the tuple:", tup)
print("The element at index-0 :", tup[0])
print("The element at index-1 :", tup[1])
print()

# we can concatenate using +
print("2. Concatenation of tuples")
print("This is the tuple:", tup)
tup2 = tup + (56.5, "Roy")
print("After concatenation like tup2 = tup + (56.5, 'Roy'):", tup2)
print()

print("3. Slicing")
print("This is the tuple:", tup2, '\nNow enter the index of starting element and the ending element, it will display the elements from starting to the ending index number, which you have entered.')
starting = int(input("Enter the starting element: "))
ending = int(input("Enter the ending element: "))
print("After perfoming ","l1[", starting,':', (ending+1),']: ', tup2[starting:ending+1],  sep='')
tup3 = tup2[:]
print("It(tup3 = tup2[:]) will copy all the elements to the tuple tup3.")
print("tup3 list is:", tup3)
print()

print("3. Some other opearations")
tup4 = (10, 54, 2, 61, 15)
print("This is the list:", tup4)
print("Result of len() function:", len(tup4))
print("Result of max() function:", max(tup4))
print("Result of min() function:", min(tup4))
print("Result of sum() function:", sum(tup4))
print("Result of membership operator (54 in tup4):", 54 in tup4)
print("Result of membership operator (54 not in tup4):", 54 not in tup4)
print("Accessing last element of the tuple(tup4[-1]) :", tup4[-1])
print("Accessing second last element of the(tup4[-2]):", tup4[-2])
print("Result of 'is' identity operator(tup3 is tup4):", tup3 is tup4) # it results False because of different objects
tup5 = tup4
print("Result of 'is' identity operator(tup4 is tup5):", tup4 is tup5) # it results True because of same objects
print("Result of '==' identity operator(tup4==tup5)  :", tup4==tup5) # it result True because it contains the same values
