print("\n.........................Dictionary.........................\n")

# it is an asscociative data structure, the elementws are unordered and accessed by an associative key
# dictionaries have keys and values
dic = {'USA':100, 'UK':[20, 'London'], 'India':(3, 1)}
print("1. Inserting into dictionary")
print("This is the dictionary:", dic)
index = input("Enter the key to insert the value: ")
value = input("Enter the value to insert: ")
dic[index] = value
print()

print("2. Deletion")
print("This is the dictionary:", dic)
to_delete = input("Enter the key to delete that element: ")
if to_delete in dic:    # to verify the existence of the key in dictionary
    del(dic[to_delete])
    print("After deleting the dictionary: ", dic)
else:
    print("Key is not present")
print()

print("3.Some other functions")
print("Result of len() function : ", len(dic))
print("To see all the keys of dic:", dic.keys())
print("To see all values of dic  :", dic.values())
print()

print("4. To print all the elements with associated key")
for i in dic:
    print(i,":",dic[i])