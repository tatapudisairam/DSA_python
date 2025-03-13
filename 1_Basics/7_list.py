print("\n.........................List.........................\n")

print("1. Insert n number of different types of elements")
n = int(input("Enter the value of n (please enter greater than 2): "))
if n<2:
    print("Enter greater than two and, Re-run the program.")
else:
    l = []
    for i in range(n):
        print("Enter the value for index", i, end=': ')
        l.append((input()))
    print("Final list is:", l)
    print()

    print("2. Accessing list elements")
    print("The element at index-0        :", l[0])
    print("The element at index-1        :", l[1])
    print("The last element(l[-1])       :", l[-1])
    print("The second last element(l[-2]):", l[-2])
    print()

print("3. Concatenation of lists")
l1 = [10, 'Hello', 2.85]
print("List l1 is:", l1)
l2 = l1+[56.5, 'Python']
print("After concatenation l2 = l1+[56.5, 'Python']: ", l2)
print()

print("4. inserting into list")
print("This is the list", l1)
index = int(input("Now enter the index number to insert: "))
value = input("Now enter tha value to insert at that index: ")
l1.insert(index, value)
print("After inserting:", l1)
print()

print("5. Appending in list")
print("This is the list:", l1)
value = input("Enter the value to insert at the last position in this list: ")
l1.append(value)
print("After performing appening:", l1)
print()

# it is used to insert list into a list
print("6. Extend performing on the list")
print("This is the list:", l1)
l1.extend([52.35, 'Simba'])
print("After performing l1.extend([52.35, 'Simba']):", l1)
print()

print("7. Deletion")
print("This is the list:", l1)
index_to_delete = int(input("Enter the index number to delete that element: "))
del(l1[index_to_delete])
print("After deleting:", l1)
print()

print("8. Performing slicing")
print("This is the list:", l1, '\nNow enter the index of starting element and the ending element, it will display the elements from starting to the ending index number, which you have entered.')
starting = int(input("Enter the starting element: "))
ending = int(input("Enter the ending element: "))
print("After perfoming ","l1[", starting,':', (ending+1),']: ', l1[starting:ending+1],  sep='')
l3 = l2[:]
print("It(l3 = l2[:]) will copy all the elements to the list l3.")
print("l3 list is:", l3)
print()

print("9. Converting string to a list using split method")
my_string = input("Enter a large string(sentence): ")
print("After performing split() operation: ", my_string.split())
my_numbers_string = '20,10,40,30'
print("This is the my_numbers_string:", my_numbers_string)
l4 = my_numbers_string.split(',')
print("After performing split(',') method(delimiter is comma):", l4)
print()

print("10. Some other built in functions")
l5 = [10, 54, 2, 61, 15]
print("This is list:", l5)
l5.sort()
print("Performing sort() method   :", l5)
l5.reverse()
print("Performing reverse() method:", l5)
print("Performing len() method    :", len(l5))
print("Performing sum() method    :", sum(l5))
print("Performing max() method    :", max(l5))
print("Performing min() method    :", min(l5))
print("type of l5[1]              :", type(l5[1]))
print("Result of 54 in l5         :", 54 in l5) # in and not in are membership operators which returns boolean value
print("Result of 54 not in l5     :", 54 not in l5)
print()