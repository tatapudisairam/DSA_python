print("\n.........................Selection Sorting.........................\n")

# implementation of selection sort
# 1. Select minimum element from the collection
# 2. Place selected element at appropriate position
# 3. Apply this technique on all remaining elements
def selection_sort(L):
    n = len(L)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if L[position] > L[j]:
                position = j
        temp = L[position]
        L[position] = L[i]
        L[i] = temp


n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
selection_sort(l1)
print("Sorted list: ", l1)