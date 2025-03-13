print("\n.........................Count Sorting.........................\n")

def count_sort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0]*(maxsize+1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j = 0
    while i <= maxsize:
        if carray[i] > 0:
            A[j] = i
            j = j+1
            carray[i] = carray[i]-1
        else:
            i = i+1


n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
count_sort(l1, 0, len(l1)-1)
print("Sorted list: ", l1)
    