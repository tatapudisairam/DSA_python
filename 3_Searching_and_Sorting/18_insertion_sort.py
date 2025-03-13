print("\n.........................Insertion Sorting.........................\n")

# implementation of Insertion sorting
# 1. Select one element at a time from the left of the collection
# 2. Insert the element at proper position
# 3. After insertion every element to its left will be sorted
def insertion_sort(L):
    n = len(L)
    for i in range(n):
        cvalue = L[i]
        position = i
        while position>0 and cvalue<L[position-1]:
            L[position] = L[position-1]
            position = position-1
        L[position] = cvalue

n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
insertion_sort(l1)
print("Sorted list: ", l1)