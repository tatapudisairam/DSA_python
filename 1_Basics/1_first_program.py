print("\n.........................Hello, Simba!.........................\n")

# type function is used to define the type of data 
print("1. type() function")
print("type(10)                           : ", type(10))
print("type(12.34)                        : ", type(12.34))
print('type("Simba roy")                  : ', type("Simba roy"))
print("type(5+3j)                         : ", type(5+3j))
print("type(True)                         : ", type(True))
print("type(False)                        : ", type(False))
print("""type([1,2,"Simba",1.24])           : """, type([1,2,"Simba",1.24]))
print("""type({1, 2, "Simba", 1.24})        : """, type({1, 2, "Simba", 1.24}))
print("""type((1,2,"Simba", 1.24))          : """, type((1,2,"Simba", 1.24)))
print("""type({"Uk":"HII", 2:"India"})      : """, type({"Uk":"HII", 2:"India"}))
print('''type(frozenset([1,2,"Simba",1.24])): ''', type(frozenset([1,2,"Simba",1.24])))
print('''type(frozenset({1,2,"Simba",1.24})): ''', type(frozenset({1,2,"Simba",1.24})))
print("""type(frozenset((1,2,"Simba",1.24))): """, type(frozenset((1,2,"Simba",1.24))))
print("type(None)                         :", type(None))
print()

# id function is used to print the address of a variable
print("2. id() fucntion")
x, y, z = 1, 2, 3 # python variables are immutable
z = y
print("Address of variable x:",x,": ", id(x))
print("Address of variable y:",y,": ", id(y))
print("Address of variable z:",z,": ", id(z))
z = 20
print(id(z))
print()

# diplaying all keywords
print("3. Diplaying all keywords")
import keyword
print("All keywords: ", keyword.kwlist)
print("Soft keywords: ", keyword.softkwlist)
print()

# Using triple quotes
print("4. Usage of Triple quotes")
s1 = """This is 
Multiline
String."""
s2 = """This sentence contains both 'Single quote' and "Double quote"."""
print(s1)
print(s2)
print()