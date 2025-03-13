print("\n.........................Quick Sorting.........................\n")

def quick_sort(A, low, high):
    if low<high:
        p = partition(A, low, high)
        quick_sort(A, low, p-1)
        quick_sort(A, p+1, high)

def partition(A, low, high):
    i = low+1
    j = high
    pivot =A[low]
    while(i<j):
        while i<=j and pivot >= A[i]:
            i = i+1
        while i<=j and A[j] > pivot:
            j = j-1
        if i<=j:
            A[i], A[j] = A[j], A[i]
    A[low],  A[j] = A[j], A[low]
    return j

n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
quick_sort(l1, 0, len(l1)-1)
print("Sorted list: ", l1)